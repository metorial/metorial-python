from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSandboxRegionsGetOutputArea:
    id: str
    name: str
@dataclass
class ManagementInstanceSandboxRegionsGetOutput:
    object: str
    id: str
    name: str
    area: ManagementInstanceSandboxRegionsGetOutputArea
    is_default: bool
    availability: str


class mapManagementInstanceSandboxRegionsGetOutputArea:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxRegionsGetOutputArea:
        return ManagementInstanceSandboxRegionsGetOutputArea(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxRegionsGetOutputArea, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSandboxRegionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSandboxRegionsGetOutput:
        return ManagementInstanceSandboxRegionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        area=mapManagementInstanceSandboxRegionsGetOutputArea.from_dict(data.get('area')) if data.get('area') else None,
        is_default=data.get('is_default'),
        availability=data.get('availability')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSandboxRegionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

