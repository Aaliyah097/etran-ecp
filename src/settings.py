import os
from dotenv import load_dotenv


load_dotenv('.env')


class AppConfig:
    ETRAN_USERNAME: str = os.environ.get('ETRAN_USERNAME')
    ETRAN_PASSWORD: str = os.environ.get('ETRAN_PASSWORD')
    ETRAN_URL: str = os.environ.get('ETRAN_URL')


settings = AppConfig()
