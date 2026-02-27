from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion:
    object: str
    id: str
    version: str
    status: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceCustomProvidersCreateOutputProvider:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    publisher: Optional[DashboardInstanceCustomProvidersCreateOutputProviderPublisher] = None
    current_version: Optional[DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion] = None
@dataclass
class DashboardInstanceCustomProvidersCreateOutput:
    object: str
    id: str
    created_at: datetime
    updated_at: datetime
    status: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    provider: Optional[DashboardInstanceCustomProvidersCreateOutputProvider] = None


class mapDashboardInstanceCustomProvidersCreateOutputProviderPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderPublisher:
        return DashboardInstanceCustomProvidersCreateOutputProviderPublisher(
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
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion:
        return DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutputProvider:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutputProvider:
        return DashboardInstanceCustomProvidersCreateOutputProvider(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        publisher=mapDashboardInstanceCustomProvidersCreateOutputProviderPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapDashboardInstanceCustomProvidersCreateOutputProviderCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutputProvider, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateOutput:
        return DashboardInstanceCustomProvidersCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider=mapDashboardInstanceCustomProvidersCreateOutputProvider.from_dict(data.get('provider')) if data.get('provider') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceCustomProvidersCreateBodyConfig:
    schema: Dict[str, Any]
    transformer: str
@dataclass
class DashboardInstanceCustomProvidersCreateBody:
    name: str
    from_: Dict[str, Any]
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    config: Optional[DashboardInstanceCustomProvidersCreateBodyConfig] = None


class mapDashboardInstanceCustomProvidersCreateBodyConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateBodyConfig:
        return DashboardInstanceCustomProvidersCreateBodyConfig(
        schema=data.get('schema'),
        transformer=data.get('transformer')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateBodyConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceCustomProvidersCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersCreateBody:
        return DashboardInstanceCustomProvidersCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        from_=data.get('from'),
        config=mapDashboardInstanceCustomProvidersCreateBodyConfig.from_dict(data.get('config')) if data.get('config') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
