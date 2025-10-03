from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionsCreateOutputProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ProviderOauthConnectionsCreateOutput:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ProviderOauthConnectionsCreateOutputProvider
  config: Dict[str, Any]
  scopes: List[str]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


class mapProviderOauthConnectionsCreateOutputProvider:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsCreateOutputProvider:
    return ProviderOauthConnectionsCreateOutputProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsCreateOutputProvider, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsCreateOutput:
    return ProviderOauthConnectionsCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapProviderOauthConnectionsCreateOutputProvider.from_dict(
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
    value: Union[ProviderOauthConnectionsCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthConnectionsCreateBody:
  config: Dict[str, Any]
  scopes: List[str]
  template_id: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None
  discovery_url: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  client_id: Optional[str] = None
  client_secret: Optional[str] = None
  auto_registration_id: Optional[str] = None


class mapProviderOauthConnectionsCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsCreateBody:
    return ProviderOauthConnectionsCreateBody(
      template_id=data.get("template_id"),
      name=data.get("name"),
      description=data.get("description"),
      discovery_url=data.get("discovery_url"),
      config=data.get("config"),
      scopes=data.get("scopes", []),
      metadata=data.get("metadata"),
      client_id=data.get("client_id"),
      client_secret=data.get("client_secret"),
      auto_registration_id=data.get("auto_registration_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
