from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class TokenGetOutputOrganization:
    object: str
    id: str
    name: str
    slug: str
@dataclass
class TokenGetOutputInstance:
    object: str
    id: str
    name: str
    slug: str
    project_id: str
@dataclass
class TokenGetOutputProject:
    object: str
    id: str
    name: str
    slug: str
@dataclass
class TokenGetOutputActor:
    object: str
    id: str
    type: str
    name: str
@dataclass
class TokenGetOutputMember:
    object: str
    id: str
    name: str
@dataclass
class TokenGetOutputUser:
    object: str
    id: str
    name: str
@dataclass
class TokenGetOutput:
    object: str
    type: str
    organization: Optional[TokenGetOutputOrganization] = None
    instance: Optional[TokenGetOutputInstance] = None
    project: Optional[TokenGetOutputProject] = None
    actor: Optional[TokenGetOutputActor] = None
    member: Optional[TokenGetOutputMember] = None
    user: Optional[TokenGetOutputUser] = None


class mapTokenGetOutputOrganization:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TokenGetOutputOrganization:
        return TokenGetOutputOrganization(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[TokenGetOutputOrganization, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapTokenGetOutputInstance:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TokenGetOutputInstance:
        return TokenGetOutputInstance(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        project_id=data.get('project_id')
        )

    @staticmethod
    def to_dict(value: Union[TokenGetOutputInstance, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapTokenGetOutputProject:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TokenGetOutputProject:
        return TokenGetOutputProject(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug')
        )

    @staticmethod
    def to_dict(value: Union[TokenGetOutputProject, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapTokenGetOutputActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TokenGetOutputActor:
        return TokenGetOutputActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[TokenGetOutputActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapTokenGetOutputMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TokenGetOutputMember:
        return TokenGetOutputMember(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[TokenGetOutputMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapTokenGetOutputUser:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TokenGetOutputUser:
        return TokenGetOutputUser(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name')
        )

    @staticmethod
    def to_dict(value: Union[TokenGetOutputUser, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapTokenGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> TokenGetOutput:
        return TokenGetOutput(
        object=data.get('object'),
        type=data.get('type'),
        organization=mapTokenGetOutputOrganization.from_dict(data.get('organization')) if data.get('organization') else None,
        instance=mapTokenGetOutputInstance.from_dict(data.get('instance')) if data.get('instance') else None,
        project=mapTokenGetOutputProject.from_dict(data.get('project')) if data.get('project') else None,
        actor=mapTokenGetOutputActor.from_dict(data.get('actor')) if data.get('actor') else None,
        member=mapTokenGetOutputMember.from_dict(data.get('member')) if data.get('member') else None,
        user=mapTokenGetOutputUser.from_dict(data.get('user')) if data.get('user') else None
        )

    @staticmethod
    def to_dict(value: Union[TokenGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

