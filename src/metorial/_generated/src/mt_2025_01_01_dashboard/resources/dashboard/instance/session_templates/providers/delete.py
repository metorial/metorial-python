from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSessionTemplatesProvidersDeleteOutputDeployment:
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
class DashboardInstanceSessionTemplatesProvidersDeleteOutputConfig:
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
class DashboardInstanceSessionTemplatesProvidersDeleteOutputAuthConfig:
    object: str
    id: str
@dataclass
class DashboardInstanceSessionTemplatesProvidersDeleteOutput:
    object: str
    id: str
    status: str
    tool_filter: Dict[str, Any]
    provider_id: str
    session_template_id: str
    deployment: DashboardInstanceSessionTemplatesProvidersDeleteOutputDeployment
    config: DashboardInstanceSessionTemplatesProvidersDeleteOutputConfig
    created_at: datetime
    updated_at: datetime
    auth_config: Optional[DashboardInstanceSessionTemplatesProvidersDeleteOutputAuthConfig] = None


class mapDashboardInstanceSessionTemplatesProvidersDeleteOutputDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionTemplatesProvidersDeleteOutputDeployment:
        return DashboardInstanceSessionTemplatesProvidersDeleteOutputDeployment(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionTemplatesProvidersDeleteOutputDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionTemplatesProvidersDeleteOutputConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionTemplatesProvidersDeleteOutputConfig:
        return DashboardInstanceSessionTemplatesProvidersDeleteOutputConfig(
        object=data.get('object'),
        id=data.get('id'),
        is_default=data.get('is_default'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionTemplatesProvidersDeleteOutputConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionTemplatesProvidersDeleteOutputAuthConfig:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionTemplatesProvidersDeleteOutputAuthConfig:
        return DashboardInstanceSessionTemplatesProvidersDeleteOutputAuthConfig(
        object=data.get('object'),
        id=data.get('id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionTemplatesProvidersDeleteOutputAuthConfig, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSessionTemplatesProvidersDeleteOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSessionTemplatesProvidersDeleteOutput:
        return DashboardInstanceSessionTemplatesProvidersDeleteOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        tool_filter=data.get('tool_filter'),
        provider_id=data.get('provider_id'),
        session_template_id=data.get('session_template_id'),
        deployment=mapDashboardInstanceSessionTemplatesProvidersDeleteOutputDeployment.from_dict(data.get('deployment')) if data.get('deployment') else None,
        config=mapDashboardInstanceSessionTemplatesProvidersDeleteOutputConfig.from_dict(data.get('config')) if data.get('config') else None,
        auth_config=mapDashboardInstanceSessionTemplatesProvidersDeleteOutputAuthConfig.from_dict(data.get('auth_config')) if data.get('auth_config') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSessionTemplatesProvidersDeleteOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
