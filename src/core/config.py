import os

from dotenv import dotenv_values

env = dotenv_values()


def get_string(setting: str) -> str:
    return env.get(setting) or os.getenv(setting)


TELEGRAM_TOKEN = get_string("TELEGRAM_TOKEN")
ANN_TELEGRAM_ID = get_string("ANN_TELEGRAM_ID")
