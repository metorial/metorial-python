from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceNetworksGetOutputPublicIps:
    object: str
    id: str
    ip: str
    region: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceNetworksGetOutput:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    public_ips: List[ManagementInstanceNetworksGetOutputPublicIps]
    description: Optional[str] = None


class mapManagementInstanceNetworksGetOutputPublicIps:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworksGetOutputPublicIps:
        return ManagementInstanceNetworksGetOutputPublicIps(
        object=data.get('object'),
        id=data.get('id'),
        ip=data.get('ip'),
        region=data.get('region'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworksGetOutputPublicIps, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceNetworksGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceNetworksGetOutput:
        return ManagementInstanceNetworksGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        public_ips=[mapManagementInstanceNetworksGetOutputPublicIps.from_dict(item) for item in data.get('public_ips', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceNetworksGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

