from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class MagicMcpServersDeleteOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class MagicMcpServersDeleteOutputEndpoints:
  id: str
  alias: str
  urls: MagicMcpServersDeleteOutputEndpointsUrls


@dataclass
class MagicMcpServersDeleteOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class MagicMcpServersDeleteOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: MagicMcpServersDeleteOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class MagicMcpServersDeleteOutput:
  object: str
  id: str
  status: str
  endpoints: List[MagicMcpServersDeleteOutputEndpoints]
  server_deployments: List[MagicMcpServersDeleteOutputServerDeployments]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapMagicMcpServersDeleteOutputEndpointsUrls:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersDeleteOutputEndpointsUrls:
    return MagicMcpServersDeleteOutputEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersDeleteOutputEndpointsUrls, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersDeleteOutputEndpoints:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersDeleteOutputEndpoints:
    return MagicMcpServersDeleteOutputEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapMagicMcpServersDeleteOutputEndpointsUrls.from_dict(data.get("urls"))
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersDeleteOutputEndpoints, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersDeleteOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> MagicMcpServersDeleteOutputServerDeploymentsServer:
    return MagicMcpServersDeleteOutputServerDeploymentsServer(
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
      MagicMcpServersDeleteOutputServerDeploymentsServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersDeleteOutputServerDeployments:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersDeleteOutputServerDeployments:
    return MagicMcpServersDeleteOutputServerDeployments(
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
      server=mapMagicMcpServersDeleteOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersDeleteOutputServerDeployments, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersDeleteOutput:
    return MagicMcpServersDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapMagicMcpServersDeleteOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapMagicMcpServersDeleteOutputServerDeployments.from_dict(item)
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
    value: Union[MagicMcpServersDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
