from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardOrganizationsInvitesCreateOutputOrganization:
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
class DashboardOrganizationsInvitesCreateOutputInvitedByTeams:
  id: str
  name: str
  slug: str
  assignment_id: str
  created_at: datetime
  updated_at: datetime


@dataclass
class DashboardOrganizationsInvitesCreateOutputInvitedBy:
  object: str
  id: str
  type: str
  organization_id: str
  name: str
  image_url: str
  teams: List[DashboardOrganizationsInvitesCreateOutputInvitedByTeams]
  created_at: datetime
  updated_at: datetime
  email: Optional[str] = None


@dataclass
class DashboardOrganizationsInvitesCreateOutputInviteLink:
  object: str
  id: str
  key_redacted: str
  created_at: datetime
  key: Optional[str] = None
  url: Optional[str] = None


@dataclass
class DashboardOrganizationsInvitesCreateOutput:
  object: str
  id: str
  status: str
  role: str
  type: str
  email: str
  organization: DashboardOrganizationsInvitesCreateOutputOrganization
  invited_by: DashboardOrganizationsInvitesCreateOutputInvitedBy
  invite_link: DashboardOrganizationsInvitesCreateOutputInviteLink
  created_at: datetime
  updated_at: datetime
  deleted_at: datetime
  expires_at: datetime
  accepted_at: datetime
  rejected_at: datetime


class mapDashboardOrganizationsInvitesCreateOutputOrganization:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsInvitesCreateOutputOrganization:
    return DashboardOrganizationsInvitesCreateOutputOrganization(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=data.get("type"),
      slug=data.get("slug"),
      name=data.get("name"),
      organization_id=data.get("organization_id"),
      image_url=data.get("image_url"),
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
      DashboardOrganizationsInvitesCreateOutputOrganization, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsInvitesCreateOutputInvitedByTeams:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsInvitesCreateOutputInvitedByTeams:
    return DashboardOrganizationsInvitesCreateOutputInvitedByTeams(
      id=data.get("id"),
      name=data.get("name"),
      slug=data.get("slug"),
      assignment_id=data.get("assignment_id"),
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
      DashboardOrganizationsInvitesCreateOutputInvitedByTeams, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsInvitesCreateOutputInvitedBy:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsInvitesCreateOutputInvitedBy:
    return DashboardOrganizationsInvitesCreateOutputInvitedBy(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      organization_id=data.get("organization_id"),
      name=data.get("name"),
      email=data.get("email"),
      image_url=data.get("image_url"),
      teams=[
        mapDashboardOrganizationsInvitesCreateOutputInvitedByTeams.from_dict(item)
        for item in data.get("teams", [])
        if item
      ],
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
      DashboardOrganizationsInvitesCreateOutputInvitedBy, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsInvitesCreateOutputInviteLink:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardOrganizationsInvitesCreateOutputInviteLink:
    return DashboardOrganizationsInvitesCreateOutputInviteLink(
      object=data.get("object"),
      id=data.get("id"),
      key=data.get("key"),
      key_redacted=data.get("key_redacted"),
      url=data.get("url"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardOrganizationsInvitesCreateOutputInviteLink, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardOrganizationsInvitesCreateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsInvitesCreateOutput:
    return DashboardOrganizationsInvitesCreateOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      type=data.get("type"),
      email=data.get("email"),
      organization=mapDashboardOrganizationsInvitesCreateOutputOrganization.from_dict(
        data.get("organization")
      )
      if data.get("organization")
      else None,
      invited_by=mapDashboardOrganizationsInvitesCreateOutputInvitedBy.from_dict(
        data.get("invited_by")
      )
      if data.get("invited_by")
      else None,
      invite_link=mapDashboardOrganizationsInvitesCreateOutputInviteLink.from_dict(
        data.get("invite_link")
      )
      if data.get("invite_link")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      deleted_at=parse_iso_datetime(data.get("deleted_at"))
      if data.get("deleted_at")
      else None,
      expires_at=parse_iso_datetime(data.get("expires_at"))
      if data.get("expires_at")
      else None,
      accepted_at=parse_iso_datetime(data.get("accepted_at"))
      if data.get("accepted_at")
      else None,
      rejected_at=parse_iso_datetime(data.get("rejected_at"))
      if data.get("rejected_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsInvitesCreateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


DashboardOrganizationsInvitesCreateBody = Dict[str, Any]


class mapDashboardOrganizationsInvitesCreateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardOrganizationsInvitesCreateBody:
    data

  @staticmethod
  def to_dict(
    value: Union[DashboardOrganizationsInvitesCreateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
