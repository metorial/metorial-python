from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstancePortalsAuthSsoTenantsCreateOutputCounts:
    connections: float
@dataclass
class ManagementInstancePortalsAuthSsoTenantsCreateOutput:
    object: str
    id: str
    name: str
    status: str
    client_id: str
    counts: ManagementInstancePortalsAuthSsoTenantsCreateOutputCounts
    created_at: datetime
    updated_at: datetime


class mapManagementInstancePortalsAuthSsoTenantsCreateOutputCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsCreateOutputCounts:
        return ManagementInstancePortalsAuthSsoTenantsCreateOutputCounts(
        connections=data.get('connections')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsCreateOutputCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstancePortalsAuthSsoTenantsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsCreateOutput:
        return ManagementInstancePortalsAuthSsoTenantsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        status=data.get('status'),
        client_id=data.get('client_id'),
        counts=mapManagementInstancePortalsAuthSsoTenantsCreateOutputCounts.from_dict(data.get('counts')) if data.get('counts') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstancePortalsAuthSsoTenantsCreateBody:
    name: str


class mapManagementInstancePortalsAuthSsoTenantsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstancePortalsAuthSsoTenantsCreateBody:
        return ManagementInstancePortalsAuthSsoTenantsCreateBody(
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstancePortalsAuthSsoTenantsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

