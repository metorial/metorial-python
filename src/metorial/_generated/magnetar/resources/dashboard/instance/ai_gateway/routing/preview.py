from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceAiGatewayRoutingPreviewOutputModel:
    slug: str
    lab_slug: str
@dataclass
class DashboardInstanceAiGatewayRoutingPreviewOutput:
    object: str
    requested: str
    request: Dict[str, Any]
    via: str
    model: DashboardInstanceAiGatewayRoutingPreviewOutputModel
    candidates: List[Dict[str, Any]]


class mapDashboardInstanceAiGatewayRoutingPreviewOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayRoutingPreviewOutputModel:
        return DashboardInstanceAiGatewayRoutingPreviewOutputModel(
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayRoutingPreviewOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceAiGatewayRoutingPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayRoutingPreviewOutput:
        return DashboardInstanceAiGatewayRoutingPreviewOutput(
        object=data.get('object'),
        requested=data.get('requested'),
        request=data.get('request'),
        via=data.get('via'),
        model=mapDashboardInstanceAiGatewayRoutingPreviewOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayRoutingPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceAiGatewayRoutingPreviewBody:
    model: str
    required_features: Optional[List[str]] = None


class mapDashboardInstanceAiGatewayRoutingPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceAiGatewayRoutingPreviewBody:
        return DashboardInstanceAiGatewayRoutingPreviewBody(
        model=data.get('model'),
        required_features=data.get('required_features', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceAiGatewayRoutingPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

