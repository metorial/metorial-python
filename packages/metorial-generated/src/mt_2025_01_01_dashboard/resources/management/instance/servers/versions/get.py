from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServersVersionsGetOutputServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersVersionsGetOutput:
    object: str
    id: str
    identifier: str
    server_id: str
    server_variant_id: str
    get_launch_params: str
    source: Dict[str, Any]
    schema: Dict[str, Any]
    server: ManagementInstanceServersVersionsGetOutputServer
    created_at: datetime


class mapManagementInstanceServersVersionsGetOutputServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersVersionsGetOutputServer:
        return ManagementInstanceServersVersionsGetOutputServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersVersionsGetOutputServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersVersionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersVersionsGetOutput:
        return ManagementInstanceServersVersionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        server_variant_id=data.get('server_variant_id'),
        get_launch_params=data.get('get_launch_params'),
        source=data.get('source'),
        schema=data.get('schema'),
        server=mapManagementInstanceServersVersionsGetOutputServer.from_dict(data.get('server')) if data.get('server') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersVersionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

