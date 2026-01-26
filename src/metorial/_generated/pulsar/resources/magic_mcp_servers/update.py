from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class MagicMcpServersUpdateOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class MagicMcpServersUpdateOutputEndpoints:
  id: str
  alias: str
  urls: MagicMcpServersUpdateOutputEndpointsUrls


@dataclass
class MagicMcpServersUpdateOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class MagicMcpServersUpdateOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: MagicMcpServersUpdateOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class MagicMcpServersUpdateOutput:
  object: str
  id: str
  status: str
  endpoints: List[MagicMcpServersUpdateOutputEndpoints]
  server_deployments: List[MagicMcpServersUpdateOutputServerDeployments]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapMagicMcpServersUpdateOutputEndpointsUrls:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateOutputEndpointsUrls:
    return MagicMcpServersUpdateOutputEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersUpdateOutputEndpointsUrls, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersUpdateOutputEndpoints:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateOutputEndpoints:
    return MagicMcpServersUpdateOutputEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapMagicMcpServersUpdateOutputEndpointsUrls.from_dict(data.get("urls"))
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersUpdateOutputEndpoints, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersUpdateOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> MagicMcpServersUpdateOutputServerDeploymentsServer:
    return MagicMcpServersUpdateOutputServerDeploymentsServer(
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
      MagicMcpServersUpdateOutputServerDeploymentsServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersUpdateOutputServerDeployments:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateOutputServerDeployments:
    return MagicMcpServersUpdateOutputServerDeployments(
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
      server=mapMagicMcpServersUpdateOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersUpdateOutputServerDeployments, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateOutput:
    return MagicMcpServersUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapMagicMcpServersUpdateOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapMagicMcpServersUpdateOutputServerDeployments.from_dict(item)
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
    value: Union[MagicMcpServersUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class MagicMcpServersUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  aliases: Optional[List[str]] = None


class mapMagicMcpServersUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersUpdateBody:
    return MagicMcpServersUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      aliases=data.get("aliases", []),
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
