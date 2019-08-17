import os
import json
import requests
import telegram
import configparser
import fake_useragent
from loguru import logger
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class Handlers:
    @staticmethod
    def help(update, context):
        logger.debug(update.message.chat_id)
        context.bot.send_message(
            chat_id=update.message.chat_id,
            text="""
            我是蛋蛋小分队专属订制 Bot, please talk to me!\n#######################\n回复我: \n1. /help 查看帮助，支持的命令\n2. /cs   查看计算机类热门信息, 来自 Hacker News等\n3. /shop 查看购物类热门信息, 来自 北美烧钱快报 等
            ...\n#######################\n已接入图灵机器人, 直接回复, 可与我聊天哦~
            """,
            parse_mode=telegram.ParseMode.MARKDOWN,
        )

    @staticmethod
    def echo(update, context):
        logger.debug(update.message.chat_id)
        context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    @staticmethod
    def tuling(update, context):
        # Try to read config to get apiKey and userId
        try:
            config = configparser.ConfigParser()
            config.read("./config.ini")
            apiKey = config["tuling"]["apiKey"]
            userId = config["tuling"]["userId"]
        except:
            raise ValueError("Config file `config.ini` is missing.")

        url = "http://openapi.tuling123.com/openapi/api/v2"

        payload = {
            "reqType": 0,
            "perception": {
                "inputText": {"text": update.message.text},
                "inputImage": {"url": "imageUrl"},
                "selfInfo": {"location": {"city": "上海", "province": "上海", "street": "南京东路"}},
            },
            "userInfo": {"apiKey": apiKey, "userId": userId},
        }

        headers = {"Content-Type": "text/json"}
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        res = response.json()
        try:
            restext = res["results"][0]["values"]["text"]
        except:
            restext = "我貌似挂了..."
        logger.debug(update.message.chat_id)
        context.bot.send_message(chat_id=update.message.chat_id, text=restext)

    @staticmethod
    def get_hackernews(update, context):
        url = "https://news.ycombinator.com/"
        res = requests.get(url)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        newslist = soup.select('td[class="title"]')
        newsletter = ""
        # hackernews = []
        for i in range(1, min(6, len(newslist) // 2 + 1)):
            link = (newslist[i * 2 - 1]).a.get("href")
            title = (newslist[i * 2 - 1]).text
            # hackernews.append((link, title))
            newsletter += "{}. [{}]({})\n".format(i, title, link)
        logger.debug(update.message.chat_id)
        context.bot.send_message(
            chat_id=update.message.chat_id, text=newsletter, parse_mode=telegram.ParseMode.MARKDOWN
        )

    @staticmethod
    def get_dealmoon(update, context):
        url = "https://www.dealmoon.cn/"
        headers = {"user-agent": Handlers.get_fake_useragent(), "authority": "www.dealmoon.cn"}
        res = requests.get(url, headers=headers)
        html = res.text
        soup = BeautifulSoup(html, "html.parser")
        dealhot = soup.select('div[class="box_item box_item_new"]')
        dealletter = ""
        for i in range(1, min(9, len(dealhot) + 1)):
            link = dealhot[i - 1].a.get("href")
            title = dealhot[i - 1].text.strip()
            dealletter += "{}. [{}]({})\n".format(i, title, link)
        logger.debug(update.message.chat_id)
        context.bot.send_message(
            chat_id=update.message.chat_id, text=dealletter, parse_mode=telegram.ParseMode.MARKDOWN
        )

    @staticmethod
    def get_fake_useragent():
        path = os.getcwd() + "/fake_useragent.json"
        ua = fake_useragent.UserAgent(path=path)
        return ua.random

