# -*- coding: utf-8 -*-
from tabulate import tabulate

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RedditPipeline(object):
    def __init__(self):
        self.threads = []
        super().__init__()

    def process_item(self, item, spider):
        self.threads.append(item)
        return item

    def close_spider(self, spider):
        # CLI output
        headers = [
            'subreddit', 'upvotes', 'title', 'thread link', 'comments link'
        ]
        data = []
        for t in self.threads:
            subreddit = t['subreddit']
            upvotes = t['upvotes']
            title = t['title'][:40] + (t['title'][40:] and '...')
            thread_link = t['thread_link'][:50] + \
                          (t['thread_link'][50:] and '...')
            comments_link = t['comments_link'][:50] + \
                            (t['comments_link'][50:] and '...')

            data.append(
                [subreddit, upvotes, title, thread_link, comments_link])

        print(tabulate(data, headers=headers, tablefmt='grid'))

        # output to file for Telegram bot usage
        with open('output.txt', 'w') as f:
            for thread in self.threads[:-1]:
                f.write(RedditPipeline.__format_thread_data(thread))
                f.write('\n------------------------------\n')
            f.write(RedditPipeline.__format_thread_data(self.threads[-1]))

    @staticmethod
    def __format_thread_data(thread):
        '''Returns a formatted string with the thread data

        Args:
            thread (dict): Dictionary containing the thread information with
                the following keys: subreddit, title, upvotes, thread_link and
                comment_link.

        Returns:
            str: Formatted string, with one information per line.
        '''
        # TODO treat more carefully this error, possibly raising an exception.
        if not all(
                k in thread
                for k in ('subreddit', 'title', 'upvotes', 'thread_link',
                          'comments_link')):
            return ''
        return "Subreddit: " + thread['subreddit'] + \
               "\nTitle: " + thread['title'] + \
               "\nUpvotes: " + str(thread['upvotes']) + \
               "\nThread link: " + thread['thread_link'] + \
               "\nComments link: " + thread['comments_link']
