import json
import logging
from datetime import datetime

from data.message_data import MessageData

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DefaultMessageHandler:
    def __init__(self, rabbit_client, queue_name):
        self.rabbit_client = rabbit_client
        self.queue_name = queue_name

    async def handle_new_message(self, event):
        chat_id = event.chat_id
        chat_title = event.message.chat.title
        msg_text = event.message.text
        logger.info(f"Received message: Group ID: {chat_id} | Group Name: {chat_title}\nMessage: {msg_text}")

        message_data = MessageData(
            post_creation_time=event.message.date,
            scrapped_creation_time=datetime.now(),
            channel_id=chat_id,
            channel_name=chat_title,
            message_text=msg_text
        )

        message_json = json.dumps(message_data.as_dict())
        self.rabbit_client.produce_message(message_json, self.queue_name)
