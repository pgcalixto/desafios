import scrapy


class SubredditSpider(scrapy.Spider):
    name = "subreddit"

    def __init__(self, subreddits=None):
        if subreddits is not None:
            self.start_urls = [
                'https://old.reddit.com/r/' + subreddit + '/top'
                for subreddit in subreddits.split(';')
            ]
        else:
            self.start_urls = []

        super().__init__()

    def parse(self, response):

        for thread in response.xpath("//div[contains(@class, 'thing')]"):

            # parses upvotes
            vote = thread.xpath(
                ".//div[contains(@class, 'score unvoted')]/text()"
            ).extract_first()

            # parses title of thread, thread link and comments link
            title_data = thread.xpath(".//a[contains(@class, 'title')]")
            title = title_data.xpath("./text()").extract_first()
            thread_link = title_data.xpath("./@href").extract_first()

            comments_link = thread.xpath(
                ".//ul[contains(@class, 'buttons')]/li[contains(@class, 'first')]/a/@href"
            ).extract_first()

            yield {
                'upvotes': vote,
                'title': title,
                'thread_link': thread_link,
                'comments_link': comments_link
            }
