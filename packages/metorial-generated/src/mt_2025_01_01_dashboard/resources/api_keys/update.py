from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ApiKeysUpdateOutputMachineAccessActor:
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
class ApiKeysUpdateOutputMachineAccessInstanceProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ApiKeysUpdateOutputMachineAccessInstance:
  object: str
  id: str
  status: str
  slug: str
  name: str
  type: str
  organization_id: str
  project: ApiKeysUpdateOutputMachineAccessInstanceProject
  created_at: datetime
  updated_at: datetime


@dataclass
class ApiKeysUpdateOutputMachineAccessOrganization:
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
class ApiKeysUpdateOutputMachineAccessUser:
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
class ApiKeysUpdateOutputMachineAccess:
  object: str
  id: str
  status: str
  type: str
  name: str
  deleted_at: datetime
  last_used_at: datetime
  created_at: datetime
  updated_at: datetime
  actor: Optional[ApiKeysUpdateOutputMachineAccessActor] = None
  instance: Optional[ApiKeysUpdateOutputMachineAccessInstance] = None
  organization: Optional[ApiKeysUpdateOutputMachineAccessOrganization] = None
  user: Optional[ApiKeysUpdateOutputMachineAccessUser] = None


@dataclass
class ApiKeysUpdateOutputRevealInfo:
  until: datetime
  forever: bool


@dataclass
class ApiKeysUpdateOutput:
  object: str
  id: str
  status: str
  secret_redacted: str
  secret_redacted_long: str
  type: str
  name: str
  machine_access: ApiKeysUpdateOutputMachineAccess
  created_at: datetime
  updated_at: datetime
  secret: Optional[str] = None
  description: Optional[str] = None
  deleted_at: Optional[datetime] = None
  last_used_at: Optional[datetime] = None
  expires_at: Optional[datetime] = None
  reveal_info: Optional[ApiKeysUpdateOutputRevealInfo] = None


class mapApiKeysUpdateOutputMachineAccessActor:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysUpdateOutputMachineAccessActor:
    return ApiKeysUpdateOutputMachineAccessActor(
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
    value: Union[ApiKeysUpdateOutputMachineAccessActor, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysUpdateOutputMachineAccessInstanceProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ApiKeysUpdateOutputMachineAccessInstanceProject:
    return ApiKeysUpdateOutputMachineAccessInstanceProject(
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
    value: Union[ApiKeysUpdateOutputMachineAccessInstanceProject, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysUpdateOutputMachineAccessInstance:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysUpdateOutputMachineAccessInstance:
    return ApiKeysUpdateOutputMachineAccessInstance(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      project=mapApiKeysUpdateOutputMachineAccessInstanceProject.from_dict(
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
    value: Union[ApiKeysUpdateOutputMachineAccessInstance, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysUpdateOutputMachineAccessOrganization:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysUpdateOutputMachineAccessOrganization:
    return ApiKeysUpdateOutputMachineAccessOrganization(
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
    value: Union[ApiKeysUpdateOutputMachineAccessOrganization, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysUpdateOutputMachineAccessUser:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysUpdateOutputMachineAccessUser:
    return ApiKeysUpdateOutputMachineAccessUser(
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
    value: Union[ApiKeysUpdateOutputMachineAccessUser, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysUpdateOutputMachineAccess:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysUpdateOutputMachineAccess:
    return ApiKeysUpdateOutputMachineAccess(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      name=data.get("name"),
      actor=mapApiKeysUpdateOutputMachineAccessActor.from_dict(data.get("actor"))
      if data.get("actor")
      else None,
      instance=mapApiKeysUpdateOutputMachineAccessInstance.from_dict(
        data.get("instance")
      )
      if data.get("instance")
      else None,
      organization=mapApiKeysUpdateOutputMachineAccessOrganization.from_dict(
        data.get("organization")
      )
      if data.get("organization")
      else None,
      user=mapApiKeysUpdateOutputMachineAccessUser.from_dict(data.get("user"))
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
    value: Union[ApiKeysUpdateOutputMachineAccess, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysUpdateOutputRevealInfo:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysUpdateOutputRevealInfo:
    return ApiKeysUpdateOutputRevealInfo(
      until=datetime.fromisoformat(data.get("until")) if data.get("until") else None,
      forever=data.get("forever"),
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysUpdateOutputRevealInfo, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysUpdateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysUpdateOutput:
    return ApiKeysUpdateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      secret_redacted=data.get("secret_redacted"),
      secret_redacted_long=data.get("secret_redacted_long"),
      secret=data.get("secret"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      machine_access=mapApiKeysUpdateOutputMachineAccess.from_dict(
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
      reveal_info=mapApiKeysUpdateOutputRevealInfo.from_dict(data.get("reveal_info"))
      if data.get("reveal_info")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysUpdateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ApiKeysUpdateBody:
  name: Optional[str] = None
  description: Optional[str] = None
  expires_at: Optional[datetime] = None


class mapApiKeysUpdateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysUpdateBody:
    return ApiKeysUpdateBody(
      name=data.get("name"),
      description=data.get("description"),
      expires_at=datetime.fromisoformat(data.get("expires_at"))
      if data.get("expires_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysUpdateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
