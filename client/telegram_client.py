import logging

from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, Channel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DefaultTelegramClient:
    def __init__(self, api_name, api_id, api_hash):
        self.client = TelegramClient(api_name, api_id, api_hash)

    async def start(self):
        await self.client.start()

    async def get_account_channels_info(self, chat_fetch_chunk_size=200):
        chats = []
        channels_info = {}

        result = await self.client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=chat_fetch_chunk_size,
            hash=0
        ))
        chats.extend(result.chats)

        for chat in chats:
            if isinstance(chat, Channel) and not chat.megagroup:
                channels_info[chat.id] = chat.title

        return channels_info

    def register_message_handler(self, handler, channel_ids):
        @self.client.on(events.NewMessage(chats=channel_ids))
        async def handle_new_message(event):
            await handler(event)

    async def run_until_disconnected(self):
        await self.client.run_until_disconnected()
