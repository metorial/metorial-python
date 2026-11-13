from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceConsumersCreateMemberSessionOutput:
    access_token: str
    catalog_item_id: Optional[str] = None


class mapManagementInstanceConsumersCreateMemberSessionOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersCreateMemberSessionOutput:
        return ManagementInstanceConsumersCreateMemberSessionOutput(
        access_token=data.get('access_token'),
        catalog_item_id=data.get('catalog_item_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersCreateMemberSessionOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceConsumersCreateMemberSessionBody:
    integration_id: Optional[str] = None


class mapManagementInstanceConsumersCreateMemberSessionBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceConsumersCreateMemberSessionBody:
        return ManagementInstanceConsumersCreateMemberSessionBody(
        integration_id=data.get('integration_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceConsumersCreateMemberSessionBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

