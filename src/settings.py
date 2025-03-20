import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):
    ETRAN_USERNAME: str
    ETRAN_PASSWORD: str
    ETRAN_URL: str

    model_config = SettingsConfigDict(
        env_file=os.getenv("ENV_FILE", ".env"),
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = AppConfig()
print(settings.dict())
