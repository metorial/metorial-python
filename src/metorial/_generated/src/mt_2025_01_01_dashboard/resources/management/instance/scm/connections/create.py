from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmConnectionsCreateOutputConnectionExternalAccount:
    id: str
    login: str
    name: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ManagementInstanceScmConnectionsCreateOutputConnection:
    object: str
    id: str
    provider: str
    external_account: ManagementInstanceScmConnectionsCreateOutputConnectionExternalAccount
    created_at: datetime
    updated_at: datetime
    external_installation_id: Optional[str] = None
    account_type: Optional[str] = None
@dataclass
class ManagementInstanceScmConnectionsCreateOutput:
    object: str
    id: str
    url: str
    status: str
    created_at: datetime
    expires_at: datetime
    connection: Optional[ManagementInstanceScmConnectionsCreateOutputConnection] = None


class mapManagementInstanceScmConnectionsCreateOutputConnectionExternalAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsCreateOutputConnectionExternalAccount:
        return ManagementInstanceScmConnectionsCreateOutputConnectionExternalAccount(
        id=data.get('id'),
        login=data.get('login'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsCreateOutputConnectionExternalAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmConnectionsCreateOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsCreateOutputConnection:
        return ManagementInstanceScmConnectionsCreateOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        external_installation_id=data.get('external_installation_id'),
        account_type=data.get('account_type'),
        external_account=mapManagementInstanceScmConnectionsCreateOutputConnectionExternalAccount.from_dict(data.get('external_account')) if data.get('external_account') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsCreateOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmConnectionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsCreateOutput:
        return ManagementInstanceScmConnectionsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        url=data.get('url'),
        status=data.get('status'),
        connection=mapManagementInstanceScmConnectionsCreateOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmConnectionsCreateBody:
    redirect_url: Optional[str] = None


class mapManagementInstanceScmConnectionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmConnectionsCreateBody:
        return ManagementInstanceScmConnectionsCreateBody(
        redirect_url=data.get('redirect_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmConnectionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

