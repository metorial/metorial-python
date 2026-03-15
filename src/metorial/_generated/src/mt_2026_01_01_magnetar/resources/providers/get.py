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
    current_version: Optional[ProvidersGetOutputCurrentVersion] = None
    oauth: Optional[ProvidersGetOutputOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapProvidersGetOutputPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersGetOutputPublisher:
        return ProvidersGetOutputPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersGetOutputPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersGetOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersGetOutputCurrentVersion:
        return ProvidersGetOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersGetOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersGetOutputOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersGetOutputOauthAutoRegistration:
        return ProvidersGetOutputOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ProvidersGetOutputOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersGetOutputOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersGetOutputOauth:
        return ProvidersGetOutputOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapProvidersGetOutputOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersGetOutputOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

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
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

