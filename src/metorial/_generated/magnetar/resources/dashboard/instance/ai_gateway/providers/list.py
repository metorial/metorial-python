from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayProvidersListOutputItemsFeatures:
    zdr: bool
@dataclass
class DashboardInstanceAiGatewayProvidersListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    supported: bool
    features: DashboardInstanceAiGatewayProvidersListOutputItemsFeatures
    website: Optional[str] = None
    docs: Optional[str] = None
    logo: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayProvidersListOutput:
    object: str
    items: List[DashboardInstanceAiGatewayProvidersListOutputItems]
    pagination: DashboardInstanceAiGatewayProvidersListOutputPagination


class mapDashboardInstanceAiGatewayProvidersListOutputItemsFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProvidersListOutputItemsFeatures:
        return DashboardInstanceAiGatewayProvidersListOutputItemsFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProvidersListOutputItemsFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProvidersListOutputItems:
        return DashboardInstanceAiGatewayProvidersListOutputItems(
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
        features=mapDashboardInstanceAiGatewayProvidersListOutputItemsFeatures.from_dict(data.get('features')) if data.get('features') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProvidersListOutputPagination:
        return DashboardInstanceAiGatewayProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProvidersListOutput:
        return DashboardInstanceAiGatewayProvidersListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceAiGatewayProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAiGatewayProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapDashboardInstanceAiGatewayProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayProvidersListQuery:
        return DashboardInstanceAiGatewayProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

