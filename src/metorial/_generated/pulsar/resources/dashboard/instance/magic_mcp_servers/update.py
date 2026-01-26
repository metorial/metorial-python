from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputEndpoints:
  id: str
  alias: str
  urls: DashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: DashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpServersUpdateOutput:
  object: str
  id: str
  status: str
  endpoints: List[DashboardInstanceMagicMcpServersUpdateOutputEndpoints]
  server_deployments: List[
    DashboardInstanceMagicMcpServersUpdateOutputServerDeployments
  ]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapDashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls:
    return DashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersUpdateOutputEndpoints:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersUpdateOutputEndpoints:
    return DashboardInstanceMagicMcpServersUpdateOutputEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapDashboardInstanceMagicMcpServersUpdateOutputEndpointsUrls.from_dict(
        data.get("urls")
      )
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpServersUpdateOutputEndpoints, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer:
    return DashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer(
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
      DashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersUpdateOutputServerDeployments:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersUpdateOutputServerDeployments:
    return DashboardInstanceMagicMcpServersUpdateOutputServerDeployments(
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
      server=mapDashboardInstanceMagicMcpServersUpdateOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpServersUpdateOutputServerDeployments,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersUpdateOutput:
    return DashboardInstanceMagicMcpServersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapDashboardInstanceMagicMcpServersUpdateOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapDashboardInstanceMagicMcpServersUpdateOutputServerDeployments.from_dict(item)
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
    value: Union[DashboardInstanceMagicMcpServersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceMagicMcpServersUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  aliases: Optional[List[str]] = None


class mapDashboardInstanceMagicMcpServersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersUpdateBody:
    return DashboardInstanceMagicMcpServersUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      aliases=data.get("aliases", []),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpServersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
