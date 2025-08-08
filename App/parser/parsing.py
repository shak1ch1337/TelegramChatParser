from config.my_config_reader import config
from telethon import TelegramClient, events, sync
from telethon.tl.types import MessageEntityTextUrl, MessageEntityUrl


def start_parsing():
    last_post = []
    client = TelegramClient(session = "test_session.session",
                            api_id = config.api_id.get_secret_value(),
                            api_hash = config.api_hash.get_secret_value(),
                            system_version = "4.16.30-vxCUSTOM")
    client.start()


    posts = client.get_messages(config.channel_url.get_secret_value())
    for post in posts:
        post_last = post.text
        if "💎" in post_last:
            if len(last_post) == 0 or last_post[0] != post_last:
                last_post[0] = post_last
            else:
                pass