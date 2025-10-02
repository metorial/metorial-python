from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ApiKeysRevealOutputMachineAccessActor:
  object: str
  id: str
  type: str
  organization_id: str
  name: str
  image_url: str
  created_at: datetime
  updated_at: datetime
  email: Optional[str] = None


@dataclass
class ApiKeysRevealOutputMachineAccessInstanceProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ApiKeysRevealOutputMachineAccessInstance:
  object: str
  id: str
  status: str
  slug: str
  name: str
  type: str
  organization_id: str
  project: ApiKeysRevealOutputMachineAccessInstanceProject
  created_at: datetime
  updated_at: datetime


@dataclass
class ApiKeysRevealOutputMachineAccessOrganization:
  object: str
  id: str
  status: str
  type: str
  slug: str
  name: str
  organization_id: str
  image_url: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ApiKeysRevealOutputMachineAccessUser:
  object: str
  id: str
  status: str
  type: str
  email: str
  name: str
  first_name: str
  last_name: str
  image_url: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ApiKeysRevealOutputMachineAccess:
  object: str
  id: str
  status: str
  type: str
  name: str
  deleted_at: datetime
  last_used_at: datetime
  created_at: datetime
  updated_at: datetime
  actor: Optional[ApiKeysRevealOutputMachineAccessActor] = None
  instance: Optional[ApiKeysRevealOutputMachineAccessInstance] = None
  organization: Optional[ApiKeysRevealOutputMachineAccessOrganization] = None
  user: Optional[ApiKeysRevealOutputMachineAccessUser] = None


@dataclass
class ApiKeysRevealOutputRevealInfo:
  until: datetime
  forever: bool


@dataclass
class ApiKeysRevealOutput:
  object: str
  id: str
  status: str
  secret_redacted: str
  secret_redacted_long: str
  type: str
  name: str
  machine_access: ApiKeysRevealOutputMachineAccess
  created_at: datetime
  updated_at: datetime
  secret: Optional[str] = None
  description: Optional[str] = None
  deleted_at: Optional[datetime] = None
  last_used_at: Optional[datetime] = None
  expires_at: Optional[datetime] = None
  reveal_info: Optional[ApiKeysRevealOutputRevealInfo] = None


class mapApiKeysRevealOutputMachineAccessActor:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysRevealOutputMachineAccessActor:
    return ApiKeysRevealOutputMachineAccessActor(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      email=data.get("email"),
      image_url=data.get("image_url"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysRevealOutputMachineAccessActor, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysRevealOutputMachineAccessInstanceProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ApiKeysRevealOutputMachineAccessInstanceProject:
    return ApiKeysRevealOutputMachineAccessInstanceProject(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      organization_id=data.get("organization_id"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysRevealOutputMachineAccessInstanceProject, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysRevealOutputMachineAccessInstance:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysRevealOutputMachineAccessInstance:
    return ApiKeysRevealOutputMachineAccessInstance(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      project=mapApiKeysRevealOutputMachineAccessInstanceProject.from_dict(
        data.get("project")
      )
      if data.get("project")
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
    value: Union[ApiKeysRevealOutputMachineAccessInstance, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysRevealOutputMachineAccessOrganization:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysRevealOutputMachineAccessOrganization:
    return ApiKeysRevealOutputMachineAccessOrganization(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      slug=data.get("slug"),
      name=data.get("name"),
      organization_id=data.get("organization_id"),
      image_url=data.get("image_url"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysRevealOutputMachineAccessOrganization, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysRevealOutputMachineAccessUser:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysRevealOutputMachineAccessUser:
    return ApiKeysRevealOutputMachineAccessUser(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      email=data.get("email"),
      name=data.get("name"),
      first_name=data.get("first_name"),
      last_name=data.get("last_name"),
      image_url=data.get("image_url"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysRevealOutputMachineAccessUser, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysRevealOutputMachineAccess:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysRevealOutputMachineAccess:
    return ApiKeysRevealOutputMachineAccess(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      name=data.get("name"),
      actor=mapApiKeysRevealOutputMachineAccessActor.from_dict(data.get("actor"))
      if data.get("actor")
      else None,
      instance=mapApiKeysRevealOutputMachineAccessInstance.from_dict(
        data.get("instance")
      )
      if data.get("instance")
      else None,
      organization=mapApiKeysRevealOutputMachineAccessOrganization.from_dict(
        data.get("organization")
      )
      if data.get("organization")
      else None,
      user=mapApiKeysRevealOutputMachineAccessUser.from_dict(data.get("user"))
      if data.get("user")
      else None,
      deleted_at=datetime.fromisoformat(data.get("deleted_at"))
      if data.get("deleted_at")
      else None,
      last_used_at=datetime.fromisoformat(data.get("last_used_at"))
      if data.get("last_used_at")
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
    value: Union[ApiKeysRevealOutputMachineAccess, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysRevealOutputRevealInfo:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysRevealOutputRevealInfo:
    return ApiKeysRevealOutputRevealInfo(
      until=datetime.fromisoformat(data.get("until")) if data.get("until") else None,
      forever=data.get("forever"),
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysRevealOutputRevealInfo, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysRevealOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysRevealOutput:
    return ApiKeysRevealOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      secret_redacted=data.get("secret_redacted"),
      secret_redacted_long=data.get("secret_redacted_long"),
      secret=data.get("secret"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      machine_access=mapApiKeysRevealOutputMachineAccess.from_dict(
        data.get("machine_access")
      )
      if data.get("machine_access")
      else None,
      deleted_at=datetime.fromisoformat(data.get("deleted_at"))
      if data.get("deleted_at")
      else None,
      last_used_at=datetime.fromisoformat(data.get("last_used_at"))
      if data.get("last_used_at")
      else None,
      expires_at=datetime.fromisoformat(data.get("expires_at"))
      if data.get("expires_at")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      reveal_info=mapApiKeysRevealOutputRevealInfo.from_dict(data.get("reveal_info"))
      if data.get("reveal_info")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysRevealOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
