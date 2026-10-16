from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxImagesVersionsGetOutput:
    object: str
    id: str
    image_id: str
    status: str
    regions: List[str]
    created_at: datetime
    updated_at: datetime
    version_number: Optional[float] = None
    build_id: Optional[str] = None


class mapDashboardInstanceSandboxImagesVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxImagesVersionsGetOutput:
        return DashboardInstanceSandboxImagesVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        image_id=data.get('image_id'),
        version_number=data.get('version_number'),
        build_id=data.get('build_id'),
        status=data.get('status'),
        regions=data.get('regions', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxImagesVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

