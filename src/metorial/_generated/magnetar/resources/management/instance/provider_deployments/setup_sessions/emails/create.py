from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputItems:
    object: str
    id: str
    deduplicated: bool
    setup_session_id: str
    created_at: datetime
    recipient_email: Optional[str] = None
    organization_member_id: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput:
    items: List[ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputItems]
    pagination: ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputPagination


class mapManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputItems:
        return ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        deduplicated=data.get('deduplicated'),
        setup_session_id=data.get('setup_session_id'),
        recipient_email=data.get('recipient_email'),
        organization_member_id=data.get('organization_member_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputPagination:
        return ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput:
        return ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput(
        items=[mapManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateBody:
    emails: Optional[List[str]] = None
    organization_member_ids: Optional[List[str]] = None


class mapManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateBody:
        return ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateBody(
        emails=data.get('emails', []),
        organization_member_ids=data.get('organization_member_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsEmailsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

