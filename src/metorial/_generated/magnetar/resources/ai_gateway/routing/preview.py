from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class AiGatewayRoutingPreviewOutputModel:
    slug: str
    lab_slug: str
@dataclass
class AiGatewayRoutingPreviewOutput:
    object: str
    requested: str
    request: Dict[str, Any]
    via: str
    model: AiGatewayRoutingPreviewOutputModel
    candidates: List[Dict[str, Any]]


class mapAiGatewayRoutingPreviewOutputModel:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayRoutingPreviewOutputModel:
        return AiGatewayRoutingPreviewOutputModel(
        slug=data.get('slug'),
        lab_slug=data.get('lab_slug')
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayRoutingPreviewOutputModel, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapAiGatewayRoutingPreviewOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayRoutingPreviewOutput:
        return AiGatewayRoutingPreviewOutput(
        object=data.get('object'),
        requested=data.get('requested'),
        request=data.get('request'),
        via=data.get('via'),
        model=mapAiGatewayRoutingPreviewOutputModel.from_dict(data.get('model')) if data.get('model') else None,
        candidates=data.get('candidates', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayRoutingPreviewOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class AiGatewayRoutingPreviewBody:
    model: str
    required_features: Optional[List[str]] = None


class mapAiGatewayRoutingPreviewBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> AiGatewayRoutingPreviewBody:
        return AiGatewayRoutingPreviewBody(
        model=data.get('model'),
        required_features=data.get('required_features', [])
        )

    @staticmethod
    def to_dict(value: Union[AiGatewayRoutingPreviewBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

