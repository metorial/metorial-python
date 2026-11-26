from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayProvidersListOutputItemsFeatures:
    zdr: bool
@dataclass
class AiGatewayProvidersListOutputItems:
    object: str
    id: str
    slug: str
    name: str
    kind: str
    status: str
    supported: bool
    features: AiGatewayProvidersListOutputItemsFeatures
    website: Optional[str] = None
    docs: Optional[str] = None
    logo: Optional[str] = None
@dataclass
class AiGatewayProvidersListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class AiGatewayProvidersListOutput:
    object: str
    items: List[AiGatewayProvidersListOutputItems]
    pagination: AiGatewayProvidersListOutputPagination


class mapAiGatewayProvidersListOutputItemsFeatures:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProvidersListOutputItemsFeatures:
        return AiGatewayProvidersListOutputItemsFeatures(
        zdr=data.get('zdr')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProvidersListOutputItemsFeatures, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProvidersListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProvidersListOutputItems:
        return AiGatewayProvidersListOutputItems(
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
        features=mapAiGatewayProvidersListOutputItemsFeatures.from_dict(data.get('features')) if data.get('features') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProvidersListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProvidersListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProvidersListOutputPagination:
        return AiGatewayProvidersListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProvidersListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayProvidersListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProvidersListOutput:
        return AiGatewayProvidersListOutput(
        object=data.get('object'),
        items=[mapAiGatewayProvidersListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAiGatewayProvidersListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProvidersListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayProvidersListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapAiGatewayProvidersListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayProvidersListQuery:
        return AiGatewayProvidersListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayProvidersListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

