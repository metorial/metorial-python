from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceScmInstallationCreateOutputConnectionExternalAccount:
    id: str
    login: str
    name: Optional[str] = None
    email: Optional[str] = None
    image_url: Optional[str] = None
@dataclass
class ManagementInstanceScmInstallationCreateOutputConnection:
    object: str
    id: str
    provider: str
    external_account: ManagementInstanceScmInstallationCreateOutputConnectionExternalAccount
    created_at: datetime
    updated_at: datetime
    external_installation_id: Optional[str] = None
    account_type: Optional[str] = None
@dataclass
class ManagementInstanceScmInstallationCreateOutput:
    object: str
    id: str
    url: str
    status: str
    created_at: datetime
    expires_at: datetime
    connection: Optional[ManagementInstanceScmInstallationCreateOutputConnection] = None


class mapManagementInstanceScmInstallationCreateOutputConnectionExternalAccount:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationCreateOutputConnectionExternalAccount:
        return ManagementInstanceScmInstallationCreateOutputConnectionExternalAccount(
        id=data.get('id'),
        login=data.get('login'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationCreateOutputConnectionExternalAccount, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmInstallationCreateOutputConnection:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationCreateOutputConnection:
        return ManagementInstanceScmInstallationCreateOutputConnection(
        object=data.get('object'),
        id=data.get('id'),
        provider=data.get('provider'),
        external_installation_id=data.get('external_installation_id'),
        account_type=data.get('account_type'),
        external_account=mapManagementInstanceScmInstallationCreateOutputConnectionExternalAccount.from_dict(data.get('external_account')) if data.get('external_account') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationCreateOutputConnection, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceScmInstallationCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationCreateOutput:
        return ManagementInstanceScmInstallationCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        url=data.get('url'),
        status=data.get('status'),
        connection=mapManagementInstanceScmInstallationCreateOutputConnection.from_dict(data.get('connection')) if data.get('connection') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceScmInstallationCreateBody:
    provider: Optional[str] = None
    redirect_url: Optional[str] = None


class mapManagementInstanceScmInstallationCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceScmInstallationCreateBody:
        return ManagementInstanceScmInstallationCreateBody(
        provider=data.get('provider'),
        redirect_url=data.get('redirect_url')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceScmInstallationCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

