from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class PortalsAuthAppGetOutput:
    object: str
    id: str
    client_id: str
    default_redirect_url: str
    redirect_domains: List[str]
    email_whitelist: List[str]
    created_at: datetime
    updated_at: datetime
    slug: Optional[str] = None


class mapPortalsAuthAppGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> PortalsAuthAppGetOutput:
        return PortalsAuthAppGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        client_id=data.get('client_id'),
        slug=data.get('slug'),
        default_redirect_url=data.get('default_redirect_url'),
        redirect_domains=data.get('redirect_domains', []),
        email_whitelist=data.get('email_whitelist', []),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[PortalsAuthAppGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

