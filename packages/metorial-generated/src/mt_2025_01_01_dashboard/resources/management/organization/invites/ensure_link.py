from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ManagementOrganizationInvitesEnsureLinkOutputOrganization:
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
class ManagementOrganizationInvitesEnsureLinkOutputInvitedBy:
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
class ManagementOrganizationInvitesEnsureLinkOutputInviteLink:
  object: str
  id: str
  key_redacted: str
  created_at: datetime
  key: Optional[str] = None
  url: Optional[str] = None


@dataclass
class ManagementOrganizationInvitesEnsureLinkOutput:
  object: str
  id: str
  status: str
  role: str
  type: str
  email: str
  organization: ManagementOrganizationInvitesEnsureLinkOutputOrganization
  invited_by: ManagementOrganizationInvitesEnsureLinkOutputInvitedBy
  invite_link: ManagementOrganizationInvitesEnsureLinkOutputInviteLink
  created_at: datetime
  updated_at: datetime
  deleted_at: datetime
  expires_at: datetime
  accepted_at: datetime
  rejected_at: datetime


class mapManagementOrganizationInvitesEnsureLinkOutputOrganization:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInvitesEnsureLinkOutputOrganization:
    return ManagementOrganizationInvitesEnsureLinkOutputOrganization(
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
      ManagementOrganizationInvitesEnsureLinkOutputOrganization, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInvitesEnsureLinkOutputInvitedBy:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInvitesEnsureLinkOutputInvitedBy:
    return ManagementOrganizationInvitesEnsureLinkOutputInvitedBy(
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
      ManagementOrganizationInvitesEnsureLinkOutputInvitedBy, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInvitesEnsureLinkOutputInviteLink:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementOrganizationInvitesEnsureLinkOutputInviteLink:
    return ManagementOrganizationInvitesEnsureLinkOutputInviteLink(
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
      ManagementOrganizationInvitesEnsureLinkOutputInviteLink, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementOrganizationInvitesEnsureLinkOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementOrganizationInvitesEnsureLinkOutput:
    return ManagementOrganizationInvitesEnsureLinkOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      role=data.get("role"),
      type=data.get("type"),
      email=data.get("email"),
      organization=mapManagementOrganizationInvitesEnsureLinkOutputOrganization.from_dict(
        data.get("organization")
      )
      if data.get("organization")
      else None,
      invited_by=mapManagementOrganizationInvitesEnsureLinkOutputInvitedBy.from_dict(
        data.get("invited_by")
      )
      if data.get("invited_by")
      else None,
      invite_link=mapManagementOrganizationInvitesEnsureLinkOutputInviteLink.from_dict(
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
    value: Union[ManagementOrganizationInvitesEnsureLinkOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
