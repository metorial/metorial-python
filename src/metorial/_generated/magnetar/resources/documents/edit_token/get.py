from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DocumentsEditTokenGetOutput:
    object: str
    token: str
    expires_at: datetime
    document_id: str


class mapDocumentsEditTokenGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DocumentsEditTokenGetOutput:
        return DocumentsEditTokenGetOutput(
        object=data.get('object'),
        token=data.get('token'),
        expires_at=datetime.fromisoformat(data.get('expires_at').replace('Z', '+00:00')) if data.get('expires_at') else None,
        document_id=data.get('document_id')
        )

    @staticmethod
    def to_dict(value: Union[DocumentsEditTokenGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

