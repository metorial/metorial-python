from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersCapabilitiesListOutputMcpServersServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersCapabilitiesListOutputMcpServersServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersCapabilitiesListOutputMcpServersServerVersion:
  object: str
  id: str
  identifier: str
  server_id: str
  server_variant_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersCapabilitiesListOutputMcpServersServerDeploymentServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersCapabilitiesListOutputMcpServersServerDeployment:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ServersCapabilitiesListOutputMcpServersServerDeploymentServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ServersCapabilitiesListOutputMcpServersInfo:
  name: str
  version: Optional[str] = None


@dataclass
class ServersCapabilitiesListOutputMcpServers:
  object: str
  id: str
  server: ServersCapabilitiesListOutputMcpServersServer
  server_variant: ServersCapabilitiesListOutputMcpServersServerVariant
  capabilities: Dict[str, Dict[str, Any]]
  info: ServersCapabilitiesListOutputMcpServersInfo
  server_version: Optional[ServersCapabilitiesListOutputMcpServersServerVersion] = None
  server_deployment: Optional[
    ServersCapabilitiesListOutputMcpServersServerDeployment
  ] = None


@dataclass
class ServersCapabilitiesListOutputTools:
  mcp_server_id: str
  name: str
  description: Optional[str] = None
  input_schema: Optional[Any] = None
  output_schema: Optional[Any] = None
  annotations: Optional[Any] = None


@dataclass
class ServersCapabilitiesListOutputPrompts:
  mcp_server_id: str
  name: str
  description: Optional[str] = None
  arguments: Optional[Any] = None


@dataclass
class ServersCapabilitiesListOutputResourceTemplates:
  mcp_server_id: str
  uri_template: str
  name: str
  description: Optional[str] = None
  mime_type: Optional[str] = None


@dataclass
class ServersCapabilitiesListOutput:
  object: str
  mcp_servers: List[ServersCapabilitiesListOutputMcpServers]
  tools: List[ServersCapabilitiesListOutputTools]
  prompts: List[ServersCapabilitiesListOutputPrompts]
  resource_templates: List[ServersCapabilitiesListOutputResourceTemplates]


class mapServersCapabilitiesListOutputMcpServersServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersCapabilitiesListOutputMcpServersServer:
    return ServersCapabilitiesListOutputMcpServersServer(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersCapabilitiesListOutputMcpServersServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputMcpServersServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersCapabilitiesListOutputMcpServersServerVariant:
    return ServersCapabilitiesListOutputMcpServersServerVariant(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      source=data.get("source"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersCapabilitiesListOutputMcpServersServerVariant, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputMcpServersServerVersion:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersCapabilitiesListOutputMcpServersServerVersion:
    return ServersCapabilitiesListOutputMcpServersServerVersion(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      source=data.get("source"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersCapabilitiesListOutputMcpServersServerVersion, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputMcpServersServerDeploymentServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersCapabilitiesListOutputMcpServersServerDeploymentServer:
    return ServersCapabilitiesListOutputMcpServersServerDeploymentServer(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersCapabilitiesListOutputMcpServersServerDeploymentServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputMcpServersServerDeployment:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersCapabilitiesListOutputMcpServersServerDeployment:
    return ServersCapabilitiesListOutputMcpServersServerDeployment(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      server=mapServersCapabilitiesListOutputMcpServersServerDeploymentServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ServersCapabilitiesListOutputMcpServersServerDeployment, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputMcpServersInfo:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersCapabilitiesListOutputMcpServersInfo:
    return ServersCapabilitiesListOutputMcpServersInfo(
      name=data.get("name"), version=data.get("version")
    )

  @staticmethod
  def to_dict(
    value: Union[ServersCapabilitiesListOutputMcpServersInfo, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputMcpServers:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersCapabilitiesListOutputMcpServers:
    return ServersCapabilitiesListOutputMcpServers(
      object=data.get("object"),
      id=data.get("id"),
      server=mapServersCapabilitiesListOutputMcpServersServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
      server_variant=mapServersCapabilitiesListOutputMcpServersServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server_version=mapServersCapabilitiesListOutputMcpServersServerVersion.from_dict(
        data.get("server_version")
      )
      if data.get("server_version")
      else None,
      server_deployment=mapServersCapabilitiesListOutputMcpServersServerDeployment.from_dict(
        data.get("server_deployment")
      )
      if data.get("server_deployment")
      else None,
      capabilities=data.get("capabilities"),
      info=mapServersCapabilitiesListOutputMcpServersInfo.from_dict(data.get("info"))
      if data.get("info")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersCapabilitiesListOutputMcpServers, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputTools:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersCapabilitiesListOutputTools:
    return ServersCapabilitiesListOutputTools(
      mcp_server_id=data.get("mcp_server_id"),
      name=data.get("name"),
      description=data.get("description"),
      input_schema=data.get("input_schema"),
      output_schema=data.get("output_schema"),
      annotations=data.get("annotations"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersCapabilitiesListOutputTools, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputPrompts:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersCapabilitiesListOutputPrompts:
    return ServersCapabilitiesListOutputPrompts(
      mcp_server_id=data.get("mcp_server_id"),
      name=data.get("name"),
      description=data.get("description"),
      arguments=data.get("arguments"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersCapabilitiesListOutputPrompts, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutputResourceTemplates:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersCapabilitiesListOutputResourceTemplates:
    return ServersCapabilitiesListOutputResourceTemplates(
      mcp_server_id=data.get("mcp_server_id"),
      uri_template=data.get("uri_template"),
      name=data.get("name"),
      description=data.get("description"),
      mime_type=data.get("mime_type"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersCapabilitiesListOutputResourceTemplates, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersCapabilitiesListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersCapabilitiesListOutput:
    return ServersCapabilitiesListOutput(
      object=data.get("object"),
      mcp_servers=[
        mapServersCapabilitiesListOutputMcpServers.from_dict(item)
        for item in data.get("mcp_servers", [])
        if item
      ],
      tools=[
        mapServersCapabilitiesListOutputTools.from_dict(item)
        for item in data.get("tools", [])
        if item
      ],
      prompts=[
        mapServersCapabilitiesListOutputPrompts.from_dict(item)
        for item in data.get("prompts", [])
        if item
      ],
      resource_templates=[
        mapServersCapabilitiesListOutputResourceTemplates.from_dict(item)
        for item in data.get("resource_templates", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[ServersCapabilitiesListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServersCapabilitiesListQuery:
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


class mapServersCapabilitiesListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersCapabilitiesListQuery:
    return ServersCapabilitiesListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      server_deployment_id=data.get("server_deployment_id"),
      server_variant_id=data.get("server_variant_id"),
      server_id=data.get("server_id"),
      server_version_id=data.get("server_version_id"),
      server_implementation_id=data.get("server_implementation_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersCapabilitiesListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
