import asyncio
import logging

from client.rabbitmq_client import DefaultRabbitMQClient
from client.telegram_client import DefaultTelegramClient
from config import TELEGRAM_API_NAME, TELEGRAM_API_ID, TELEGRAM_API_HASH, RABBIT_RAW_QUEUE_NAME, RABBIT_DELIVERY_MODE, \
    RABBIT_HOST, RABBIT_USERNAME, RABBIT_RETRY_DELAY, RABBIT_MAX_RETRIES, RABBIT_PASSWORD, RABBIT_PORT
from message_handler.message_handler import DefaultMessageHandler

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    # Initialize clients
    rabbit_client = DefaultRabbitMQClient(RABBIT_RAW_QUEUE_NAME, RABBIT_DELIVERY_MODE, RABBIT_HOST, RABBIT_PORT,
                                          RABBIT_USERNAME,
                                          RABBIT_PASSWORD, RABBIT_MAX_RETRIES, RABBIT_RETRY_DELAY)
    telegram_client = DefaultTelegramClient(TELEGRAM_API_NAME, TELEGRAM_API_ID, TELEGRAM_API_HASH)

    # Start clients
    await telegram_client.start()
    rabbit_client.setup_connection()

    # Fetch channel information
    # todo: consider possibility to specify channel ids manually
    channels_info = await telegram_client.get_account_channels_info()
    channel_ids = list(channels_info.keys())

    # Log channel IDs and names
    channels_info_str = ', '.join([f"ID: {ch_id}, Name: {ch_name}" for ch_id, ch_name in channels_info.items()])
    logger.info(f"Channels to monitor: [{channels_info_str}]")

    # Register the message handler
    message_handler = DefaultMessageHandler(rabbit_client, RABBIT_RAW_QUEUE_NAME)
    telegram_client.register_message_handler(message_handler.handle_new_message, channel_ids)

    # Run the clients until disconnected
    await telegram_client.run_until_disconnected()
    rabbit_client.close_connection()


if __name__ == "__main__":
    asyncio.run(main())
