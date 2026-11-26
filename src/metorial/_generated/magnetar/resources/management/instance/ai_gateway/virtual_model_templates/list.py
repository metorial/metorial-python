from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters:
    key: str
    name: str
    description: str
@dataclass
class ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItems:
    object: str
    slug: str
    name: str
    description: str
    parameters: List[ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters]
    uses_decision_model: bool
@dataclass
class ManagementInstanceAiGatewayVirtualModelTemplatesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class ManagementInstanceAiGatewayVirtualModelTemplatesListOutput:
    object: str
    items: List[ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItems]
    pagination: ManagementInstanceAiGatewayVirtualModelTemplatesListOutputPagination


class mapManagementInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters:
        return ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters(
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelTemplatesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItems:
        return ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItems(
        object=data.get('object'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        parameters=[mapManagementInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters.from_dict(item) for item in data.get('parameters', []) if item],
        uses_decision_model=data.get('uses_decision_model')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelTemplatesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelTemplatesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelTemplatesListOutputPagination:
        return ManagementInstanceAiGatewayVirtualModelTemplatesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelTemplatesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayVirtualModelTemplatesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayVirtualModelTemplatesListOutput:
        return ManagementInstanceAiGatewayVirtualModelTemplatesListOutput(
        object=data.get('object'),
        items=[mapManagementInstanceAiGatewayVirtualModelTemplatesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceAiGatewayVirtualModelTemplatesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayVirtualModelTemplatesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

