import logging

from telegram.ext import CommandHandler
from telegram.ext import Updater

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def crawl(args):
    pass


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
    crawl(args)
    bot.send_message(chat_id=update.message.chat_id, text="Hello there!")


def main():
    handler = CommandHandler('NadaPraFazer', nothing_to_do, pass_args=True)
    updater = Updater(token='681115372:AAG0rwggK_0VSRIc_yPk4r9TwNckn9wuXec')
    updater.dispatcher.add_handler(handler)
    updater.start_polling()


if __name__ == '__main__':
    main()
