import os

from dotenv import load_dotenv

load_dotenv()

# Telegram configs
TELEGRAM_API_NAME = os.environ.get("TELEGRAM_API_NAME")
TELEGRAM_API_ID = int(os.environ.get("TELEGRAM_API_ID"))
TELEGRAM_API_HASH = os.environ.get("TELEGRAM_API_HASH")

# RabbitMQ configs
RABBIT_RAW_QUEUE_NAME = os.environ.get("RABBIT_RAW_QUEUE_NAME")
RABBIT_DELIVERY_MODE = int(os.environ.get("RABBIT_DELIVERY_MODE"))
RABBIT_HOST = os.environ.get("RABBIT_HOST")
RABBIT_PORT = int(os.environ.get("RABBIT_PORT"))
RABBIT_USERNAME = os.environ.get("RABBIT_USERNAME")
RABBIT_PASSWORD = os.environ.get("RABBIT_PASSWORD")
RABBIT_MAX_RETRIES = int(os.environ.get("RABBIT_MAX_RETRIES"))
RABBIT_RETRY_DELAY = int(os.environ.get("RABBIT_RETRY_DELAY"))
