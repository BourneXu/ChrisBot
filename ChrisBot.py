# -*- coding: utf8 -*-
import telegram
import configparser
from handlers import Handlers
from loguru import logger
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class ChrisBot:
    def __init__(self, configfile):
        self.__InitBot(configfile)
        self.Addservices()

    def __InitBot(self, configfile):
        config = configparser.ConfigParser()
        config.read(configfile)
        self.updater = Updater(token=config["bot"]["token"], use_context=True)
        self.dispatcher = self.updater.dispatcher

    def Addservices(self):
        help_handler = CommandHandler("help", Handlers.help)
        self.dispatcher.add_handler(help_handler)
        logger.info("added help_handler")

        # echo_handler = MessageHandler(Filters.text, Handlers.echo)
        # self.dispatcher.add_handler(echo_handler)
        # logger.info("added start_handler")

        tuling_handler = MessageHandler(Filters.text, Handlers.tuling)
        self.dispatcher.add_handler(tuling_handler)
        logger.info("added tuling_handler")

        get_hackernews_handler = CommandHandler("cs", Handlers.get_hackernews)
        self.dispatcher.add_handler(get_hackernews_handler)
        logger.info("added get_hackernews_handler")

        get_dealmoon_handler = CommandHandler("shop", Handlers.get_dealmoon)
        self.dispatcher.add_handler(get_dealmoon_handler)
        logger.info("added get_dealmoon_handler")

    def Run(self):
        self.updater.start_polling()


# bot = telegram.Bot(token=token)


if __name__ == "__main__":
    chrisbot = ChrisBot("./config.ini")
    chrisbot.Run()
