from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ServersImplementationsUpdateOutputServerVariant:
  object: str
  id: str
  identifier: str
  server_id: str
  source: Dict[str, Any]
  created_at: datetime


@dataclass
class ServersImplementationsUpdateOutputServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ServersImplementationsUpdateOutput:
  object: str
  id: str
  status: str
  name: str
  metadata: Dict[str, Any]
  server_variant: ServersImplementationsUpdateOutputServerVariant
  server: ServersImplementationsUpdateOutputServer
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None
  get_launch_params: Optional[str] = None


class mapServersImplementationsUpdateOutputServerVariant:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ServersImplementationsUpdateOutputServerVariant:
    return ServersImplementationsUpdateOutputServerVariant(
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
    value: Union[ServersImplementationsUpdateOutputServerVariant, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersImplementationsUpdateOutputServer:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsUpdateOutputServer:
    return ServersImplementationsUpdateOutputServer(
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
    value: Union[ServersImplementationsUpdateOutputServer, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapServersImplementationsUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsUpdateOutput:
    return ServersImplementationsUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
      server_variant=mapServersImplementationsUpdateOutputServerVariant.from_dict(
        data.get("server_variant")
      )
      if data.get("server_variant")
      else None,
      server=mapServersImplementationsUpdateOutputServer.from_dict(data.get("server"))
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
    value: Union[ServersImplementationsUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ServersImplementationsUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  metadata: Optional[Dict[str, Any]] = None
  get_launch_params: Optional[str] = None


class mapServersImplementationsUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ServersImplementationsUpdateBody:
    return ServersImplementationsUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      get_launch_params=data.get("get_launch_params"),
    )

  @staticmethod
  def to_dict(
    value: Union[ServersImplementationsUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
