from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class MagicMcpServersGetOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class MagicMcpServersGetOutputEndpoints:
  id: str
  alias: str
  urls: MagicMcpServersGetOutputEndpointsUrls


@dataclass
class MagicMcpServersGetOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class MagicMcpServersGetOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: MagicMcpServersGetOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class MagicMcpServersGetOutput:
  object: str
  id: str
  status: str
  endpoints: List[MagicMcpServersGetOutputEndpoints]
  server_deployments: List[MagicMcpServersGetOutputServerDeployments]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapMagicMcpServersGetOutputEndpointsUrls:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputEndpointsUrls:
    return MagicMcpServersGetOutputEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersGetOutputEndpointsUrls, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersGetOutputEndpoints:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputEndpoints:
    return MagicMcpServersGetOutputEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapMagicMcpServersGetOutputEndpointsUrls.from_dict(data.get("urls"))
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersGetOutputEndpoints, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersGetOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> MagicMcpServersGetOutputServerDeploymentsServer:
    return MagicMcpServersGetOutputServerDeploymentsServer(
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
    value: Union[MagicMcpServersGetOutputServerDeploymentsServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersGetOutputServerDeployments:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutputServerDeployments:
    return MagicMcpServersGetOutputServerDeployments(
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
      server=mapMagicMcpServersGetOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersGetOutputServerDeployments, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersGetOutput:
    return MagicMcpServersGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapMagicMcpServersGetOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapMagicMcpServersGetOutputServerDeployments.from_dict(item)
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
    value: Union[MagicMcpServersGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
