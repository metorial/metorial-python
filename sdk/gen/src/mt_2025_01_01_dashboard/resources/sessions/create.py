
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

SessionsCreateOutput = Union[Dict[str, Any], Dict[str, Any]]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsCreateOutput:
        data

    @staticmethod
    def to_dict(value: Union[SessionsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)


from typing import Any, Dict, List, Optional, Union
from datetime import datetime

SessionsCreateBody = Union[Dict[str, Any], Dict[str, Any]]


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSessionsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SessionsCreateBody:
        data

    @staticmethod
    def to_dict(value: Union[SessionsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

