from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersGetOutputPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProvidersGetOutputCurrentVersion:
    object: str
    id: str
    version: str
    provider_id: str
    is_current: bool
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    specification_id: Optional[str] = None
@dataclass
class ManagementInstanceProvidersGetOutputOauthAutoRegistration:
    status: str
@dataclass
class ManagementInstanceProvidersGetOutputOauth:
    status: str
    auto_registration: ManagementInstanceProvidersGetOutputOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class ManagementInstanceProvidersGetOutputType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceProvidersGetOutput:
    object: str
    id: str
    access: str
    status: str
    publisher: ManagementInstanceProvidersGetOutputPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    type: ManagementInstanceProvidersGetOutputType
    tag: str
    current_version: Optional[ManagementInstanceProvidersGetOutputCurrentVersion] = None
    oauth: Optional[ManagementInstanceProvidersGetOutputOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutput:
        return ManagementInstanceProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapManagementInstanceProvidersGetOutputPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapManagementInstanceProvidersGetOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapManagementInstanceProvidersGetOutputOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        type=mapManagementInstanceProvidersGetOutputType.from_dict(data.get('type')) if data.get('type') else None,
        tag=data.get('tag')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

