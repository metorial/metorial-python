from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class DashboardOrganizationsJoinGetOutputOrganization:
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
class DashboardOrganizationsJoinGetOutputInvitedBy:
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
class DashboardOrganizationsJoinGetOutputInviteLink:
  object: str
  id: str
  key_redacted: str
  created_at: datetime
  key: Optional[str] = None
  url: Optional[str] = None


@dataclass
class DashboardOrganizationsJoinGetOutput:
  object: str
  id: str
  status: str
  role: str
  type: str
  email: str
  organization: DashboardOrganizationsJoinGetOutputOrganization
  invited_by: DashboardOrganizationsJoinGetOutputInvitedBy
  invite_link: DashboardOrganizationsJoinGetOutputInviteLink
  created_at: datetime
  updated_at: datetime
  deleted_at: datetime
  expires_at: datetime
  accepted_at: datetime
  rejected_at: datetime


class mapDashboardOrganizationsJoinGetOutputOrganization:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsJoinGetOutputOrganization:
    return DashboardOrganizationsJoinGetOutputOrganization(
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
    value: Union[DashboardOrganizationsJoinGetOutputOrganization, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsJoinGetOutputInvitedBy:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsJoinGetOutputInvitedBy:
    return DashboardOrganizationsJoinGetOutputInvitedBy(
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
    value: Union[DashboardOrganizationsJoinGetOutputInvitedBy, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsJoinGetOutputInviteLink:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsJoinGetOutputInviteLink:
    return DashboardOrganizationsJoinGetOutputInviteLink(
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
    value: Union[DashboardOrganizationsJoinGetOutputInviteLink, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsJoinGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsJoinGetOutput:
    return DashboardOrganizationsJoinGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      type=data.get("type"),
      email=data.get("email"),
      organization=mapDashboardOrganizationsJoinGetOutputOrganization.from_dict(
        data.get("organization")
      )
      if data.get("organization")
      else None,
      invited_by=mapDashboardOrganizationsJoinGetOutputInvitedBy.from_dict(
        data.get("invited_by")
      )
      if data.get("invited_by")
      else None,
      invite_link=mapDashboardOrganizationsJoinGetOutputInviteLink.from_dict(
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
    value: Union[DashboardOrganizationsJoinGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardOrganizationsJoinGetQuery:
  invite_key: str


class mapDashboardOrganizationsJoinGetQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsJoinGetQuery:
    return DashboardOrganizationsJoinGetQuery(invite_key=data.get("inviteKey"))

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsJoinGetQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
