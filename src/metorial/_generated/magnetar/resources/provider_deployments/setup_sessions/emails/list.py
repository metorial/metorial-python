from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsSetupSessionsEmailsListOutputItems:
    object: str
    id: str
    deduplicated: bool
    setup_session_id: str
    created_at: datetime
    recipient_email: Optional[str] = None
    organization_member_id: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsEmailsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderDeploymentsSetupSessionsEmailsListOutput:
    items: List[ProviderDeploymentsSetupSessionsEmailsListOutputItems]
    pagination: ProviderDeploymentsSetupSessionsEmailsListOutputPagination


class mapProviderDeploymentsSetupSessionsEmailsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsEmailsListOutputItems:
        return ProviderDeploymentsSetupSessionsEmailsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        deduplicated=data.get('deduplicated'),
        setup_session_id=data.get('setup_session_id'),
        recipient_email=data.get('recipient_email'),
        organization_member_id=data.get('organization_member_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsEmailsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsEmailsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsEmailsListOutputPagination:
        return ProviderDeploymentsSetupSessionsEmailsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsEmailsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsEmailsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsEmailsListOutput:
        return ProviderDeploymentsSetupSessionsEmailsListOutput(
        items=[mapProviderDeploymentsSetupSessionsEmailsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderDeploymentsSetupSessionsEmailsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsEmailsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsSetupSessionsEmailsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None


class mapProviderDeploymentsSetupSessionsEmailsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsEmailsListQuery:
        return ProviderDeploymentsSetupSessionsEmailsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsEmailsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

