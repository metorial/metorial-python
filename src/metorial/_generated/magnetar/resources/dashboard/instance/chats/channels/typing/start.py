from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceChatsChannelsTypingStartOutput:
    object: str
    started: bool


class mapDashboardInstanceChatsChannelsTypingStartOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsTypingStartOutput:
        return DashboardInstanceChatsChannelsTypingStartOutput(
        object=data.get('object'),
        started=data.get('started')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsTypingStartOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceChatsChannelsTypingStartBody:
    thread_id: Optional[str] = None
    status: Optional[str] = None


class mapDashboardInstanceChatsChannelsTypingStartBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceChatsChannelsTypingStartBody:
        return DashboardInstanceChatsChannelsTypingStartBody(
        thread_id=data.get('thread_id'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceChatsChannelsTypingStartBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

