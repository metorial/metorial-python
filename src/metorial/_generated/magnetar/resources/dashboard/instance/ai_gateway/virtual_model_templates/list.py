from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters:
    key: str
    name: str
    description: str
@dataclass
class DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItems:
    object: str
    slug: str
    name: str
    description: str
    parameters: List[DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters]
    uses_decision_model: bool
@dataclass
class DashboardInstanceAiGatewayVirtualModelTemplatesListOutputPagination:
    has_more_before: bool
    has_more_after: bool
    before: Optional[str] = None
    after: Optional[str] = None
@dataclass
class DashboardInstanceAiGatewayVirtualModelTemplatesListOutput:
    object: str
    items: List[DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItems]
    pagination: DashboardInstanceAiGatewayVirtualModelTemplatesListOutputPagination


class mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters:
        return DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters(
        key=data.get('key'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItems:
        return DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItems(
        object=data.get('object'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        parameters=[mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutputItemsParameters.from_dict(item) for item in data.get('parameters', []) if item],
        uses_decision_model=data.get('uses_decision_model')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelTemplatesListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelTemplatesListOutputPagination:
        return DashboardInstanceAiGatewayVirtualModelTemplatesListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after'),
        before=data.get('before'),
        after=data.get('after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelTemplatesListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayVirtualModelTemplatesListOutput:
        return DashboardInstanceAiGatewayVirtualModelTemplatesListOutput(
        object=data.get('object'),
        items=[mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceAiGatewayVirtualModelTemplatesListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayVirtualModelTemplatesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

