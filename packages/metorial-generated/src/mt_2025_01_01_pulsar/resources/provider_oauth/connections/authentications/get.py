from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionsAuthenticationsGetOutputError:
  code: str
  message: Optional[str] = None


@dataclass
class ProviderOauthConnectionsAuthenticationsGetOutputEvents:
  id: str
  type: str
  metadata: Dict[str, Any]
  created_at: datetime


@dataclass
class ProviderOauthConnectionsAuthenticationsGetOutputProfile:
  object: str
  id: str
  status: str
  sub: str
  connection_id: str
  created_at: datetime
  last_used_at: datetime
  updated_at: datetime
  name: Optional[str] = None
  email: Optional[str] = None


@dataclass
class ProviderOauthConnectionsAuthenticationsGetOutput:
  object: str
  id: str
  status: str
  events: List[ProviderOauthConnectionsAuthenticationsGetOutputEvents]
  connection_id: str
  created_at: datetime
  error: Optional[ProviderOauthConnectionsAuthenticationsGetOutputError] = None
  profile: Optional[ProviderOauthConnectionsAuthenticationsGetOutputProfile] = None


class mapProviderOauthConnectionsAuthenticationsGetOutputError:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsGetOutputError:
    return ProviderOauthConnectionsAuthenticationsGetOutputError(
      code=data.get("code"), message=data.get("message")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsAuthenticationsGetOutputError, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsAuthenticationsGetOutputEvents:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsGetOutputEvents:
    return ProviderOauthConnectionsAuthenticationsGetOutputEvents(
      id=data.get("id"),
      type=data.get("type"),
      metadata=data.get("metadata"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsAuthenticationsGetOutputEvents, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsAuthenticationsGetOutputProfile:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsGetOutputProfile:
    return ProviderOauthConnectionsAuthenticationsGetOutputProfile(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      sub=data.get("sub"),
      name=data.get("name"),
      email=data.get("email"),
      connection_id=data.get("connection_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      last_used_at=datetime.fromisoformat(data.get("last_used_at"))
      if data.get("last_used_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthConnectionsAuthenticationsGetOutputProfile, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsAuthenticationsGetOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthConnectionsAuthenticationsGetOutput:
    return ProviderOauthConnectionsAuthenticationsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      error=mapProviderOauthConnectionsAuthenticationsGetOutputError.from_dict(
        data.get("error")
      )
      if data.get("error")
      else None,
      events=[
        mapProviderOauthConnectionsAuthenticationsGetOutputEvents.from_dict(item)
        for item in data.get("events", [])
        if item
      ],
      connection_id=data.get("connection_id"),
      profile=mapProviderOauthConnectionsAuthenticationsGetOutputProfile.from_dict(
        data.get("profile")
      )
      if data.get("profile")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsAuthenticationsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
