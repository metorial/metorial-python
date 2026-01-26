from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceMagicMcpServersCreateOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class ManagementInstanceMagicMcpServersCreateOutputEndpoints:
  id: str
  alias: str
  urls: ManagementInstanceMagicMcpServersCreateOutputEndpointsUrls


@dataclass
class ManagementInstanceMagicMcpServersCreateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersCreateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ManagementInstanceMagicMcpServersCreateOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersCreateOutput:
  object: str
  id: str
  status: str
  endpoints: List[ManagementInstanceMagicMcpServersCreateOutputEndpoints]
  server_deployments: List[
    ManagementInstanceMagicMcpServersCreateOutputServerDeployments
  ]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapManagementInstanceMagicMcpServersCreateOutputEndpointsUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersCreateOutputEndpointsUrls:
    return ManagementInstanceMagicMcpServersCreateOutputEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersCreateOutputEndpointsUrls, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersCreateOutputEndpoints:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersCreateOutputEndpoints:
    return ManagementInstanceMagicMcpServersCreateOutputEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapManagementInstanceMagicMcpServersCreateOutputEndpointsUrls.from_dict(
        data.get("urls")
      )
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersCreateOutputEndpoints, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersCreateOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersCreateOutputServerDeploymentsServer:
    return ManagementInstanceMagicMcpServersCreateOutputServerDeploymentsServer(
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
      ManagementInstanceMagicMcpServersCreateOutputServerDeploymentsServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersCreateOutputServerDeployments:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersCreateOutputServerDeployments:
    return ManagementInstanceMagicMcpServersCreateOutputServerDeployments(
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
      server=mapManagementInstanceMagicMcpServersCreateOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersCreateOutputServerDeployments,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersCreateOutput:
    return ManagementInstanceMagicMcpServersCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapManagementInstanceMagicMcpServersCreateOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapManagementInstanceMagicMcpServersCreateOutputServerDeployments.from_dict(
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
    value: Union[ManagementInstanceMagicMcpServersCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceMagicMcpServersCreateBody:
  server_implementation: Optional[Dict[str, Any]] = None
  server_implementation_id: Optional[str] = None
  server_variant_id: Optional[str] = None
  server_id: Optional[str] = None


class mapManagementInstanceMagicMcpServersCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersCreateBody:
    return ManagementInstanceMagicMcpServersCreateBody(
      server_implementation=data.get("server_implementation"),
      server_implementation_id=data.get("server_implementation_id"),
      server_variant_id=data.get("server_variant_id"),
      server_id=data.get("server_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpServersCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
