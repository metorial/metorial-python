from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputItems:
    object: str
    id: str
    deduplicated: bool
    setup_session_id: str
    created_at: datetime
    recipient_email: Optional[str] = None
    organization_member_id: Optional[str] = None
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutput:
    items: List[ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputItems]
    pagination: ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputPagination


class mapManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputItems:
        return ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        deduplicated=data.get('deduplicated'),
        setup_session_id=data.get('setup_session_id'),
        recipient_email=data.get('recipient_email'),
        organization_member_id=data.get('organization_member_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputPagination:
        return ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutput:
        return ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutput(
        items=[mapManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsEmailsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsSetupSessionsEmailsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapManagementInstanceProviderDeploymentsSetupSessionsEmailsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsSetupSessionsEmailsListQuery:
        return ManagementInstanceProviderDeploymentsSetupSessionsEmailsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsSetupSessionsEmailsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

