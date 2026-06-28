from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceCustomProvidersVersionsGetEnvOutput:
    object: str
    env: Optional[Dict[str, Any]] = None


class mapDashboardInstanceCustomProvidersVersionsGetEnvOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceCustomProvidersVersionsGetEnvOutput:
        return DashboardInstanceCustomProvidersVersionsGetEnvOutput(
        object=data.get('object'),
        env=data.get('env')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceCustomProvidersVersionsGetEnvOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

