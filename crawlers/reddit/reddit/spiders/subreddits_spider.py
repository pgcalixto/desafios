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

        subreddit_name = response.url.split('/')[4]
        page_data = []
        for thread in response.xpath("//div[contains(@class, 'thing')]"):

            # parses upvotes
            vote_str = thread.xpath(
                ".//div[contains(@class, 'score unvoted')]/text()"
            ).extract_first()
            if vote_str == '•':
                continue

            vote = float(vote_str[:-1]) * 1000 if vote_str[-1] == 'k' \
                   else float(vote_str)
            if vote < 5000:
                break

            # parses title of thread, thread link and comments link
            title_data = thread.xpath(".//a[contains(@class, 'title')]")
            title = title_data.xpath("./text()").extract_first()
            thread_link = title_data.xpath("./@href").extract_first()
            if thread_link[:3] == '/r/':
                thread_link = 'https://old.reddit.com' + thread_link

            comments_link = thread.xpath(
                ".//ul[contains(@class, 'buttons')]/li[contains(@class, 'first')]/a/@href"
            ).extract_first()

            yield {
                'subreddit': subreddit_name,
                'upvotes': vote,
                'title': title,
                'thread_link': thread_link,
                'comments_link': comments_link
            }

        # if the last item in the page has a score greater than 5000 and there
        # is a link to a next page, follows the link
        next_page = response.xpath(
            "//span[contains(@class, 'next-button')]/a/@href").extract_first()

        if len(page_data) >= 25 and float(
                page_data[-1]['upvotes']) >= 5000 and next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)
