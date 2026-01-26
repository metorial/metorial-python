from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceMagicMcpServersListOutputItemsEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class ManagementInstanceMagicMcpServersListOutputItemsEndpoints:
  id: str
  alias: str
  urls: ManagementInstanceMagicMcpServersListOutputItemsEndpointsUrls


@dataclass
class ManagementInstanceMagicMcpServersListOutputItemsServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersListOutputItemsServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ManagementInstanceMagicMcpServersListOutputItemsServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersListOutputItems:
  object: str
  id: str
  status: str
  endpoints: List[ManagementInstanceMagicMcpServersListOutputItemsEndpoints]
  server_deployments: List[
    ManagementInstanceMagicMcpServersListOutputItemsServerDeployments
  ]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ManagementInstanceMagicMcpServersListOutput:
  items: List[ManagementInstanceMagicMcpServersListOutputItems]
  pagination: ManagementInstanceMagicMcpServersListOutputPagination


class mapManagementInstanceMagicMcpServersListOutputItemsEndpointsUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersListOutputItemsEndpointsUrls:
    return ManagementInstanceMagicMcpServersListOutputItemsEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersListOutputItemsEndpointsUrls,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersListOutputItemsEndpoints:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersListOutputItemsEndpoints:
    return ManagementInstanceMagicMcpServersListOutputItemsEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapManagementInstanceMagicMcpServersListOutputItemsEndpointsUrls.from_dict(
        data.get("urls")
      )
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersListOutputItemsEndpoints, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersListOutputItemsServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersListOutputItemsServerDeploymentsServer:
    return ManagementInstanceMagicMcpServersListOutputItemsServerDeploymentsServer(
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
      ManagementInstanceMagicMcpServersListOutputItemsServerDeploymentsServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersListOutputItemsServerDeployments:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersListOutputItemsServerDeployments:
    return ManagementInstanceMagicMcpServersListOutputItemsServerDeployments(
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
      server=mapManagementInstanceMagicMcpServersListOutputItemsServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersListOutputItemsServerDeployments,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersListOutputItems:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersListOutputItems:
    return ManagementInstanceMagicMcpServersListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapManagementInstanceMagicMcpServersListOutputItemsEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapManagementInstanceMagicMcpServersListOutputItemsServerDeployments.from_dict(
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
    value: Union[ManagementInstanceMagicMcpServersListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersListOutputPagination:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersListOutputPagination:
    return ManagementInstanceMagicMcpServersListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersListOutputPagination, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersListOutput:
    return ManagementInstanceMagicMcpServersListOutput(
      items=[
        mapManagementInstanceMagicMcpServersListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapManagementInstanceMagicMcpServersListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpServersListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ManagementInstanceMagicMcpServersListQuery:
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


class mapManagementInstanceMagicMcpServersListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersListQuery:
    return ManagementInstanceMagicMcpServersListQuery(
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
    value: Union[ManagementInstanceMagicMcpServersListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
