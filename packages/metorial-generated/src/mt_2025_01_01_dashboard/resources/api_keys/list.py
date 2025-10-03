from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ApiKeysListOutputItemsMachineAccessActor:
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
class ApiKeysListOutputItemsMachineAccessInstanceProject:
  object: str
  id: str
  status: str
  slug: str
  name: str
  organization_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class ApiKeysListOutputItemsMachineAccessInstance:
  object: str
  id: str
  status: str
  slug: str
  name: str
  type: str
  organization_id: str
  project: ApiKeysListOutputItemsMachineAccessInstanceProject
  created_at: datetime
  updated_at: datetime


@dataclass
class ApiKeysListOutputItemsMachineAccessOrganization:
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
class ApiKeysListOutputItemsMachineAccessUser:
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
class ApiKeysListOutputItemsMachineAccess:
  object: str
  id: str
  status: str
  type: str
  name: str
  deleted_at: datetime
  last_used_at: datetime
  created_at: datetime
  updated_at: datetime
  actor: Optional[ApiKeysListOutputItemsMachineAccessActor] = None
  instance: Optional[ApiKeysListOutputItemsMachineAccessInstance] = None
  organization: Optional[ApiKeysListOutputItemsMachineAccessOrganization] = None
  user: Optional[ApiKeysListOutputItemsMachineAccessUser] = None


@dataclass
class ApiKeysListOutputItemsRevealInfo:
  until: datetime
  forever: bool


@dataclass
class ApiKeysListOutputItems:
  object: str
  id: str
  status: str
  secret_redacted: str
  secret_redacted_long: str
  type: str
  name: str
  machine_access: ApiKeysListOutputItemsMachineAccess
  created_at: datetime
  updated_at: datetime
  secret: Optional[str] = None
  description: Optional[str] = None
  deleted_at: Optional[datetime] = None
  last_used_at: Optional[datetime] = None
  expires_at: Optional[datetime] = None
  reveal_info: Optional[ApiKeysListOutputItemsRevealInfo] = None


@dataclass
class ApiKeysListOutputPagination:
  has_more_before: bool
  has_more_after: bool


@dataclass
class ApiKeysListOutput:
  items: List[ApiKeysListOutputItems]
  pagination: ApiKeysListOutputPagination


class mapApiKeysListOutputItemsMachineAccessActor:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListOutputItemsMachineAccessActor:
    return ApiKeysListOutputItemsMachineAccessActor(
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
    value: Union[ApiKeysListOutputItemsMachineAccessActor, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutputItemsMachineAccessInstanceProject:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ApiKeysListOutputItemsMachineAccessInstanceProject:
    return ApiKeysListOutputItemsMachineAccessInstanceProject(
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
    value: Union[
      ApiKeysListOutputItemsMachineAccessInstanceProject, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutputItemsMachineAccessInstance:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListOutputItemsMachineAccessInstance:
    return ApiKeysListOutputItemsMachineAccessInstance(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      slug=data.get("slug"),
      name=data.get("name"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      project=mapApiKeysListOutputItemsMachineAccessInstanceProject.from_dict(
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
    value: Union[ApiKeysListOutputItemsMachineAccessInstance, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutputItemsMachineAccessOrganization:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ApiKeysListOutputItemsMachineAccessOrganization:
    return ApiKeysListOutputItemsMachineAccessOrganization(
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
    value: Union[ApiKeysListOutputItemsMachineAccessOrganization, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutputItemsMachineAccessUser:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListOutputItemsMachineAccessUser:
    return ApiKeysListOutputItemsMachineAccessUser(
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
    value: Union[ApiKeysListOutputItemsMachineAccessUser, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutputItemsMachineAccess:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListOutputItemsMachineAccess:
    return ApiKeysListOutputItemsMachineAccess(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      name=data.get("name"),
      actor=mapApiKeysListOutputItemsMachineAccessActor.from_dict(data.get("actor"))
      if data.get("actor")
      else None,
      instance=mapApiKeysListOutputItemsMachineAccessInstance.from_dict(
        data.get("instance")
      )
      if data.get("instance")
      else None,
      organization=mapApiKeysListOutputItemsMachineAccessOrganization.from_dict(
        data.get("organization")
      )
      if data.get("organization")
      else None,
      user=mapApiKeysListOutputItemsMachineAccessUser.from_dict(data.get("user"))
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
    value: Union[ApiKeysListOutputItemsMachineAccess, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutputItemsRevealInfo:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListOutputItemsRevealInfo:
    return ApiKeysListOutputItemsRevealInfo(
      until=datetime.fromisoformat(data.get("until")) if data.get("until") else None,
      forever=data.get("forever"),
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysListOutputItemsRevealInfo, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutputItems:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListOutputItems:
    return ApiKeysListOutputItems(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      secret_redacted=data.get("secret_redacted"),
      secret_redacted_long=data.get("secret_redacted_long"),
      secret=data.get("secret"),
      type=data.get("type"),
      name=data.get("name"),
      description=data.get("description"),
      machine_access=mapApiKeysListOutputItemsMachineAccess.from_dict(
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
      reveal_info=mapApiKeysListOutputItemsRevealInfo.from_dict(data.get("reveal_info"))
      if data.get("reveal_info")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysListOutputItems, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutputPagination:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListOutputPagination:
    return ApiKeysListOutputPagination(
      has_more_before=data.get("has_more_before"),
      has_more_after=data.get("has_more_after"),
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysListOutputPagination, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapApiKeysListOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListOutput:
    return ApiKeysListOutput(
      items=[
        mapApiKeysListOutputItems.from_dict(item)
        for item in data.get("items", [])
        if item
      ],
      pagination=mapApiKeysListOutputPagination.from_dict(data.get("pagination"))
      if data.get("pagination")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysListOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ApiKeysListQuery:
  limit: Optional[float] = None
  after: Optional[str] = None
  before: Optional[str] = None
  cursor: Optional[str] = None
  order: Optional[str] = None
  type: Optional[str] = None
  instance_id: Optional[str] = None


class mapApiKeysListQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ApiKeysListQuery:
    return ApiKeysListQuery(
      limit=data.get("limit"),
      after=data.get("after"),
      before=data.get("before"),
      cursor=data.get("cursor"),
      order=data.get("order"),
      type=data.get("type"),
      instance_id=data.get("instance_id"),
    )

  @staticmethod
  def to_dict(
    value: Union[ApiKeysListQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
