from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProvidersGetOutputOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class ManagementInstanceProvidersGetOutputPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceProvidersGetOutputEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceProvidersGetOutputDefaultVariantCurrentVersion:
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
class ManagementInstanceProvidersGetOutputDefaultVariant:
    object: str
    id: str
    tag: str
    identifier: str
    provider_id: str
    is_default: bool
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    current_version: Optional[ManagementInstanceProvidersGetOutputDefaultVariantCurrentVersion] = None
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
class ManagementInstanceProvidersGetOutputType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceProvidersGetOutputOauthAutoRegistration:
    status: str
@dataclass
class ManagementInstanceProvidersGetOutputOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[ManagementInstanceProvidersGetOutputOauthAutoRegistration] = None
@dataclass
class ManagementInstanceProvidersGetOutput:
    object: str
    id: str
    access: str
    status: str
    publisher: ManagementInstanceProvidersGetOutputPublisher
    entry: ManagementInstanceProvidersGetOutputEntry
    type: ManagementInstanceProvidersGetOutputType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[ManagementInstanceProvidersGetOutputOwnerTenant] = None
    default_variant: Optional[ManagementInstanceProvidersGetOutputDefaultVariant] = None
    current_version: Optional[ManagementInstanceProvidersGetOutputCurrentVersion] = None
    oauth: Optional[ManagementInstanceProvidersGetOutputOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProvidersGetOutputOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputOwnerTenant:
        return ManagementInstanceProvidersGetOutputOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutputPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputPublisher:
        return ManagementInstanceProvidersGetOutputPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutputEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputEntry:
        return ManagementInstanceProvidersGetOutputEntry(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutputDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputDefaultVariantCurrentVersion:
        return ManagementInstanceProvidersGetOutputDefaultVariantCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutputDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputDefaultVariant:
        return ManagementInstanceProvidersGetOutputDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapManagementInstanceProvidersGetOutputDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputCurrentVersion:
        return ManagementInstanceProvidersGetOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        provider_id=data.get('provider_id'),
        is_current=data.get('is_current'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        specification_id=data.get('specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutputType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputType:
        return ManagementInstanceProvidersGetOutputType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutputOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputOauthAutoRegistration:
        return ManagementInstanceProvidersGetOutputOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutputOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutputOauth:
        return ManagementInstanceProvidersGetOutputOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapManagementInstanceProvidersGetOutputOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutputOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProvidersGetOutput:
        return ManagementInstanceProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapManagementInstanceProvidersGetOutputOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapManagementInstanceProvidersGetOutputPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapManagementInstanceProvidersGetOutputEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapManagementInstanceProvidersGetOutputDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapManagementInstanceProvidersGetOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapManagementInstanceProvidersGetOutputType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapManagementInstanceProvidersGetOutputOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
        identifier=data.get('identifier'),
        tag=data.get('tag'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
