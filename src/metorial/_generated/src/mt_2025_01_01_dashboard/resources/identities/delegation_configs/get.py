from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class IdentitiesDelegationConfigsGetOutput:
    object: str
    id: str
    status: str
    is_default: bool
    sub_delegation_behavior: str
    sub_delegation_depth: float
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapIdentitiesDelegationConfigsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> IdentitiesDelegationConfigsGetOutput:
        return IdentitiesDelegationConfigsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        sub_delegation_behavior=data.get('sub_delegation_behavior'),
        sub_delegation_depth=data.get('sub_delegation_depth'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[IdentitiesDelegationConfigsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

