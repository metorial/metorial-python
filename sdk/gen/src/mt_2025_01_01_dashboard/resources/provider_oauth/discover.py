from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthDiscoverOutput:
    object: str
    id: str
    provider_name: str
    provider_url: str
    config: Dict[str, Any]
    created_at: datetime
    refreshed_at: datetime


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthDiscoverOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthDiscoverOutput:
        return ProviderOauthDiscoverOutput(
        object=data.get('object'),
        id=data.get('id'),
        provider_name=data.get('provider_name'),
        provider_url=data.get('provider_url'),
        config=data.get('config'),
        created_at=data.get('created_at') and datetime.fromisoformat(data.get('created_at')),
        refreshed_at=data.get('refreshed_at') and datetime.fromisoformat(data.get('refreshed_at'))
        )

    @staticmethod
    def to_dict(value: Union[ProviderOauthDiscoverOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime

@dataclass
class ProviderOauthDiscoverBody:
    discovery_url: str


from typing import Any, Dict, Optional, Union
from datetime import datetime
import dataclasses

class mapProviderOauthDiscoverBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderOauthDiscoverBody:
        return ProviderOauthDiscoverBody(
        discovery_url=data.get('discovery_url')
        )

    @staticmethod
    def to_dict(value: Union[ProviderOauthDiscoverBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

