from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumersCreateMemberSessionOutput:
    access_token: str
    catalog_item_id: Optional[str] = None


class mapConsumersCreateMemberSessionOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersCreateMemberSessionOutput:
        return ConsumersCreateMemberSessionOutput(
        access_token=data.get('access_token'),
        catalog_item_id=data.get('catalog_item_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersCreateMemberSessionOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ConsumersCreateMemberSessionBody:
    integration_id: Optional[str] = None


class mapConsumersCreateMemberSessionBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersCreateMemberSessionBody:
        return ConsumersCreateMemberSessionBody(
        integration_id=data.get('integration_id')
        )

    @staticmethod
    def to_dict(value: Union[ConsumersCreateMemberSessionBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

