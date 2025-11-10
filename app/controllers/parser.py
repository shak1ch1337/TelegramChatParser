#!/usr/bin/python3


#   Importing libraries

from ..config.my_config_reader import my_config
from telethon import TelegramClient, events, sync
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl
import os


sort_posts = [] #   Array for last message

#   Create and starting telegram session

client = TelegramClient(session = "parsing.session",
                        api_id = my_config.api_id.get_secret_value(),
                        api_hash = my_config.api_hash.get_secret_value(),
                        system_version = "4.16.30-vxCUSTOM")
client.start()


#   Start webscrapping messages from telegram-channel

def startParsing():
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
    

    if (len(sort_posts) == 0):
        sort_posts.append(last_post)
        return sort_posts[0]
    elif sort_posts[0] == last_post:
        return 0
    else:
        sort_posts.pop()
        sort_posts.append(last_post)
        return sort_posts[0]