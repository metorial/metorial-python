from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmConnectionsGetOutputExternalAccount:
    id: str
    login: str
    name: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class DashboardInstanceScmConnectionsGetOutput:
    object: str
    id: str
    provider: str
    external_account: DashboardInstanceScmConnectionsGetOutputExternalAccount
    created_at: datetime
    updated_at: datetime
    external_installation_id: Optional[str] = None
    account_type: Optional[str] = None


class mapDashboardInstanceScmConnectionsGetOutputExternalAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmConnectionsGetOutputExternalAccount:
        return DashboardInstanceScmConnectionsGetOutputExternalAccount(
        id=data.get('id'),
        login=data.get('login'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmConnectionsGetOutputExternalAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmConnectionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmConnectionsGetOutput:
        return DashboardInstanceScmConnectionsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        external_installation_id=data.get('external_installation_id'),
        account_type=data.get('account_type'),
        external_account=mapDashboardInstanceScmConnectionsGetOutputExternalAccount.from_dict(data.get('external_account')) if data.get('external_account') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmConnectionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

