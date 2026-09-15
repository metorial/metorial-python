from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementOrganizationWebhookEventsListOutputItems:
    object: str
    name: str
@dataclass
class ManagementOrganizationWebhookEventsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementOrganizationWebhookEventsListOutput:
    items: List[ManagementOrganizationWebhookEventsListOutputItems]
    pagination: ManagementOrganizationWebhookEventsListOutputPagination


class mapManagementOrganizationWebhookEventsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationWebhookEventsListOutputItems:
        return ManagementOrganizationWebhookEventsListOutputItems(
        object=data.get('object'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationWebhookEventsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationWebhookEventsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationWebhookEventsListOutputPagination:
        return ManagementOrganizationWebhookEventsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationWebhookEventsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementOrganizationWebhookEventsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementOrganizationWebhookEventsListOutput:
        return ManagementOrganizationWebhookEventsListOutput(
        items=[mapManagementOrganizationWebhookEventsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementOrganizationWebhookEventsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementOrganizationWebhookEventsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

