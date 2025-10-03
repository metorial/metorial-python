from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class SessionsListOutput:
  items: List[Dict[str, Any]]
  pagination: SessionsListOutputPagination


class mapSessionsListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutputPagination:
    return SessionsListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListOutput:
    return SessionsListOutput(
      items=data.get("items", []),
      pagination=mapSessionsListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class SessionsListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  status: Optional[Union[str, List[str]]] = None
  server_id: Optional[Union[str, List[str]]] = None
  server_variant_id: Optional[Union[str, List[str]]] = None
  server_implementation_id: Optional[Union[str, List[str]]] = None
  server_deployment_id: Optional[Union[str, List[str]]] = None


class mapSessionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListQuery:
    return SessionsListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      status=data.get("status"),
      server_id=data.get("server_id"),
      server_variant_id=data.get("server_variant_id"),
      server_implementation_id=data.get("server_implementation_id"),
      server_deployment_id=data.get("server_deployment_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
