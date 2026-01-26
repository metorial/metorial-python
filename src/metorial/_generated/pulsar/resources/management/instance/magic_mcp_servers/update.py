from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceMagicMcpServersUpdateOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class ManagementInstanceMagicMcpServersUpdateOutputEndpoints:
  id: str
  alias: str
  urls: ManagementInstanceMagicMcpServersUpdateOutputEndpointsUrls


@dataclass
class ManagementInstanceMagicMcpServersUpdateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersUpdateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ManagementInstanceMagicMcpServersUpdateOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersUpdateOutput:
  object: str
  id: str
  status: str
  endpoints: List[ManagementInstanceMagicMcpServersUpdateOutputEndpoints]
  server_deployments: List[
    ManagementInstanceMagicMcpServersUpdateOutputServerDeployments
  ]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapManagementInstanceMagicMcpServersUpdateOutputEndpointsUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersUpdateOutputEndpointsUrls:
    return ManagementInstanceMagicMcpServersUpdateOutputEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersUpdateOutputEndpointsUrls, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersUpdateOutputEndpoints:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersUpdateOutputEndpoints:
    return ManagementInstanceMagicMcpServersUpdateOutputEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapManagementInstanceMagicMcpServersUpdateOutputEndpointsUrls.from_dict(
        data.get("urls")
      )
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersUpdateOutputEndpoints, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersUpdateOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersUpdateOutputServerDeploymentsServer:
    return ManagementInstanceMagicMcpServersUpdateOutputServerDeploymentsServer(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersUpdateOutputServerDeploymentsServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersUpdateOutputServerDeployments:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersUpdateOutputServerDeployments:
    return ManagementInstanceMagicMcpServersUpdateOutputServerDeployments(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      server=mapManagementInstanceMagicMcpServersUpdateOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersUpdateOutputServerDeployments,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersUpdateOutput:
    return ManagementInstanceMagicMcpServersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapManagementInstanceMagicMcpServersUpdateOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapManagementInstanceMagicMcpServersUpdateOutputServerDeployments.from_dict(
          item
        )
        for item in data.get("server_deployments", [])
        if item
      ],
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpServersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceMagicMcpServersUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  aliases: Optional[List[str]] = None


class mapManagementInstanceMagicMcpServersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersUpdateBody:
    return ManagementInstanceMagicMcpServersUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      aliases=data.get("aliases", []),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpServersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
