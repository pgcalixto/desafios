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
        headers = ['subreddit', 'upvotes', 'title', 'thread link', 'comments link']
        data = []
        for t in self.threads:
            subreddit = t['subreddit']
            upvotes = t['upvotes']
            title = t['title'][:40] + (t['title'][40:] and '...')
            thread_link = t['thread_link'][:50] + \
                          (t['thread_link'][50:] and '...')
            comments_link = t['comments_link'][:50] + \
                            (t['comments_link'][50:] and '...')

            data.append([subreddit, upvotes, title, thread_link,
                         comments_link])

        print(tabulate(data, headers=headers, tablefmt='grid'))
