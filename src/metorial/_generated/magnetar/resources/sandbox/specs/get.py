from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxSpecsGetOutput:
    object: str
    id: str
    identifier: str
    memory_gib: float
    cpus: float
    available: bool
    regions: List[str]
    created_at: datetime


class mapSandboxSpecsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxSpecsGetOutput:
        return SandboxSpecsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        memory_gib=data.get('memory_gib'),
        cpus=data.get('cpus'),
        available=data.get('available'),
        regions=data.get('regions', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SandboxSpecsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

