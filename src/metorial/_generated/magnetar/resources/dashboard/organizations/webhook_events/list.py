from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardOrganizationsWebhookEventsListOutputItems:
    object: str
    name: str
@dataclass
class DashboardOrganizationsWebhookEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardOrganizationsWebhookEventsListOutput:
    items: List[DashboardOrganizationsWebhookEventsListOutputItems]
    pagination: DashboardOrganizationsWebhookEventsListOutputPagination


class mapDashboardOrganizationsWebhookEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsWebhookEventsListOutputItems:
        return DashboardOrganizationsWebhookEventsListOutputItems(
        object=data.get('object'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsWebhookEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsWebhookEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsWebhookEventsListOutputPagination:
        return DashboardOrganizationsWebhookEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsWebhookEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardOrganizationsWebhookEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsWebhookEventsListOutput:
        return DashboardOrganizationsWebhookEventsListOutput(
        items=[mapDashboardOrganizationsWebhookEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardOrganizationsWebhookEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardOrganizationsWebhookEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

