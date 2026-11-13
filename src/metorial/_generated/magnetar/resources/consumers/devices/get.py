from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ConsumersDevicesGetOutputClients:
    object: str
    key: str
    name: str
    detected: bool
    installable: bool
    supports_skills: bool
    enabled: bool
    excluded_magic_mcp_server_ids: List[str]
    excluded_skill_ids: List[str]
@dataclass
class ConsumersDevicesGetOutput:
    object: str
    id: str
    status: str
    consumer_profile_id: str
    name: str
    os: str
    arch: str
    app_version: str
    clients: List[ConsumersDevicesGetOutputClients]
    last_seen_at: datetime
    created_at: datetime
    updated_at: datetime
    revoked_at: Optional[datetime] = None


class mapConsumersDevicesGetOutputClients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersDevicesGetOutputClients:
        return ConsumersDevicesGetOutputClients(
        object=data.get('object'),
        key=data.get('key'),
        name=data.get('name'),
        detected=data.get('detected'),
        installable=data.get('installable'),
        supports_skills=data.get('supports_skills'),
        enabled=data.get('enabled'),
        excluded_magic_mcp_server_ids=data.get('excluded_magic_mcp_server_ids', []),
        excluded_skill_ids=data.get('excluded_skill_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ConsumersDevicesGetOutputClients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapConsumersDevicesGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ConsumersDevicesGetOutput:
        return ConsumersDevicesGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        consumer_profile_id=data.get('consumer_profile_id'),
        name=data.get('name'),
        os=data.get('os'),
        arch=data.get('arch'),
        app_version=data.get('app_version'),
        clients=[mapConsumersDevicesGetOutputClients.from_dict(item) for item in data.get('clients', []) if item],
        last_seen_at=datetime.fromisoformat(data.get('last_seen_at').replace('Z', '+00:00')) if data.get('last_seen_at') else None,
        revoked_at=datetime.fromisoformat(data.get('revoked_at').replace('Z', '+00:00')) if data.get('revoked_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ConsumersDevicesGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

