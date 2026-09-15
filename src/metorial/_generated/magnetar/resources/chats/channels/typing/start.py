from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ChatsChannelsTypingStartOutput:
    object: str
    started: bool


class mapChatsChannelsTypingStartOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsTypingStartOutput:
        return ChatsChannelsTypingStartOutput(
        object=data.get('object'),
        started=data.get('started')
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsTypingStartOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ChatsChannelsTypingStartBody:
    thread_id: Optional[str] = None
    status: Optional[str] = None


class mapChatsChannelsTypingStartBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ChatsChannelsTypingStartBody:
        return ChatsChannelsTypingStartBody(
        thread_id=data.get('thread_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ChatsChannelsTypingStartBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

