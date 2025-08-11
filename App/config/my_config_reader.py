#!/usr/bin/python3

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()   #   Подгружаем .env


class Settings(BaseSettings):
    api_id: SecretStr
    api_hash: SecretStr
    channel_url: SecretStr


    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore"
    )


my_config = Settings()