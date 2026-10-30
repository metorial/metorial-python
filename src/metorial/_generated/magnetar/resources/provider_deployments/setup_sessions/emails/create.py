from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderDeploymentsSetupSessionsEmailsCreateOutputItems:
    object: str
    id: str
    deduplicated: bool
    setup_session_id: str
    created_at: datetime
    recipient_email: Optional[str] = None
    organization_member_id: Optional[str] = None
@dataclass
class ProviderDeploymentsSetupSessionsEmailsCreateOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ProviderDeploymentsSetupSessionsEmailsCreateOutput:
    items: List[ProviderDeploymentsSetupSessionsEmailsCreateOutputItems]
    pagination: ProviderDeploymentsSetupSessionsEmailsCreateOutputPagination


class mapProviderDeploymentsSetupSessionsEmailsCreateOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsEmailsCreateOutputItems:
        return ProviderDeploymentsSetupSessionsEmailsCreateOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        deduplicated=data.get('deduplicated'),
        setup_session_id=data.get('setup_session_id'),
        recipient_email=data.get('recipient_email'),
        organization_member_id=data.get('organization_member_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsEmailsCreateOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsEmailsCreateOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsEmailsCreateOutputPagination:
        return ProviderDeploymentsSetupSessionsEmailsCreateOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsEmailsCreateOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderDeploymentsSetupSessionsEmailsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsEmailsCreateOutput:
        return ProviderDeploymentsSetupSessionsEmailsCreateOutput(
        items=[mapProviderDeploymentsSetupSessionsEmailsCreateOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapProviderDeploymentsSetupSessionsEmailsCreateOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsEmailsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProviderDeploymentsSetupSessionsEmailsCreateBody:
    emails: Optional[List[str]] = None
    organization_member_ids: Optional[List[str]] = None


class mapProviderDeploymentsSetupSessionsEmailsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderDeploymentsSetupSessionsEmailsCreateBody:
        return ProviderDeploymentsSetupSessionsEmailsCreateBody(
        emails=data.get('emails', []),
        organization_member_ids=data.get('organization_member_ids', [])
        )

    @staticmethod
    def to_dict(value: Union[ProviderDeploymentsSetupSessionsEmailsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

