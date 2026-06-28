from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ProviderSpecificationChangeNotificationsGetOutputFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderSpecificationChangeNotificationsGetOutputToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderSpecificationChangeNotificationsGetOutputFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderSpecificationChangeNotificationsGetOutputToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ProviderSpecificationChangeNotificationsGetOutput:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[ProviderSpecificationChangeNotificationsGetOutputFromSpecification] = None
    to_specification: Optional[ProviderSpecificationChangeNotificationsGetOutputToSpecification] = None
    from_provider_version: Optional[ProviderSpecificationChangeNotificationsGetOutputFromProviderVersion] = None
    to_provider_version: Optional[ProviderSpecificationChangeNotificationsGetOutputToProviderVersion] = None


class mapProviderSpecificationChangeNotificationsGetOutputFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsGetOutputFromSpecification:
        return ProviderSpecificationChangeNotificationsGetOutputFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsGetOutputFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsGetOutputToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsGetOutputToSpecification:
        return ProviderSpecificationChangeNotificationsGetOutputToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsGetOutputToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsGetOutputFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsGetOutputFromProviderVersion:
        return ProviderSpecificationChangeNotificationsGetOutputFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsGetOutputFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsGetOutputToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsGetOutputToProviderVersion:
        return ProviderSpecificationChangeNotificationsGetOutputToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsGetOutputToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapProviderSpecificationChangeNotificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ProviderSpecificationChangeNotificationsGetOutput:
        return ProviderSpecificationChangeNotificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapProviderSpecificationChangeNotificationsGetOutputFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapProviderSpecificationChangeNotificationsGetOutputToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapProviderSpecificationChangeNotificationsGetOutputFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapProviderSpecificationChangeNotificationsGetOutputToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ProviderSpecificationChangeNotificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

