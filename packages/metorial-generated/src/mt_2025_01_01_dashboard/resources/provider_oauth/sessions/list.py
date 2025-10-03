from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthSessionsListOutputItemsConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ProviderOauthSessionsListOutputItemsConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ProviderOauthSessionsListOutputItemsConnectionProvider
  config: Dict[str, Any]
  scopes: List[str]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class ProviderOauthSessionsListOutputItems:
  object: str
  id: str
  status: str
  url: str
  connection: ProviderOauthSessionsListOutputItemsConnection
  metadata: Dict[str, Any]
  instance_id: str
  created_at: datetime
  updated_at: datetime
  redirect_uri: Optional[str] = None
  completed_at: Optional[datetime] = None


@dataclass
class ProviderOauthSessionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ProviderOauthSessionsListOutput:
  items: List[ProviderOauthSessionsListOutputItems]
  pagination: ProviderOauthSessionsListOutputPagination


class mapProviderOauthSessionsListOutputItemsConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthSessionsListOutputItemsConnectionProvider:
    return ProviderOauthSessionsListOutputItemsConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthSessionsListOutputItemsConnectionProvider, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthSessionsListOutputItemsConnection:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthSessionsListOutputItemsConnection:
    return ProviderOauthSessionsListOutputItemsConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapProviderOauthSessionsListOutputItemsConnectionProvider.from_dict(
        data.get("provider")
      )
      if data.get("provider")
      else None,
      config=data.get("config"),
      scopes=data.get("scopes", []),
      client_id=data.get("client_id"),
      instance_id=data.get("instance_id"),
      template_id=data.get("template_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthSessionsListOutputItemsConnection, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthSessionsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthSessionsListOutputItems:
    return ProviderOauthSessionsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      url=data.get("url"),
      connection=mapProviderOauthSessionsListOutputItemsConnection.from_dict(
        data.get("connection")
      )
      if data.get("connection")
      else None,
      metadata=data.get("metadata"),
      redirect_uri=data.get("redirect_uri"),
      instance_id=data.get("instance_id"),
      completed_at=datetime.fromisoformat(data.get("completed_at"))
      if data.get("completed_at")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthSessionsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthSessionsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthSessionsListOutputPagination:
    return ProviderOauthSessionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthSessionsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthSessionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthSessionsListOutput:
    return ProviderOauthSessionsListOutput(
      items=[
        mapProviderOauthSessionsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapProviderOauthSessionsListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthSessionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthSessionsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None


class mapProviderOauthSessionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthSessionsListQuery:
    return ProviderOauthSessionsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthSessionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
