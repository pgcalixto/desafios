import logging

from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from telegram.ext import CommandHandler
from telegram.ext import Updater

from reddit.spiders.subreddits_spider import SubredditSpider

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def crawl(args):
    process = CrawlerProcess(get_project_settings())
    process.crawl(SubredditSpider, subreddits=args)
    process.start()


def nothing_to_do(bot, update, args):
    '''Get threads with high upvotes and send them as Telegram bot text.

    Given a list of subreddits, gets their threads with upvotes greater than or
    equal to 5000, parses their basic informations and send them via Telegram
    bot.

    Args:
        bot (telegram.bot.Bot): Telegram bot instance
        update (telegram.update.Update): Incoming update.
        args (str): List of subreddits, separated by semicolon.
    '''
    # wait for crawling process
    process = Process(target=crawl, args=args)
    process.start()
    process.join()

    # parses thread information and sends 1 thread per bot message
    threads_content = ''
    with open('output.txt', 'r') as f:
        threads_content = f.read()

    threads = threads_content.split("------------------------------")

    for thread in threads:
        bot.send_message(chat_id=update.message.chat_id, text=thread)


def main():
    handler = CommandHandler('NadaPraFazer', nothing_to_do, pass_args=True)
    updater = Updater(token='681115372:AAG0rwggK_0VSRIc_yPk4r9TwNckn9wuXec')
    updater.dispatcher.add_handler(handler)
    updater.start_polling()


if __name__ == '__main__':
    main()
