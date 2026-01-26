from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class MagicMcpServersListOutputItemsEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class MagicMcpServersListOutputItemsEndpoints:
  id: str
  alias: str
  urls: MagicMcpServersListOutputItemsEndpointsUrls


@dataclass
class MagicMcpServersListOutputItemsServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class MagicMcpServersListOutputItemsServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: MagicMcpServersListOutputItemsServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class MagicMcpServersListOutputItems:
  object: str
  id: str
  status: str
  endpoints: List[MagicMcpServersListOutputItemsEndpoints]
  server_deployments: List[MagicMcpServersListOutputItemsServerDeployments]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class MagicMcpServersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class MagicMcpServersListOutput:
  items: List[MagicMcpServersListOutputItems]
  pagination: MagicMcpServersListOutputPagination


class mapMagicMcpServersListOutputItemsEndpointsUrls:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutputItemsEndpointsUrls:
    return MagicMcpServersListOutputItemsEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersListOutputItemsEndpointsUrls, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersListOutputItemsEndpoints:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutputItemsEndpoints:
    return MagicMcpServersListOutputItemsEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapMagicMcpServersListOutputItemsEndpointsUrls.from_dict(data.get("urls"))
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersListOutputItemsEndpoints, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersListOutputItemsServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> MagicMcpServersListOutputItemsServerDeploymentsServer:
    return MagicMcpServersListOutputItemsServerDeploymentsServer(
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
      MagicMcpServersListOutputItemsServerDeploymentsServer, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersListOutputItemsServerDeployments:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> MagicMcpServersListOutputItemsServerDeployments:
    return MagicMcpServersListOutputItemsServerDeployments(
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
      server=mapMagicMcpServersListOutputItemsServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersListOutputItemsServerDeployments, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutputItems:
    return MagicMcpServersListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapMagicMcpServersListOutputItemsEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapMagicMcpServersListOutputItemsServerDeployments.from_dict(item)
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
    value: Union[MagicMcpServersListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutputPagination:
    return MagicMcpServersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapMagicMcpServersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersListOutput:
    return MagicMcpServersListOutput(
      items=[
        mapMagicMcpServersListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapMagicMcpServersListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class MagicMcpServersListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  status: Optional[Union[str, List[str]]] = None
  server_id: Optional[Union[str, List[str]]] = None
  server_variant_id: Optional[Union[str, List[str]]] = None
  server_implementation_id: Optional[Union[str, List[str]]] = None
  session_id: Optional[Union[str, List[str]]] = None
  search: Optional[str] = None


class mapMagicMcpServersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> MagicMcpServersListQuery:
    return MagicMcpServersListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      status=data.get("status"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      server_implementation_id=data.get("server_implementation_id"),
      session_id=data.get("session_id"),
      search=data.get("search"),
    )

  @staticmethod
  def to_dict(
    value: Union[MagicMcpServersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
