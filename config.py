import os
class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7168558964:AAGi_UEJraz28p2Y73SYSiw2lOikJPhRGIg")

    API_ID = int(os.environ.get("API_ID", "21188057"))

    API_HASH = os.environ.get("API_HASH", "8564fab8db759bb04b1907bd12ed98ef")

    DATABASE = os.environ.get("DATABASE", "mongodb+srv://rohanahamed75:gt4RXJZ1mUtOh4Xv@mmtg.0ong5.mongodb.net/?retryWrites=true&w=majority&appName=mmtg")

    DEV_NAME = os.environ.get("DEV_NAME", "Rahat")

    DEV_ID = set(int(x) for x in os.environ.get("DEV_ID", "8102446291").split())
