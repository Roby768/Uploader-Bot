import os

class Config(object):
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("1915896583:AAErqDx6EsDZS5aASNq8eKNicHT5c-7COmA", "")
    # The Telegram API things
    APP_ID = int(os.environ.get("961780", ))
    API_HASH = os.environ.get("bbbfa43f067e1e8e2fb41f334d32a6a7")
    # Get these values from my.telegram.org
