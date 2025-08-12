#!/usr/bin/python3


from ..config.my_config_reader import my_config
from telethon import TelegramClient, events, sync
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl
import playsound
import os

sort_post = []  #   Массив для последнего сообщения

#   Запуск телеграм-сессии

client = TelegramClient(session = "test_session.session",
                            api_id = my_config.api_id.get_secret_value(),
                            api_hash = my_config.api_hash.get_secret_value(),
                            system_version = "4.16.30-vxCUSTOM")
client.start()


def start_parsing():    #   Парсинг данных
    last_post = ""
    posts = client.get_messages(my_config.channel_url.get_secret_value(), limit = 20)
    for post in posts:
        post_last = post.text
        if post_last[0] == "💎":
            last_post = post_last
            break
        else:
            continue
    

    if last_post == "":
        return 0
    

    if len(sort_post) == 0:
        sort_post.append(last_post)
        playsound.playsound(f"{os.getcwd()}/App/telegramParse/message.mp3")
        return sort_post[0]
    elif sort_post[0] == last_post:
        return 0
    else:
        sort_post.pop()
        sort_post.append(last_post)
        playsound.playsound(f"{os.getcwd()}/App/telegramParse/message.mp3")
        return sort_post[0]