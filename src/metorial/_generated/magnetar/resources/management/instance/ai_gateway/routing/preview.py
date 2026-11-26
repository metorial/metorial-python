from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceAiGatewayRoutingPreviewOutputModel:
    slug: str
    lab_slug: str
@dataclass
class ManagementInstanceAiGatewayRoutingPreviewOutput:
    object: str
    requested: str
    request: Dict[str, Any]
    via: str
    model: ManagementInstanceAiGatewayRoutingPreviewOutputModel
    candidates: List[Dict[str, Any]]


class mapManagementInstanceAiGatewayRoutingPreviewOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayRoutingPreviewOutputModel:
        return ManagementInstanceAiGatewayRoutingPreviewOutputModel(
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayRoutingPreviewOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceAiGatewayRoutingPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayRoutingPreviewOutput:
        return ManagementInstanceAiGatewayRoutingPreviewOutput(
        object=data.get('object'),
        requested=data.get('requested'),
        request=data.get('request'),
        via=data.get('via'),
        model=mapManagementInstanceAiGatewayRoutingPreviewOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayRoutingPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceAiGatewayRoutingPreviewBody:
    model: str
    required_features: Optional[List[str]] = None


class mapManagementInstanceAiGatewayRoutingPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceAiGatewayRoutingPreviewBody:
        return ManagementInstanceAiGatewayRoutingPreviewBody(
        model=data.get('model'),
        required_features=data.get('required_features', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceAiGatewayRoutingPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

