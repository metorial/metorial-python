from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SecretsListOutputItemsType:
  identifier: str
  name: str


@dataclass
class SecretsListOutputItems:
  object: str
  id: str
  status: str
  type: SecretsListOutputItemsType
  description: str
  metadata: Dict[str, Any]
  organization_id: str
  instance_id: str
  fingerprint: str
  created_at: datetime
  last_used_at: Optional[datetime] = None


@dataclass
class SecretsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class SecretsListOutput:
  items: List[SecretsListOutputItems]
  pagination: SecretsListOutputPagination


class mapSecretsListOutputItemsType:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SecretsListOutputItemsType:
    return SecretsListOutputItemsType(
      identifier=data.get("identifier"), name=data.get("name")
    )

  @staticmethod
  def to_dict(
    value: Union[SecretsListOutputItemsType, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSecretsListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SecretsListOutputItems:
    return SecretsListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=mapSecretsListOutputItemsType.from_dict(data.get("type"))
      if data.get("type")
      else None,
      description=data.get("description"),
      metadata=data.get("metadata"),
      organization_id=data.get("organization_id"),
      instance_id=data.get("instance_id"),
      fingerprint=data.get("fingerprint"),
      last_used_at=datetime.fromisoformat(data.get("last_used_at"))
      if data.get("last_used_at")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SecretsListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSecretsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SecretsListOutputPagination:
    return SecretsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[SecretsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSecretsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SecretsListOutput:
    return SecretsListOutput(
      items=[
        mapSecretsListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapSecretsListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SecretsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class SecretsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  type: Optional[Union[str, List[str]]] = None
  status: Optional[Union[str, List[str]]] = None


class mapSecretsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SecretsListQuery:
    return SecretsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      type=data.get("type"),
      status=data.get("status"),
    )

  @staticmethod
  def to_dict(
    value: Union[SecretsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
