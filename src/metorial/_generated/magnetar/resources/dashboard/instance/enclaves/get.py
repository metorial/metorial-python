from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceEnclavesGetOutputEnclaveEnvironment:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
@dataclass
class DashboardInstanceEnclavesGetOutput:
    object: str
    id: str
    slug: str
    name: str
    network_id: str
    provider_deployment_id: str
    enclave_environment: DashboardInstanceEnclavesGetOutputEnclaveEnvironment
    created_at: datetime
    description: Optional[str] = None
    last_used_at: Optional[datetime] = None


class mapDashboardInstanceEnclavesGetOutputEnclaveEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceEnclavesGetOutputEnclaveEnvironment:
        return DashboardInstanceEnclavesGetOutputEnclaveEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceEnclavesGetOutputEnclaveEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceEnclavesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceEnclavesGetOutput:
        return DashboardInstanceEnclavesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        network_id=data.get('network_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        enclave_environment=mapDashboardInstanceEnclavesGetOutputEnclaveEnvironment.from_dict(data.get('enclave_environment')) if data.get('enclave_environment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceEnclavesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

