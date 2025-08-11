#!/usr/bin/python3


from ..config.my_config_reader import my_config
from telethon import TelegramClient, events, sync
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl
import playsound
import os

last_post = []  #   Массив для последнего сообщения

def start_parsing():    #   Парсинг данных
    client = TelegramClient(session = "test_session.session",
                            api_id = my_config.api_id.get_secret_value(),
                            api_hash = my_config.api_hash.get_secret_value(),
                            system_version = "4.16.30-vxCUSTOM")
    client.start()


    posts = client.get_messages(my_config.channel_url.get_secret_value(), limit = 40)
    for post in posts:
        post_last = post.text
        if post_last[0] == "💎":    #   Ищем сообщения с кристаликом
            if len(last_post) == 0:
                last_post.append(post_last)
                client.disconnect()
                playsound.playsound(f"{os.getcwd()}/App/telegramParse/message.mp3")
                return last_post[0]
            elif len(last_post) != 0 and last_post[0] != post_last:
                last_post[0] = post_last
                client.disconnect()
                playsound.playsound(f"{os.getcwd()}/App/telegramParse/message.mp3")
                return last_post[0]
                
            else:
                continue
        else:
            continue
    client.disconnect()
    return 0