#!/usr/bin/python3


#   Importing libraries

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


#   Load config from .env

load_dotenv()


#   Create class Settings for my_config

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