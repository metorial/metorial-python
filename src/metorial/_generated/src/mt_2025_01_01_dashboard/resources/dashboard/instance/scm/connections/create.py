from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceScmConnectionsCreateOutputConnectionExternalAccount:
    id: str
    login: str
    name: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class DashboardInstanceScmConnectionsCreateOutputConnection:
    object: str
    id: str
    provider: str
    external_account: DashboardInstanceScmConnectionsCreateOutputConnectionExternalAccount
    created_at: datetime
    updated_at: datetime
    external_installation_id: Optional[str] = None
    account_type: Optional[str] = None
@dataclass
class DashboardInstanceScmConnectionsCreateOutput:
    object: str
    id: str
    url: str
    status: str
    created_at: datetime
    expires_at: datetime
    connection: Optional[DashboardInstanceScmConnectionsCreateOutputConnection] = None


class mapDashboardInstanceScmConnectionsCreateOutputConnectionExternalAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmConnectionsCreateOutputConnectionExternalAccount:
        return DashboardInstanceScmConnectionsCreateOutputConnectionExternalAccount(
        id=data.get('id'),
        login=data.get('login'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmConnectionsCreateOutputConnectionExternalAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmConnectionsCreateOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmConnectionsCreateOutputConnection:
        return DashboardInstanceScmConnectionsCreateOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        external_installation_id=data.get('external_installation_id'),
        account_type=data.get('account_type'),
        external_account=mapDashboardInstanceScmConnectionsCreateOutputConnectionExternalAccount.from_dict(data.get('external_account')) if data.get('external_account') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmConnectionsCreateOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceScmConnectionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmConnectionsCreateOutput:
        return DashboardInstanceScmConnectionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        url=data.get('url'),
        status=data.get('status'),
        connection=mapDashboardInstanceScmConnectionsCreateOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmConnectionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceScmConnectionsCreateBody:
    redirect_url: Optional[str] = None


class mapDashboardInstanceScmConnectionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceScmConnectionsCreateBody:
        return DashboardInstanceScmConnectionsCreateBody(
        redirect_url=data.get('redirect_url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceScmConnectionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

