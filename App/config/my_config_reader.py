from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from dotenv import load_dotenv


load_dotenv()   #   Загрузка .env-файла


class Settings(BaseSettings):   #   Конфигурация настроек .env
    api_id: SecretStr
    api_hash: SecretStr
    channel_url: SecretStr

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding = "utf-8",
        extra = "ignore"
    )


config = Settings()