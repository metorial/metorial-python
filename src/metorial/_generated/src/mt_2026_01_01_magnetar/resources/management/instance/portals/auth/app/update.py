from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsAuthAppUpdateOutput:
    object: str
    id: str
    email_whitelist: List[str]
    created_at: datetime
    updated_at: datetime
    slug: Optional[str] = None


class mapManagementInstancePortalsAuthAppUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthAppUpdateOutput:
        return ManagementInstancePortalsAuthAppUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        email_whitelist=data.get('email_whitelist', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthAppUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsAuthAppUpdateBody:
    email_whitelist: Optional[List[str]] = None


class mapManagementInstancePortalsAuthAppUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthAppUpdateBody:
        return ManagementInstancePortalsAuthAppUpdateBody(
        email_whitelist=data.get('email_whitelist', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthAppUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

