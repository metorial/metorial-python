from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionsUpdateOutputProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ProviderOauthConnectionsUpdateOutput:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ProviderOauthConnectionsUpdateOutputProvider
  config: Dict[str, Any]
  scopes: List[str]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


class mapProviderOauthConnectionsUpdateOutputProvider:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsUpdateOutputProvider:
    return ProviderOauthConnectionsUpdateOutputProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsUpdateOutputProvider, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapProviderOauthConnectionsUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsUpdateOutput:
    return ProviderOauthConnectionsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapProviderOauthConnectionsUpdateOutputProvider.from_dict(
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
    value: Union[ProviderOauthConnectionsUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthConnectionsUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  config: Optional[Dict[str, Any]] = None
  client_id: Optional[str] = None
  client_secret: Optional[str] = None
  scopes: Optional[List[str]] = None
  metadata: Optional[Dict[str, Any]] = None


class mapProviderOauthConnectionsUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionsUpdateBody:
    return ProviderOauthConnectionsUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      config=data.get("config"),
      client_id=data.get("client_id"),
      client_secret=data.get("client_secret"),
      scopes=data.get("scopes", []),
      metadata=data.get("metadata"),
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionsUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
