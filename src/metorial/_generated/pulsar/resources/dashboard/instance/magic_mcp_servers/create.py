from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceMagicMcpServersCreateOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class DashboardInstanceMagicMcpServersCreateOutputEndpoints:
  id: str
  alias: str
  urls: DashboardInstanceMagicMcpServersCreateOutputEndpointsUrls


@dataclass
class DashboardInstanceMagicMcpServersCreateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpServersCreateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: DashboardInstanceMagicMcpServersCreateOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class DashboardInstanceMagicMcpServersCreateOutput:
  object: str
  id: str
  status: str
  endpoints: List[DashboardInstanceMagicMcpServersCreateOutputEndpoints]
  server_deployments: List[
    DashboardInstanceMagicMcpServersCreateOutputServerDeployments
  ]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapDashboardInstanceMagicMcpServersCreateOutputEndpointsUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersCreateOutputEndpointsUrls:
    return DashboardInstanceMagicMcpServersCreateOutputEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpServersCreateOutputEndpointsUrls, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersCreateOutputEndpoints:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersCreateOutputEndpoints:
    return DashboardInstanceMagicMcpServersCreateOutputEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapDashboardInstanceMagicMcpServersCreateOutputEndpointsUrls.from_dict(
        data.get("urls")
      )
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpServersCreateOutputEndpoints, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersCreateOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersCreateOutputServerDeploymentsServer:
    return DashboardInstanceMagicMcpServersCreateOutputServerDeploymentsServer(
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
      DashboardInstanceMagicMcpServersCreateOutputServerDeploymentsServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersCreateOutputServerDeployments:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceMagicMcpServersCreateOutputServerDeployments:
    return DashboardInstanceMagicMcpServersCreateOutputServerDeployments(
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
      server=mapDashboardInstanceMagicMcpServersCreateOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceMagicMcpServersCreateOutputServerDeployments,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceMagicMcpServersCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersCreateOutput:
    return DashboardInstanceMagicMcpServersCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapDashboardInstanceMagicMcpServersCreateOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapDashboardInstanceMagicMcpServersCreateOutputServerDeployments.from_dict(item)
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
    value: Union[DashboardInstanceMagicMcpServersCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardInstanceMagicMcpServersCreateBody:
  server_implementation: Optional[Dict[str, Any]] = None
  server_implementation_id: Optional[str] = None
  server_variant_id: Optional[str] = None
  server_id: Optional[str] = None


class mapDashboardInstanceMagicMcpServersCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceMagicMcpServersCreateBody:
    return DashboardInstanceMagicMcpServersCreateBody(
      server_implementation=data.get("server_implementation"),
      server_implementation_id=data.get("server_implementation_id"),
      server_variant_id=data.get("server_variant_id"),
      server_id=data.get("server_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceMagicMcpServersCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
