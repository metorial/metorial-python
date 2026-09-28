from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatEventsGetOutput:
    object: str
    id: str
    type: str
    source: str
    chat_connection_id: str
    occurred_at: datetime
    created_at: datetime
    chat_id: Optional[str] = None
    channel_id: Optional[str] = None
    thread_id: Optional[str] = None
    message_id: Optional[str] = None
    author_id: Optional[str] = None
    provider_event_id: Optional[str] = None
    provider_channel_id: Optional[str] = None
    provider_thread_id: Optional[str] = None
    provider_message_id: Optional[str] = None
    provider_author_id: Optional[str] = None
    payload: Optional[Dict[str, Any]] = None


class mapChatEventsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatEventsGetOutput:
        return ChatEventsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        source=data.get('source'),
        chat_connection_id=data.get('chat_connection_id'),
        chat_id=data.get('chat_id'),
        channel_id=data.get('channel_id'),
        thread_id=data.get('thread_id'),
        message_id=data.get('message_id'),
        author_id=data.get('author_id'),
        provider_event_id=data.get('provider_event_id'),
        provider_channel_id=data.get('provider_channel_id'),
        provider_thread_id=data.get('provider_thread_id'),
        provider_message_id=data.get('provider_message_id'),
        provider_author_id=data.get('provider_author_id'),
        payload=data.get('payload'),
        occurred_at=datetime.fromisoformat(data.get('occurred_at').replace('Z', '+00:00')) if data.get('occurred_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ChatEventsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

