from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstancePortalsAuthSsoTenantsSetupOutput:
    object: str
    url: str


class mapDashboardInstancePortalsAuthSsoTenantsSetupOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstancePortalsAuthSsoTenantsSetupOutput:
        return DashboardInstancePortalsAuthSsoTenantsSetupOutput(
        object=data.get('object'),
        url=data.get('url')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstancePortalsAuthSsoTenantsSetupOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

