from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceServersCapabilitiesListOutputMcpServersServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServersCapabilitiesListOutputMcpServersServerVariant:
    object: str
    id: str
    identifier: str
    server_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceServersCapabilitiesListOutputMcpServersServerVersion:
    object: str
    id: str
    identifier: str
    server_id: str
    server_variant_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class DashboardInstanceServersCapabilitiesListOutputMcpServersInfo:
    name: str
    version: Optional[str] = None
@dataclass
class DashboardInstanceServersCapabilitiesListOutputMcpServers:
    object: str
    id: str
    server: DashboardInstanceServersCapabilitiesListOutputMcpServersServer
    server_variant: DashboardInstanceServersCapabilitiesListOutputMcpServersServerVariant
    capabilities: Dict[str, Dict[str, Any]]
    info: DashboardInstanceServersCapabilitiesListOutputMcpServersInfo
    server_version: Optional[DashboardInstanceServersCapabilitiesListOutputMcpServersServerVersion] = None
    server_deployment: Optional[DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeployment] = None
@dataclass
class DashboardInstanceServersCapabilitiesListOutputTools:
    mcp_server_id: str
    name: str
    description: Optional[str] = None
    input_schema: Optional[Any] = None
    output_schema: Optional[Any] = None
    annotations: Optional[Any] = None
@dataclass
class DashboardInstanceServersCapabilitiesListOutputPrompts:
    mcp_server_id: str
    name: str
    description: Optional[str] = None
    arguments: Optional[Any] = None
@dataclass
class DashboardInstanceServersCapabilitiesListOutputResourceTemplates:
    mcp_server_id: str
    uri_template: str
    name: str
    description: Optional[str] = None
    mime_type: Optional[str] = None
@dataclass
class DashboardInstanceServersCapabilitiesListOutput:
    object: str
    mcp_servers: List[DashboardInstanceServersCapabilitiesListOutputMcpServers]
    tools: List[DashboardInstanceServersCapabilitiesListOutputTools]
    prompts: List[DashboardInstanceServersCapabilitiesListOutputPrompts]
    resource_templates: List[DashboardInstanceServersCapabilitiesListOutputResourceTemplates]


class mapDashboardInstanceServersCapabilitiesListOutputMcpServersServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputMcpServersServer:
        return DashboardInstanceServersCapabilitiesListOutputMcpServersServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputMcpServersServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputMcpServersServerVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputMcpServersServerVariant:
        return DashboardInstanceServersCapabilitiesListOutputMcpServersServerVariant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputMcpServersServerVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputMcpServersServerVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputMcpServersServerVersion:
        return DashboardInstanceServersCapabilitiesListOutputMcpServersServerVersion(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        server_variant_id=data.get('server_variant_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputMcpServersServerVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer:
        return DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputMcpServersServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeployment:
        return DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapDashboardInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputMcpServersServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputMcpServersInfo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputMcpServersInfo:
        return DashboardInstanceServersCapabilitiesListOutputMcpServersInfo(
        name=data.get('name'),
        version=data.get('version')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputMcpServersInfo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputMcpServers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputMcpServers:
        return DashboardInstanceServersCapabilitiesListOutputMcpServers(
        object=data.get('object'),
        id=data.get('id'),
        server=mapDashboardInstanceServersCapabilitiesListOutputMcpServersServer.from_dict(data.get('server')) if data.get('server') else None,
        server_variant=mapDashboardInstanceServersCapabilitiesListOutputMcpServersServerVariant.from_dict(data.get('server_variant')) if data.get('server_variant') else None,
        server_version=mapDashboardInstanceServersCapabilitiesListOutputMcpServersServerVersion.from_dict(data.get('server_version')) if data.get('server_version') else None,
        server_deployment=mapDashboardInstanceServersCapabilitiesListOutputMcpServersServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        capabilities=data.get('capabilities'),
        info=mapDashboardInstanceServersCapabilitiesListOutputMcpServersInfo.from_dict(data.get('info')) if data.get('info') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputMcpServers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputTools:
        return DashboardInstanceServersCapabilitiesListOutputTools(
        mcp_server_id=data.get('mcp_server_id'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        output_schema=data.get('output_schema'),
        annotations=data.get('annotations')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputPrompts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputPrompts:
        return DashboardInstanceServersCapabilitiesListOutputPrompts(
        mcp_server_id=data.get('mcp_server_id'),
        name=data.get('name'),
        description=data.get('description'),
        arguments=data.get('arguments')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputPrompts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutputResourceTemplates:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutputResourceTemplates:
        return DashboardInstanceServersCapabilitiesListOutputResourceTemplates(
        mcp_server_id=data.get('mcp_server_id'),
        uri_template=data.get('uri_template'),
        name=data.get('name'),
        description=data.get('description'),
        mime_type=data.get('mime_type')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutputResourceTemplates, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceServersCapabilitiesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListOutput:
        return DashboardInstanceServersCapabilitiesListOutput(
        object=data.get('object'),
        mcp_servers=[mapDashboardInstanceServersCapabilitiesListOutputMcpServers.from_dict(item) for item in data.get('mcp_servers', []) if item],
        tools=[mapDashboardInstanceServersCapabilitiesListOutputTools.from_dict(item) for item in data.get('tools', []) if item],
        prompts=[mapDashboardInstanceServersCapabilitiesListOutputPrompts.from_dict(item) for item in data.get('prompts', []) if item],
        resource_templates=[mapDashboardInstanceServersCapabilitiesListOutputResourceTemplates.from_dict(item) for item in data.get('resource_templates', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceServersCapabilitiesListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    server_deployment_id: Optional[Union[str, List[str]]] = None
    server_variant_id: Optional[Union[str, List[str]]] = None
    server_id: Optional[Union[str, List[str]]] = None
    server_version_id: Optional[Union[str, List[str]]] = None
    server_implementation_id: Optional[Union[str, List[str]]] = None


class mapDashboardInstanceServersCapabilitiesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceServersCapabilitiesListQuery:
        return DashboardInstanceServersCapabilitiesListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        server_deployment_id=data.get('server_deployment_id'),
        server_variant_id=data.get('server_variant_id'),
        server_id=data.get('server_id'),
        server_version_id=data.get('server_version_id'),
        server_implementation_id=data.get('server_implementation_id')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceServersCapabilitiesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

