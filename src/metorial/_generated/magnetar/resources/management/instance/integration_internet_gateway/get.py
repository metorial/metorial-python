from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationInternetGatewayGetOutputPublicIps:
    object: str
    id: str
    ip: str
    region: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceIntegrationInternetGatewayGetOutput:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    public_ips: List[ManagementInstanceIntegrationInternetGatewayGetOutputPublicIps]
    description: Optional[str] = None


class mapManagementInstanceIntegrationInternetGatewayGetOutputPublicIps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationInternetGatewayGetOutputPublicIps:
        return ManagementInstanceIntegrationInternetGatewayGetOutputPublicIps(
        object=data.get('object'),
        id=data.get('id'),
        ip=data.get('ip'),
        region=data.get('region'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationInternetGatewayGetOutputPublicIps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationInternetGatewayGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationInternetGatewayGetOutput:
        return ManagementInstanceIntegrationInternetGatewayGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        public_ips=[mapManagementInstanceIntegrationInternetGatewayGetOutputPublicIps.from_dict(item) for item in data.get('public_ips', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationInternetGatewayGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

