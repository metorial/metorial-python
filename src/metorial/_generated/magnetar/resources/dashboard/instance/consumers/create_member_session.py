from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceConsumersCreateMemberSessionOutput:
    access_token: str
    catalog_item_id: Optional[str] = None


class mapDashboardInstanceConsumersCreateMemberSessionOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersCreateMemberSessionOutput:
        return DashboardInstanceConsumersCreateMemberSessionOutput(
        access_token=data.get('access_token'),
        catalog_item_id=data.get('catalog_item_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersCreateMemberSessionOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceConsumersCreateMemberSessionBody:
    integration_id: Optional[str] = None


class mapDashboardInstanceConsumersCreateMemberSessionBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceConsumersCreateMemberSessionBody:
        return DashboardInstanceConsumersCreateMemberSessionBody(
        integration_id=data.get('integration_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceConsumersCreateMemberSessionBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

