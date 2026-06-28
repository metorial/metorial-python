from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceStoresPermissionsGetOutput:
    object: str
    store_id: str
    has_full_access: bool
    permissions: List[str]
    relevant_store_ids: List[str]
    readable_store_ids: List[str]
    writable_store_ids: List[str]


class mapDashboardInstanceStoresPermissionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceStoresPermissionsGetOutput:
        return DashboardInstanceStoresPermissionsGetOutput(
        object=data.get('object'),
        store_id=data.get('store_id'),
        has_full_access=data.get('has_full_access'),
        permissions=data.get('permissions', []),
        relevant_store_ids=data.get('relevant_store_ids', []),
        readable_store_ids=data.get('readable_store_ids', []),
        writable_store_ids=data.get('writable_store_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceStoresPermissionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

