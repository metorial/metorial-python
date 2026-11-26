from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayLabsListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    status: str
    description: Optional[str] = None
    website: Optional[str] = None
    logo: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayLabsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayLabsListOutput:
    object: str
    items: List[ManagementInstanceAiGatewayLabsListOutputItems]
    pagination: ManagementInstanceAiGatewayLabsListOutputPagination


class mapManagementInstanceAiGatewayLabsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayLabsListOutputItems:
        return ManagementInstanceAiGatewayLabsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        website=data.get('website'),
        logo=data.get('logo'),
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayLabsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayLabsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayLabsListOutputPagination:
        return ManagementInstanceAiGatewayLabsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayLabsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayLabsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayLabsListOutput:
        return ManagementInstanceAiGatewayLabsListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceAiGatewayLabsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceAiGatewayLabsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayLabsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayLabsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceAiGatewayLabsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayLabsListQuery:
        return ManagementInstanceAiGatewayLabsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayLabsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

