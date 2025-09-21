from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersImplementationsDeleteOutputServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersImplementationsDeleteOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersImplementationsDeleteOutput:
  object: str
  id: str
  status: str
  is_default: bool
  is_ephemeral: bool
  name: str
  metadata: Dict[str, Any]
  server_variant: ServersImplementationsDeleteOutputServerVariant
  server: ServersImplementationsDeleteOutputServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


class mapServersImplementationsDeleteOutputServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersImplementationsDeleteOutputServerVariant:
    return ServersImplementationsDeleteOutputServerVariant(
      object=data.get("object"),
      id=data.get("id"),
      identifier=data.get("identifier"),
      server_id=data.get("server_id"),
      source=data.get("source"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersImplementationsDeleteOutputServerVariant, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersImplementationsDeleteOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsDeleteOutputServer:
    return ServersImplementationsDeleteOutputServer(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ServersImplementationsDeleteOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersImplementationsDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsDeleteOutput:
    return ServersImplementationsDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      is_default=data.get("is_default"),
      is_ephemeral=data.get("is_ephemeral"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapServersImplementationsDeleteOutputServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapServersImplementationsDeleteOutputServer.from_dict(data.get("server"))
      if data.get("server")
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
    value: Union[ServersImplementationsDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
