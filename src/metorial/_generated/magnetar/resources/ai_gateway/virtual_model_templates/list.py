from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayVirtualModelTemplatesListOutputItemsParameters:
    key: str
    name: str
    description: str
@dataclass
class AiGatewayVirtualModelTemplatesListOutputItems:
    object: str
    slug: str
    name: str
    description: str
    parameters: List[AiGatewayVirtualModelTemplatesListOutputItemsParameters]
    uses_decision_model: bool
@dataclass
class AiGatewayVirtualModelTemplatesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class AiGatewayVirtualModelTemplatesListOutput:
    object: str
    items: List[AiGatewayVirtualModelTemplatesListOutputItems]
    pagination: AiGatewayVirtualModelTemplatesListOutputPagination


class mapAiGatewayVirtualModelTemplatesListOutputItemsParameters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelTemplatesListOutputItemsParameters:
        return AiGatewayVirtualModelTemplatesListOutputItemsParameters(
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelTemplatesListOutputItemsParameters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelTemplatesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelTemplatesListOutputItems:
        return AiGatewayVirtualModelTemplatesListOutputItems(
        object=data.get('object'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        parameters=[mapAiGatewayVirtualModelTemplatesListOutputItemsParameters.from_dict(item) for item in data.get('parameters', []) if item],
        uses_decision_model=data.get('uses_decision_model')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelTemplatesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelTemplatesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelTemplatesListOutputPagination:
        return AiGatewayVirtualModelTemplatesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelTemplatesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayVirtualModelTemplatesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayVirtualModelTemplatesListOutput:
        return AiGatewayVirtualModelTemplatesListOutput(
        object=data.get('object'),
        items=[mapAiGatewayVirtualModelTemplatesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapAiGatewayVirtualModelTemplatesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayVirtualModelTemplatesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

