from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProvidersGetOutputOwnerTenant:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
@dataclass
class DashboardInstanceProvidersGetOutputPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProvidersGetOutputEntry:
    object: str
    id: str
    identifier: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceProvidersGetOutputDefaultVariantCurrentVersion:
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
class DashboardInstanceProvidersGetOutputDefaultVariant:
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
    current_version: Optional[DashboardInstanceProvidersGetOutputDefaultVariantCurrentVersion] = None
@dataclass
class DashboardInstanceProvidersGetOutputCurrentVersion:
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
class DashboardInstanceProvidersGetOutputType:
    object: str
    id: str
    name: str
    config: Dict[str, Any]
    triggers: Dict[str, Any]
    auth: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceProvidersGetOutputOauthAutoRegistration:
    status: str
@dataclass
class DashboardInstanceProvidersGetOutputOauth:
    status: str
    callback_url: Optional[str] = None
    auto_registration: Optional[DashboardInstanceProvidersGetOutputOauthAutoRegistration] = None
@dataclass
class DashboardInstanceProvidersGetOutput:
    object: str
    id: str
    access: str
    status: str
    publisher: DashboardInstanceProvidersGetOutputPublisher
    entry: DashboardInstanceProvidersGetOutputEntry
    type: DashboardInstanceProvidersGetOutputType
    identifier: str
    tag: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    owner_tenant: Optional[DashboardInstanceProvidersGetOutputOwnerTenant] = None
    default_variant: Optional[DashboardInstanceProvidersGetOutputDefaultVariant] = None
    current_version: Optional[DashboardInstanceProvidersGetOutputCurrentVersion] = None
    oauth: Optional[DashboardInstanceProvidersGetOutputOauth] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapDashboardInstanceProvidersGetOutputOwnerTenant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputOwnerTenant:
        return DashboardInstanceProvidersGetOutputOwnerTenant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        name=data.get('name'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputOwnerTenant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputPublisher:
        return DashboardInstanceProvidersGetOutputPublisher(
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
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputEntry:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputEntry:
        return DashboardInstanceProvidersGetOutputEntry(
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
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputEntry, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputDefaultVariantCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputDefaultVariantCurrentVersion:
        return DashboardInstanceProvidersGetOutputDefaultVariantCurrentVersion(
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
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputDefaultVariantCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputDefaultVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputDefaultVariant:
        return DashboardInstanceProvidersGetOutputDefaultVariant(
        object=data.get('object'),
        id=data.get('id'),
        tag=data.get('tag'),
        identifier=data.get('identifier'),
        provider_id=data.get('provider_id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        current_version=mapDashboardInstanceProvidersGetOutputDefaultVariantCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputDefaultVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputCurrentVersion:
        return DashboardInstanceProvidersGetOutputCurrentVersion(
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
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputType:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputType:
        return DashboardInstanceProvidersGetOutputType(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        config=data.get('config'),
        triggers=data.get('triggers'),
        auth=data.get('auth'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputType, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputOauthAutoRegistration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputOauthAutoRegistration:
        return DashboardInstanceProvidersGetOutputOauthAutoRegistration(
        status=data.get('status')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputOauthAutoRegistration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutputOauth:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutputOauth:
        return DashboardInstanceProvidersGetOutputOauth(
        status=data.get('status'),
        callback_url=data.get('callback_url'),
        auto_registration=mapDashboardInstanceProvidersGetOutputOauthAutoRegistration.from_dict(data.get('auto_registration')) if data.get('auto_registration') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersGetOutputOauth, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersGetOutput:
        return DashboardInstanceProvidersGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        access=data.get('access'),
        status=data.get('status'),
        owner_tenant=mapDashboardInstanceProvidersGetOutputOwnerTenant.from_dict(data.get('owner_tenant')) if data.get('owner_tenant') else None,
        publisher=mapDashboardInstanceProvidersGetOutputPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        entry=mapDashboardInstanceProvidersGetOutputEntry.from_dict(data.get('entry')) if data.get('entry') else None,
        default_variant=mapDashboardInstanceProvidersGetOutputDefaultVariant.from_dict(data.get('default_variant')) if data.get('default_variant') else None,
        current_version=mapDashboardInstanceProvidersGetOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        type=mapDashboardInstanceProvidersGetOutputType.from_dict(data.get('type')) if data.get('type') else None,
        oauth=mapDashboardInstanceProvidersGetOutputOauth.from_dict(data.get('oauth')) if data.get('oauth') else None,
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
    def to_dict(value: Union[DashboardInstanceProvidersGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
