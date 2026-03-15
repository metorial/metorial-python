from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersGetOutputPublisher:
    object: str
    id: str
    name: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProvidersGetOutputCurrentVersion:
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
class ProvidersGetOutputOauthAutoRegistration:
    status: str
@dataclass
class ProvidersGetOutputOauth:
    status: str
    auto_registration: ProvidersGetOutputOauthAutoRegistration
    callback_url: Optional[str] = None
@dataclass
class ProvidersGetOutputType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class ProvidersGetOutput:
    object: str
    id: str
    access: str
    status: str
    publisher: ProvidersGetOutputPublisher
    identifier: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    type: ProvidersGetOutputType
    tag: str
    current_version: Optional[ProvidersGetOutputCurrentVersion] = None
    oauth: Optional[ProvidersGetOutputOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersGetOutput:
        return ProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        publisher=mapProvidersGetOutputPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapProvidersGetOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        oauth=mapProvidersGetOutputOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        type=mapProvidersGetOutputType.from_dict(data.get('type')) if data.get('type') else None,
        tag=data.get('tag')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

