
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

SessionsGetOutput = Union[Dict[str, Any], Dict[str, Any]]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsGetOutput:
        data

    @staticmethod
    def to_dict(value: Union[SessionsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

