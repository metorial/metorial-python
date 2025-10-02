from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ManagementOrganizationInvitesCreateOutputOrganization:
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
class ManagementOrganizationInvitesCreateOutputInvitedBy:
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
class ManagementOrganizationInvitesCreateOutputInviteLink:
  object: str
  id: str
  key_redacted: str
  created_at: datetime
  key: Optional[str] = None
  url: Optional[str] = None


@dataclass
class ManagementOrganizationInvitesCreateOutput:
  object: str
  id: str
  status: str
  role: str
  type: str
  email: str
  organization: ManagementOrganizationInvitesCreateOutputOrganization
  invited_by: ManagementOrganizationInvitesCreateOutputInvitedBy
  invite_link: ManagementOrganizationInvitesCreateOutputInviteLink
  created_at: datetime
  updated_at: datetime
  deleted_at: datetime
  expires_at: datetime
  accepted_at: datetime
  rejected_at: datetime


class mapManagementOrganizationInvitesCreateOutputOrganization:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInvitesCreateOutputOrganization:
    return ManagementOrganizationInvitesCreateOutputOrganization(
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
    value: Union[
      ManagementOrganizationInvitesCreateOutputOrganization, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInvitesCreateOutputInvitedBy:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInvitesCreateOutputInvitedBy:
    return ManagementOrganizationInvitesCreateOutputInvitedBy(
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
    value: Union[
      ManagementOrganizationInvitesCreateOutputInvitedBy, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInvitesCreateOutputInviteLink:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInvitesCreateOutputInviteLink:
    return ManagementOrganizationInvitesCreateOutputInviteLink(
      object=data.get("object"),
      id=data.get("id"),
      key=data.get("key"),
      key_redacted=data.get("key_redacted"),
      url=data.get("url"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementOrganizationInvitesCreateOutputInviteLink, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInvitesCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInvitesCreateOutput:
    return ManagementOrganizationInvitesCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      type=data.get("type"),
      email=data.get("email"),
      organization=mapManagementOrganizationInvitesCreateOutputOrganization.from_dict(
        data.get("organization")
      )
      if data.get("organization")
      else None,
      invited_by=mapManagementOrganizationInvitesCreateOutputInvitedBy.from_dict(
        data.get("invited_by")
      )
      if data.get("invited_by")
      else None,
      invite_link=mapManagementOrganizationInvitesCreateOutputInviteLink.from_dict(
        data.get("invite_link")
      )
      if data.get("invite_link")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=datetime.fromisoformat(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      deleted_at=datetime.fromisoformat(data.get("deleted_at"))
      if data.get("deleted_at")
      else None,
      expires_at=datetime.fromisoformat(data.get("expires_at"))
      if data.get("expires_at")
      else None,
      accepted_at=datetime.fromisoformat(data.get("accepted_at"))
      if data.get("accepted_at")
      else None,
      rejected_at=datetime.fromisoformat(data.get("rejected_at"))
      if data.get("rejected_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationInvitesCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


ManagementOrganizationInvitesCreateBody = Dict[str, Any]


class mapManagementOrganizationInvitesCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInvitesCreateBody:
    data

  @staticmethod
  def to_dict(
    value: Union[ManagementOrganizationInvitesCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
