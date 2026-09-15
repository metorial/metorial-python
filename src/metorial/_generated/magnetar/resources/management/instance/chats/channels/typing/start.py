from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceChatsChannelsTypingStartOutput:
    object: str
    started: bool


class mapManagementInstanceChatsChannelsTypingStartOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsChannelsTypingStartOutput:
        return ManagementInstanceChatsChannelsTypingStartOutput(
        object=data.get('object'),
        started=data.get('started')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsChannelsTypingStartOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceChatsChannelsTypingStartBody:
    thread_id: Optional[str] = None
    status: Optional[str] = None


class mapManagementInstanceChatsChannelsTypingStartBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceChatsChannelsTypingStartBody:
        return ManagementInstanceChatsChannelsTypingStartBody(
        thread_id=data.get('thread_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceChatsChannelsTypingStartBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

