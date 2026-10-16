from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationEnclavesGetOutputEnclaveEnvironment:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
@dataclass
class ManagementInstanceIntegrationEnclavesGetOutput:
    object: str
    id: str
    slug: str
    name: str
    internet_gateway_id: str
    provider_deployment_id: str
    enclave_environment: ManagementInstanceIntegrationEnclavesGetOutputEnclaveEnvironment
    created_at: datetime
    description: Optional[str] = None
    last_used_at: Optional[datetime] = None


class mapManagementInstanceIntegrationEnclavesGetOutputEnclaveEnvironment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationEnclavesGetOutputEnclaveEnvironment:
        return ManagementInstanceIntegrationEnclavesGetOutputEnclaveEnvironment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationEnclavesGetOutputEnclaveEnvironment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationEnclavesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationEnclavesGetOutput:
        return ManagementInstanceIntegrationEnclavesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        internet_gateway_id=data.get('internet_gateway_id'),
        provider_deployment_id=data.get('provider_deployment_id'),
        enclave_environment=mapManagementInstanceIntegrationEnclavesGetOutputEnclaveEnvironment.from_dict(data.get('enclave_environment')) if data.get('enclave_environment') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        last_used_at=datetime.fromisoformat(data.get('last_used_at').replace('Z', '+00:00')) if data.get('last_used_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationEnclavesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

