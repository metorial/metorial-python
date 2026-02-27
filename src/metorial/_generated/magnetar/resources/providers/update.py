from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProvidersUpdateOutputPublisher:
    object: str
    id: str
    name: str
    slug: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProvidersUpdateOutputCurrentVersion:
    object: str
    id: str
    version: str
    status: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ProvidersUpdateOutput:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    publisher: Optional[ProvidersUpdateOutputPublisher] = None
    current_version: Optional[ProvidersUpdateOutputCurrentVersion] = None


class mapProvidersUpdateOutputPublisher:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersUpdateOutputPublisher:
        return ProvidersUpdateOutputPublisher(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersUpdateOutputPublisher, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersUpdateOutputCurrentVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersUpdateOutputCurrentVersion:
        return ProvidersUpdateOutputCurrentVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        status=data.get('status'),
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersUpdateOutputCurrentVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProvidersUpdateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersUpdateOutput:
        return ProvidersUpdateOutput(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        publisher=mapProvidersUpdateOutputPublisher.from_dict(data.get('publisher')) if data.get('publisher') else None,
        current_version=mapProvidersUpdateOutputCurrentVersion.from_dict(data.get('current_version')) if data.get('current_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProvidersUpdateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ProvidersUpdateBody:
    name: Optional[str] = None
    description: Optional[str] = None
    slug: Optional[str] = None
    image: Optional[str] = None
    skills: Optional[List[str]] = None


class mapProvidersUpdateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProvidersUpdateBody:
        return ProvidersUpdateBody(
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        image=data.get('image'),
        skills=data.get('skills', [])
        )

    @staticmethod
    def to_dict(value: Union[ProvidersUpdateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)
