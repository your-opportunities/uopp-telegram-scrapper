from dataclasses import dataclass
from datetime import datetime


@dataclass
class MessageData:
    post_creation_time: datetime
    scrapped_creation_time: datetime
    channel_id: int
    channel_name: str
    message_text: str

    def as_dict(self):
        return {
            "post_creation_time": self.post_creation_time.isoformat(),
            "scrapped_creation_time": self.scrapped_creation_time.isoformat(),
            "channel_id": self.channel_id,
            "channel_name": self.channel_name,
            "message_text": self.message_text
        }
