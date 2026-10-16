from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxRegionsGetOutputArea:
    id: str
    name: str
@dataclass
class DashboardInstanceSandboxRegionsGetOutput:
    object: str
    id: str
    name: str
    area: DashboardInstanceSandboxRegionsGetOutputArea
    is_default: bool
    availability: str


class mapDashboardInstanceSandboxRegionsGetOutputArea:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxRegionsGetOutputArea:
        return DashboardInstanceSandboxRegionsGetOutputArea(
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxRegionsGetOutputArea, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSandboxRegionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxRegionsGetOutput:
        return DashboardInstanceSandboxRegionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        area=mapDashboardInstanceSandboxRegionsGetOutputArea.from_dict(data.get('area')) if data.get('area') else None,
        is_default=data.get('is_default'),
        availability=data.get('availability')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxRegionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

