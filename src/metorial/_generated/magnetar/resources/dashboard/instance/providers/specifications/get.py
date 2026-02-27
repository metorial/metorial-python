from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputTools:
    object: str
    id: str
    name: str
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    title: Optional[str] = None
    description: Optional[str] = None
    input_schema: Optional[Dict[str, Any]] = None
    output_schema: Optional[Dict[str, Any]] = None
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
    object: str
    id: str
    scope: str
    name: str
    description: Optional[str] = None
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutputAuthMethods:
    object: str
    id: str
    type: str
    name: str
    provider_id: str
    provider_specification_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    input_schema: Optional[Dict[str, Any]] = None
    scopes: Optional[List[DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes]] = None
@dataclass
class DashboardInstanceProvidersSpecificationsGetOutput:
    object: str
    id: str
    name: str
    tools: List[DashboardInstanceProvidersSpecificationsGetOutputTools]
    auth_methods: List[DashboardInstanceProvidersSpecificationsGetOutputAuthMethods]
    provider_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    config_schema: Optional[Dict[str, Any]] = None


class mapDashboardInstanceProvidersSpecificationsGetOutputTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputTools:
        return DashboardInstanceProvidersSpecificationsGetOutputTools(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        title=data.get('title'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        output_schema=data.get('output_schema'),
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes:
        return DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes(
        object=data.get('object'),
        id=data.get('id'),
        scope=data.get('scope'),
        name=data.get('name'),
        description=data.get('description')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethods:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutputAuthMethods:
        return DashboardInstanceProvidersSpecificationsGetOutputAuthMethods(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        scopes=[mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethodsScopes.from_dict(item) for item in data.get('scopes', []) if item],
        provider_id=data.get('provider_id'),
        provider_specification_id=data.get('provider_specification_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutputAuthMethods, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProvidersSpecificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProvidersSpecificationsGetOutput:
        return DashboardInstanceProvidersSpecificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        config_schema=data.get('config_schema'),
        tools=[mapDashboardInstanceProvidersSpecificationsGetOutputTools.from_dict(item) for item in data.get('tools', []) if item],
        auth_methods=[mapDashboardInstanceProvidersSpecificationsGetOutputAuthMethods.from_dict(item) for item in data.get('auth_methods', []) if item],
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProvidersSpecificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
