from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class CustomServersRemoteServersGetOutputProviderOauth:
  config: Dict[str, Any]
  scopes: List[str]


@dataclass
class CustomServersRemoteServersGetOutput:
  object: str
  id: str
  remote_url: str
  created_at: datetime
  updated_at: datetime
  provider_oauth: Optional[CustomServersRemoteServersGetOutputProviderOauth] = None


class mapCustomServersRemoteServersGetOutputProviderOauth:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> CustomServersRemoteServersGetOutputProviderOauth:
    return CustomServersRemoteServersGetOutputProviderOauth(
      config=data.get("config"), scopes=data.get("scopes", [])
    )

  @staticmethod
  def to_dict(
    value: Union[CustomServersRemoteServersGetOutputProviderOauth, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCustomServersRemoteServersGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CustomServersRemoteServersGetOutput:
    return CustomServersRemoteServersGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      remote_url=data.get("remote_url"),
      provider_oauth=mapCustomServersRemoteServersGetOutputProviderOauth.from_dict(
        data.get("provider_oauth")
      )
      if data.get("provider_oauth")
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
    value: Union[CustomServersRemoteServersGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
