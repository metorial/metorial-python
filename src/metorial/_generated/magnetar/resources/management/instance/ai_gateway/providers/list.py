from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayProvidersListOutputItemsFeatures:
    zdr: bool
@dataclass
class ManagementInstanceAiGatewayProvidersListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    supported: bool
    features: ManagementInstanceAiGatewayProvidersListOutputItemsFeatures
    website: Optional[str] = None
    docs: Optional[str] = None
    logo: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayProvidersListOutput:
    object: str
    items: List[ManagementInstanceAiGatewayProvidersListOutputItems]
    pagination: ManagementInstanceAiGatewayProvidersListOutputPagination


class mapManagementInstanceAiGatewayProvidersListOutputItemsFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProvidersListOutputItemsFeatures:
        return ManagementInstanceAiGatewayProvidersListOutputItemsFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProvidersListOutputItemsFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProvidersListOutputItems:
        return ManagementInstanceAiGatewayProvidersListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        kind=data.get('kind'),
        website=data.get('website'),
        docs=data.get('docs'),
        logo=data.get('logo'),
        status=data.get('status'),
        supported=data.get('supported'),
        features=mapManagementInstanceAiGatewayProvidersListOutputItemsFeatures.from_dict(data.get('features')) if data.get('features') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProvidersListOutputPagination:
        return ManagementInstanceAiGatewayProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProvidersListOutput:
        return ManagementInstanceAiGatewayProvidersListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceAiGatewayProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceAiGatewayProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceAiGatewayProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayProvidersListQuery:
        return ManagementInstanceAiGatewayProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

