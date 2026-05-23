from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceDocumentsPermissionsGetOutput:
    object: str
    document_id: str
    is_owner: bool
    has_full_access: bool
    permissions: List[str]
    relevant_store_ids: List[str]
    readable_store_ids: List[str]
    writable_store_ids: List[str]


class mapManagementInstanceDocumentsPermissionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceDocumentsPermissionsGetOutput:
        return ManagementInstanceDocumentsPermissionsGetOutput(
        object=data.get('object'),
        document_id=data.get('document_id'),
        is_owner=data.get('is_owner'),
        has_full_access=data.get('has_full_access'),
        permissions=data.get('permissions', []),
        relevant_store_ids=data.get('relevant_store_ids', []),
        readable_store_ids=data.get('readable_store_ids', []),
        writable_store_ids=data.get('writable_store_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceDocumentsPermissionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

