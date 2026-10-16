from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceIntegrationInternetGatewayGetOutputPublicIps:
    object: str
    id: str
    ip: str
    region: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceIntegrationInternetGatewayGetOutput:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    public_ips: List[DashboardInstanceIntegrationInternetGatewayGetOutputPublicIps]
    description: Optional[str] = None


class mapDashboardInstanceIntegrationInternetGatewayGetOutputPublicIps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationInternetGatewayGetOutputPublicIps:
        return DashboardInstanceIntegrationInternetGatewayGetOutputPublicIps(
        object=data.get('object'),
        id=data.get('id'),
        ip=data.get('ip'),
        region=data.get('region'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationInternetGatewayGetOutputPublicIps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceIntegrationInternetGatewayGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceIntegrationInternetGatewayGetOutput:
        return DashboardInstanceIntegrationInternetGatewayGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        public_ips=[mapDashboardInstanceIntegrationInternetGatewayGetOutputPublicIps.from_dict(item) for item in data.get('public_ips', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceIntegrationInternetGatewayGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

