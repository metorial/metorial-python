from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
    object: str
    schema: Optional[Dict[str, Any]] = None


class mapManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput:
        return ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput(
        object=data.get('object'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceProviderDeploymentsAuthConfigsImportsGetSchemaOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
