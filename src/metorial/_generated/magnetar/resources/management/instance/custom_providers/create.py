from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceCustomProvidersCreateOutputProviderPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceCustomProvidersCreateOutputProviderCurrentVersion:
    object: str
    id: str
    version: str
    status: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceCustomProvidersCreateOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    publisher: Optional[ManagementInstanceCustomProvidersCreateOutputProviderPublisher] = None
    current_version: Optional[ManagementInstanceCustomProvidersCreateOutputProviderCurrentVersion] = None
@dataclass
class ManagementInstanceCustomProvidersCreateOutput:
    object: str
    id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider: Optional[ManagementInstanceCustomProvidersCreateOutputProvider] = None


class mapManagementInstanceCustomProvidersCreateOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCreateOutputProviderPublisher:
        return ManagementInstanceCustomProvidersCreateOutputProviderPublisher(
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
    def to_dict(value: Union[ManagementInstanceCustomProvidersCreateOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCreateOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCreateOutputProviderCurrentVersion:
        return ManagementInstanceCustomProvidersCreateOutputProviderCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCreateOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCreateOutputProvider:
        return ManagementInstanceCustomProvidersCreateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        publisher=mapManagementInstanceCustomProvidersCreateOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapManagementInstanceCustomProvidersCreateOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCreateOutput:
        return ManagementInstanceCustomProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider=mapManagementInstanceCustomProvidersCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceCustomProvidersCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class ManagementInstanceCustomProvidersCreateBody:
    name: str
    from_: Dict[str, Any]
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[ManagementInstanceCustomProvidersCreateBodyConfig] = None


class mapManagementInstanceCustomProvidersCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCreateBodyConfig:
        return ManagementInstanceCustomProvidersCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceCustomProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceCustomProvidersCreateBody:
        return ManagementInstanceCustomProvidersCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        from_=data.get('from'),
        config=mapManagementInstanceCustomProvidersCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceCustomProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
