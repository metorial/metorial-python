from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthSessionsCreateOutputConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ProviderOauthSessionsCreateOutputConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ProviderOauthSessionsCreateOutputConnectionProvider
  config: Dict[str, Any]
  scopes: List[str]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class ProviderOauthSessionsCreateOutput:
  object: str
  id: str
  status: str
  url: str
  connection: ProviderOauthSessionsCreateOutputConnection
  metadata: Dict[str, Any]
  instance_id: str
  created_at: datetime
  updated_at: datetime
  redirect_uri: Optional[str] = None
  completed_at: Optional[datetime] = None


class mapProviderOauthSessionsCreateOutputConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ProviderOauthSessionsCreateOutputConnectionProvider:
    return ProviderOauthSessionsCreateOutputConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ProviderOauthSessionsCreateOutputConnectionProvider, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthSessionsCreateOutputConnection:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthSessionsCreateOutputConnection:
    return ProviderOauthSessionsCreateOutputConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapProviderOauthSessionsCreateOutputConnectionProvider.from_dict(
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
    value: Union[ProviderOauthSessionsCreateOutputConnection, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthSessionsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthSessionsCreateOutput:
    return ProviderOauthSessionsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      url=data.get("url"),
      connection=mapProviderOauthSessionsCreateOutputConnection.from_dict(
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
    value: Union[ProviderOauthSessionsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthSessionsCreateBody:
  metadata: Optional[Dict[str, Any]] = None
  redirect_uri: Optional[str] = None
  server_deployment_id: Optional[str] = None
  connection_id: Optional[str] = None


class mapProviderOauthSessionsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthSessionsCreateBody:
    return ProviderOauthSessionsCreateBody(
      metadata=data.get("metadata"),
      redirect_uri=data.get("redirect_uri"),
      server_deployment_id=data.get("server_deployment_id"),
      connection_id=data.get("connection_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthSessionsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
