from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderDeploymentsConfigsGetConfigSchemaOutput:
    object: str
    schema: Optional[Dict[str, Any]] = None


class mapDashboardInstanceProviderDeploymentsConfigsGetConfigSchemaOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderDeploymentsConfigsGetConfigSchemaOutput:
        return DashboardInstanceProviderDeploymentsConfigsGetConfigSchemaOutput(
        object=data.get('object'),
        schema=data.get('schema')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderDeploymentsConfigsGetConfigSchemaOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
