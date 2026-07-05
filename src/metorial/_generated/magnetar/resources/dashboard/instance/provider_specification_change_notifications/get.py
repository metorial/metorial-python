from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceProviderSpecificationChangeNotificationsGetOutput:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromSpecification] = None
    to_specification: Optional[DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToSpecification] = None
    from_provider_version: Optional[DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromProviderVersion] = None
    to_provider_version: Optional[DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToProviderVersion] = None


class mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromSpecification:
        return DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutputToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToSpecification:
        return DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromProviderVersion:
        return DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutputToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToProviderVersion:
        return DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderSpecificationChangeNotificationsGetOutputToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceProviderSpecificationChangeNotificationsGetOutput:
        return DashboardInstanceProviderSpecificationChangeNotificationsGetOutput(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutputToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutputFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapDashboardInstanceProviderSpecificationChangeNotificationsGetOutputToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceProviderSpecificationChangeNotificationsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

