import os

from dotenv import load_dotenv

load_dotenv()


AQUARIUS_URL = os.getenv('AQUARIUS_URL')
SAGINARIUS_URL = os.getenv('SAGINARIUS_URL')
LIBRA_URL = os.getenv('LIBRA_URL')
VIRGO_URL = os.getenv('VIRGO_URL')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')