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


SessionsListQuery = Any


class mapSessionsListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsListQuery:
    data

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
