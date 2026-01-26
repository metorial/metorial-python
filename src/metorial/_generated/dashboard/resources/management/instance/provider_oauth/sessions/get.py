from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceProviderOauthSessionsGetOutputConnectionProvider:
  id: str
  name: str
  url: str
  image_url: str


@dataclass
class ManagementInstanceProviderOauthSessionsGetOutputConnection:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  provider: ManagementInstanceProviderOauthSessionsGetOutputConnectionProvider
  config: Dict[str, Any]
  client_id: str
  instance_id: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  template_id: Optional[str] = None


@dataclass
class ManagementInstanceProviderOauthSessionsGetOutput:
  object: str
  id: str
  status: str
  url: str
  connection: ManagementInstanceProviderOauthSessionsGetOutputConnection
  metadata: Dict[str, Any]
  instance_id: str
  created_at: datetime
  updated_at: datetime
  redirect_uri: Optional[str] = None
  completed_at: Optional[datetime] = None


class mapManagementInstanceProviderOauthSessionsGetOutputConnectionProvider:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceProviderOauthSessionsGetOutputConnectionProvider:
    return ManagementInstanceProviderOauthSessionsGetOutputConnectionProvider(
      id=data.get("id"),
      name=data.get("name"),
      url=data.get("url"),
      image_url=data.get("image_url"),
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceProviderOauthSessionsGetOutputConnectionProvider,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceProviderOauthSessionsGetOutputConnection:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceProviderOauthSessionsGetOutputConnection:
    return ManagementInstanceProviderOauthSessionsGetOutputConnection(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      provider=mapManagementInstanceProviderOauthSessionsGetOutputConnectionProvider.from_dict(
        data.get("provider")
      )
      if data.get("provider")
      else None,
      config=data.get("config"),
      client_id=data.get("client_id"),
      instance_id=data.get("instance_id"),
      template_id=data.get("template_id"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceProviderOauthSessionsGetOutputConnection, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceProviderOauthSessionsGetOutput:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceProviderOauthSessionsGetOutput:
    return ManagementInstanceProviderOauthSessionsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      url=data.get("url"),
      connection=mapManagementInstanceProviderOauthSessionsGetOutputConnection.from_dict(
        data.get("connection")
      )
      if data.get("connection")
      else None,
      metadata=data.get("metadata"),
      redirect_uri=data.get("redirect_uri"),
      instance_id=data.get("instance_id"),
      completed_at=parse_iso_datetime(data.get("completed_at"))
      if data.get("completed_at")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceProviderOauthSessionsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
