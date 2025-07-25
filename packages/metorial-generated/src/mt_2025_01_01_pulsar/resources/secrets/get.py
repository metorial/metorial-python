from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class SecretsGetOutput:
    object: str
    id: str
    status: str
    type: Dict[str, Any]
    description: str
    metadata: Dict[str, Any]
    organization_id: str
    instance_id: str
    fingerprint: str
    created_at: datetime
    last_used_at: Optional[datetime] = None


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapSecretsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SecretsGetOutput:
        return SecretsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        type=data.get('type') and {
            "identifier": data.get('type', {}).get('identifier'),
            "name": data.get('type', {}).get('name')
        },
        description=data.get('description'),
        metadata=data.get('metadata'),
        organization_id=data.get('organization_id'),
        instance_id=data.get('instance_id'),
        fingerprint=data.get('fingerprint'),
        last_used_at=data.get('last_used_at') and datetime.fromisoformat(data.get('last_used_at')),
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at'))
        )

    @staticmethod
    def to_dict(value: Union[SecretsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

