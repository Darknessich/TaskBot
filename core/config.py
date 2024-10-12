from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    bot_token: str = ""
    pg_dns: str = ""
    redis_dns: str = ""
