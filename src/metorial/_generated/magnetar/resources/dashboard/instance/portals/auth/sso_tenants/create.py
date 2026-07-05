from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsAuthSsoTenantsCreateOutputCounts:
    connections: float
@dataclass
class DashboardInstancePortalsAuthSsoTenantsCreateOutput:
    object: str
    id: str
    name: str
    status: str
    client_id: str
    counts: DashboardInstancePortalsAuthSsoTenantsCreateOutputCounts
    created_at: datetime
    updated_at: datetime


class mapDashboardInstancePortalsAuthSsoTenantsCreateOutputCounts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsCreateOutputCounts:
        return DashboardInstancePortalsAuthSsoTenantsCreateOutputCounts(
        connections=data.get('connections')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsCreateOutputCounts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstancePortalsAuthSsoTenantsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsCreateOutput:
        return DashboardInstancePortalsAuthSsoTenantsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        status=data.get('status'),
        client_id=data.get('client_id'),
        counts=mapDashboardInstancePortalsAuthSsoTenantsCreateOutputCounts.from_dict(data.get('counts')) if data.get('counts') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstancePortalsAuthSsoTenantsCreateBody:
    name: str


class mapDashboardInstancePortalsAuthSsoTenantsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsCreateBody:
        return DashboardInstancePortalsAuthSsoTenantsCreateBody(
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

