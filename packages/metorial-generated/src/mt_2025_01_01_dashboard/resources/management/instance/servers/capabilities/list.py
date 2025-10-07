from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceServersCapabilitiesListOutputMcpServersServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersCapabilitiesListOutputMcpServersServerVariant:
    object: str
    id: str
    identifier: str
    server_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceServersCapabilitiesListOutputMcpServersServerVersion:
    object: str
    id: str
    identifier: str
    server_id: str
    server_variant_id: str
    source: Dict[str, Any]
    created_at: datetime
@dataclass
class ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer:
    object: str
    id: str
    name: str
    type: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeployment:
    object: str
    id: str
    metadata: Dict[str, Any]
    created_at: datetime
    updated_at: datetime
    server: ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer
    name: Optional[str] = None
    description: Optional[str] = None
@dataclass
class ManagementInstanceServersCapabilitiesListOutputMcpServersInfo:
    name: str
    version: Optional[str] = None
@dataclass
class ManagementInstanceServersCapabilitiesListOutputMcpServers:
    object: str
    id: str
    server: ManagementInstanceServersCapabilitiesListOutputMcpServersServer
    server_variant: ManagementInstanceServersCapabilitiesListOutputMcpServersServerVariant
    capabilities: Dict[str, Dict[str, Any]]
    info: ManagementInstanceServersCapabilitiesListOutputMcpServersInfo
    server_version: Optional[ManagementInstanceServersCapabilitiesListOutputMcpServersServerVersion] = None
    server_deployment: Optional[ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeployment] = None
@dataclass
class ManagementInstanceServersCapabilitiesListOutputTools:
    mcp_server_id: str
    name: str
    description: Optional[str] = None
    input_schema: Optional[Any] = None
    output_schema: Optional[Any] = None
    annotations: Optional[Any] = None
@dataclass
class ManagementInstanceServersCapabilitiesListOutputPrompts:
    mcp_server_id: str
    name: str
    description: Optional[str] = None
    arguments: Optional[Any] = None
@dataclass
class ManagementInstanceServersCapabilitiesListOutputResourceTemplates:
    mcp_server_id: str
    uri_template: str
    name: str
    description: Optional[str] = None
    mime_type: Optional[str] = None
@dataclass
class ManagementInstanceServersCapabilitiesListOutput:
    object: str
    mcp_servers: List[ManagementInstanceServersCapabilitiesListOutputMcpServers]
    tools: List[ManagementInstanceServersCapabilitiesListOutputTools]
    prompts: List[ManagementInstanceServersCapabilitiesListOutputPrompts]
    resource_templates: List[ManagementInstanceServersCapabilitiesListOutputResourceTemplates]


class mapManagementInstanceServersCapabilitiesListOutputMcpServersServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputMcpServersServer:
        return ManagementInstanceServersCapabilitiesListOutputMcpServersServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputMcpServersServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputMcpServersServerVariant:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputMcpServersServerVariant:
        return ManagementInstanceServersCapabilitiesListOutputMcpServersServerVariant(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputMcpServersServerVariant, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputMcpServersServerVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputMcpServersServerVersion:
        return ManagementInstanceServersCapabilitiesListOutputMcpServersServerVersion(
        object=data.get('object'),
        id=data.get('id'),
        identifier=data.get('identifier'),
        server_id=data.get('server_id'),
        server_variant_id=data.get('server_variant_id'),
        source=data.get('source'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputMcpServersServerVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer:
        return ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        type=data.get('type'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputMcpServersServerDeployment:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeployment:
        return ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeployment(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None,
        server=mapManagementInstanceServersCapabilitiesListOutputMcpServersServerDeploymentServer.from_dict(data.get('server')) if data.get('server') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputMcpServersServerDeployment, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputMcpServersInfo:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputMcpServersInfo:
        return ManagementInstanceServersCapabilitiesListOutputMcpServersInfo(
        name=data.get('name'),
        version=data.get('version')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputMcpServersInfo, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputMcpServers:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputMcpServers:
        return ManagementInstanceServersCapabilitiesListOutputMcpServers(
        object=data.get('object'),
        id=data.get('id'),
        server=mapManagementInstanceServersCapabilitiesListOutputMcpServersServer.from_dict(data.get('server')) if data.get('server') else None,
        server_variant=mapManagementInstanceServersCapabilitiesListOutputMcpServersServerVariant.from_dict(data.get('server_variant')) if data.get('server_variant') else None,
        server_version=mapManagementInstanceServersCapabilitiesListOutputMcpServersServerVersion.from_dict(data.get('server_version')) if data.get('server_version') else None,
        server_deployment=mapManagementInstanceServersCapabilitiesListOutputMcpServersServerDeployment.from_dict(data.get('server_deployment')) if data.get('server_deployment') else None,
        capabilities=data.get('capabilities'),
        info=mapManagementInstanceServersCapabilitiesListOutputMcpServersInfo.from_dict(data.get('info')) if data.get('info') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputMcpServers, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputTools:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputTools:
        return ManagementInstanceServersCapabilitiesListOutputTools(
        mcp_server_id=data.get('mcp_server_id'),
        name=data.get('name'),
        description=data.get('description'),
        input_schema=data.get('input_schema'),
        output_schema=data.get('output_schema'),
        annotations=data.get('annotations')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputTools, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputPrompts:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputPrompts:
        return ManagementInstanceServersCapabilitiesListOutputPrompts(
        mcp_server_id=data.get('mcp_server_id'),
        name=data.get('name'),
        description=data.get('description'),
        arguments=data.get('arguments')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputPrompts, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutputResourceTemplates:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutputResourceTemplates:
        return ManagementInstanceServersCapabilitiesListOutputResourceTemplates(
        mcp_server_id=data.get('mcp_server_id'),
        uri_template=data.get('uri_template'),
        name=data.get('name'),
        description=data.get('description'),
        mime_type=data.get('mime_type')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutputResourceTemplates, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceServersCapabilitiesListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListOutput:
        return ManagementInstanceServersCapabilitiesListOutput(
        object=data.get('object'),
        mcp_servers=[mapManagementInstanceServersCapabilitiesListOutputMcpServers.from_dict(item) for item in data.get('mcp_servers', []) if item],
        tools=[mapManagementInstanceServersCapabilitiesListOutputTools.from_dict(item) for item in data.get('tools', []) if item],
        prompts=[mapManagementInstanceServersCapabilitiesListOutputPrompts.from_dict(item) for item in data.get('prompts', []) if item],
        resource_templates=[mapManagementInstanceServersCapabilitiesListOutputResourceTemplates.from_dict(item) for item in data.get('resource_templates', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceServersCapabilitiesListQuery:
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


class mapManagementInstanceServersCapabilitiesListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceServersCapabilitiesListQuery:
        return ManagementInstanceServersCapabilitiesListQuery(
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
    def to_dict(value: Union[ManagementInstanceServersCapabilitiesListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

