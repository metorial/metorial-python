from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsExportsCreateOutput:
    object: str
    id: str
    note: str
    provider_auth_config_id: str
    value: Dict[str, Any]
    created_at: datetime
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsExportsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsExportsCreateOutput:
        return ManagementInstanceProviderDeploymentsAuthConfigsExportsCreateOutput(
        object=data.get('object'),
        id=data.get('id'),
        note=data.get('note'),
        metadata=data.get('metadata'),
        provider_auth_config_id=data.get('provider_auth_config_id'),
        value=data.get('value'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsExportsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsExportsCreateBody:
    note: str
    metadata: Optional[Dict[str, Any]] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsExportsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsExportsCreateBody:
        return ManagementInstanceProviderDeploymentsAuthConfigsExportsCreateBody(
        note=data.get('note'),
        metadata=data.get('metadata')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsExportsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
