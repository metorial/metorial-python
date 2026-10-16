from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxRegionsGetOutputArea:
    id: str
    name: str
@dataclass
class SandboxRegionsGetOutput:
    object: str
    id: str
    name: str
    area: SandboxRegionsGetOutputArea
    is_default: bool
    availability: str


class mapSandboxRegionsGetOutputArea:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxRegionsGetOutputArea:
        return SandboxRegionsGetOutputArea(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[SandboxRegionsGetOutputArea, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSandboxRegionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxRegionsGetOutput:
        return SandboxRegionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        area=mapSandboxRegionsGetOutputArea.from_dict(data.get('area')) if data.get('area') else None,
        is_default=data.get('is_default'),
        availability=data.get('availability')
        )

    @staticmethod
    def to_dict(value: Union[SandboxRegionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

