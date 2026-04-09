from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SessionTemplatesUpdateOutputProvidersDeployment:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class SessionTemplatesUpdateOutputProvidersConfig:
    object: str
    id: str
    is_default: bool
    provider_id: str
    created_at: datetime
    updated_at: datetime
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
@dataclass
class SessionTemplatesUpdateOutputProvidersAuthConfig:
    object: str
    id: str
@dataclass
class SessionTemplatesUpdateOutputProviders:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: SessionTemplatesUpdateOutputProvidersDeployment
    config: SessionTemplatesUpdateOutputProvidersConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[SessionTemplatesUpdateOutputProvidersAuthConfig] = None
@dataclass
class SessionTemplatesUpdateOutput:
    object: str
    id: str
    status: str
    name: str
    providers: List[SessionTemplatesUpdateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapSessionTemplatesUpdateOutputProvidersDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesUpdateOutputProvidersDeployment:
        return SessionTemplatesUpdateOutputProvidersDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesUpdateOutputProvidersDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesUpdateOutputProvidersConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesUpdateOutputProvidersConfig:
        return SessionTemplatesUpdateOutputProvidersConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesUpdateOutputProvidersConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesUpdateOutputProvidersAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesUpdateOutputProvidersAuthConfig:
        return SessionTemplatesUpdateOutputProvidersAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesUpdateOutputProvidersAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesUpdateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesUpdateOutputProviders:
        return SessionTemplatesUpdateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapSessionTemplatesUpdateOutputProvidersDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapSessionTemplatesUpdateOutputProvidersConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapSessionTemplatesUpdateOutputProvidersAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesUpdateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSessionTemplatesUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesUpdateOutput:
        return SessionTemplatesUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        providers=[mapSessionTemplatesUpdateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SessionTemplatesUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class mapSessionTemplatesUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionTemplatesUpdateBody:
        return SessionTemplatesUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[SessionTemplatesUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

