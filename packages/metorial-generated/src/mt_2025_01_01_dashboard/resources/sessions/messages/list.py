from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SessionsMessagesListOutputItemsSender:
  object: str
  type: str
  id: str


@dataclass
class SessionsMessagesListOutputItemsMcpMessage:
  object: str
  id: str
  method: str
  payload: Dict[str, Any]
  original_id: Optional[str] = None


@dataclass
class SessionsMessagesListOutputItems:
  object: str
  id: str
  type: str
  sender: SessionsMessagesListOutputItemsSender
  mcp_message: SessionsMessagesListOutputItemsMcpMessage
  session_id: str
  server_session_id: str
  created_at: datetime


@dataclass
class SessionsMessagesListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class SessionsMessagesListOutput:
  items: List[SessionsMessagesListOutputItems]
  pagination: SessionsMessagesListOutputPagination


class mapSessionsMessagesListOutputItemsSender:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsSender:
    return SessionsMessagesListOutputItemsSender(
      object=data.get("object"), type=data.get("type"), id=data.get("id")
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsMessagesListOutputItemsSender, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsMessagesListOutputItemsMcpMessage:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItemsMcpMessage:
    return SessionsMessagesListOutputItemsMcpMessage(
      object=data.get("object"),
      id=data.get("id"),
      original_id=data.get("original_id"),
      method=data.get("method"),
      payload=data.get("payload"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsMessagesListOutputItemsMcpMessage, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsMessagesListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputItems:
    return SessionsMessagesListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      sender=mapSessionsMessagesListOutputItemsSender.from_dict(data.get("sender"))
      if data.get("sender")
      else None,
      mcp_message=mapSessionsMessagesListOutputItemsMcpMessage.from_dict(
        data.get("mcp_message")
      )
      if data.get("mcp_message")
      else None,
      session_id=data.get("session_id"),
      server_session_id=data.get("server_session_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsMessagesListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsMessagesListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutputPagination:
    return SessionsMessagesListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsMessagesListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSessionsMessagesListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsMessagesListOutput:
    return SessionsMessagesListOutput(
      items=[
        mapSessionsMessagesListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapSessionsMessagesListOutputPagination.from_dict(
        data.get("pagination")
      )
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsMessagesListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class SessionsMessagesListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  server_run_id: Optional[Union[str, List[str]]] = None
  server_session_id: Optional[Union[str, List[str]]] = None


class mapSessionsMessagesListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SessionsMessagesListQuery:
    return SessionsMessagesListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      server_run_id=data.get("server_run_id"),
      server_session_id=data.get("server_session_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[SessionsMessagesListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
