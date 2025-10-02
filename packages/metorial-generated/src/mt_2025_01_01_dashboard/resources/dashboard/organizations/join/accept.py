from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class DashboardOrganizationsJoinAcceptOutputOrganization:
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
class DashboardOrganizationsJoinAcceptOutputInvitedBy:
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
class DashboardOrganizationsJoinAcceptOutputInviteLink:
  object: str
  id: str
  key_redacted: str
  created_at: datetime
  key: Optional[str] = None
  url: Optional[str] = None


@dataclass
class DashboardOrganizationsJoinAcceptOutput:
  object: str
  id: str
  status: str
  role: str
  type: str
  email: str
  organization: DashboardOrganizationsJoinAcceptOutputOrganization
  invited_by: DashboardOrganizationsJoinAcceptOutputInvitedBy
  invite_link: DashboardOrganizationsJoinAcceptOutputInviteLink
  created_at: datetime
  updated_at: datetime
  deleted_at: datetime
  expires_at: datetime
  accepted_at: datetime
  rejected_at: datetime


class mapDashboardOrganizationsJoinAcceptOutputOrganization:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsJoinAcceptOutputOrganization:
    return DashboardOrganizationsJoinAcceptOutputOrganization(
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
      DashboardOrganizationsJoinAcceptOutputOrganization, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsJoinAcceptOutputInvitedBy:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsJoinAcceptOutputInvitedBy:
    return DashboardOrganizationsJoinAcceptOutputInvitedBy(
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
    value: Union[DashboardOrganizationsJoinAcceptOutputInvitedBy, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsJoinAcceptOutputInviteLink:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsJoinAcceptOutputInviteLink:
    return DashboardOrganizationsJoinAcceptOutputInviteLink(
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
    value: Union[DashboardOrganizationsJoinAcceptOutputInviteLink, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsJoinAcceptOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsJoinAcceptOutput:
    return DashboardOrganizationsJoinAcceptOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      type=data.get("type"),
      email=data.get("email"),
      organization=mapDashboardOrganizationsJoinAcceptOutputOrganization.from_dict(
        data.get("organization")
      )
      if data.get("organization")
      else None,
      invited_by=mapDashboardOrganizationsJoinAcceptOutputInvitedBy.from_dict(
        data.get("invited_by")
      )
      if data.get("invited_by")
      else None,
      invite_link=mapDashboardOrganizationsJoinAcceptOutputInviteLink.from_dict(
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
    value: Union[DashboardOrganizationsJoinAcceptOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardOrganizationsJoinAcceptBody:
  invite_key: str


class mapDashboardOrganizationsJoinAcceptBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsJoinAcceptBody:
    return DashboardOrganizationsJoinAcceptBody(invite_key=data.get("invite_key"))

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsJoinAcceptBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
