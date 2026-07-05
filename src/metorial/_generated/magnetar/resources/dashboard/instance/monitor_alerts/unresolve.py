from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutputMonitor:
    object: str
    id: str
    name: str
    target: str
    status: str
    owner: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    proto_guard_filter_id: Optional[str] = None
    provider_id: Optional[str] = None
    first_alert_at: Optional[datetime] = None
    last_alert_at: Optional[datetime] = None
@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotification:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromSpecification] = None
    to_specification: Optional[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToSpecification] = None
    from_provider_version: Optional[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromProviderVersion] = None
    to_provider_version: Optional[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToProviderVersion] = None
@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutputRecipients:
    object: str
    id: str
    recipient_id: str
    created_at: datetime
    viewed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutputEvents:
    object: str
    id: str
    type: str
    created_at: datetime
    actor_id: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsUnresolveOutput:
    object: str
    id: str
    status: str
    monitor: DashboardInstanceMonitorAlertsUnresolveOutputMonitor
    created_at: datetime
    recipients: List[DashboardInstanceMonitorAlertsUnresolveOutputRecipients]
    events: List[DashboardInstanceMonitorAlertsUnresolveOutputEvents]
    proto_guard_alert_id: Optional[str] = None
    proto_guard_run_id: Optional[str] = None
    specification_change_notification: Optional[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotification] = None
    resolved_at: Optional[datetime] = None


class mapDashboardInstanceMonitorAlertsUnresolveOutputMonitor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutputMonitor:
        return DashboardInstanceMonitorAlertsUnresolveOutputMonitor(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        target=data.get('target'),
        status=data.get('status'),
        owner=data.get('owner'),
        proto_guard_filter_id=data.get('proto_guard_filter_id'),
        provider_id=data.get('provider_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        first_alert_at=datetime.fromisoformat(data.get('first_alert_at').replace('Z', '+00:00')) if data.get('first_alert_at') else None,
        last_alert_at=datetime.fromisoformat(data.get('last_alert_at').replace('Z', '+00:00')) if data.get('last_alert_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutputMonitor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromSpecification:
        return DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToSpecification:
        return DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromProviderVersion:
        return DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToProviderVersion:
        return DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotification:
        return DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotification(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotificationToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsUnresolveOutputRecipients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutputRecipients:
        return DashboardInstanceMonitorAlertsUnresolveOutputRecipients(
        object=data.get('object'),
        id=data.get('id'),
        recipient_id=data.get('recipient_id'),
        viewed_at=datetime.fromisoformat(data.get('viewed_at').replace('Z', '+00:00')) if data.get('viewed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutputRecipients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsUnresolveOutputEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutputEvents:
        return DashboardInstanceMonitorAlertsUnresolveOutputEvents(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutputEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsUnresolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsUnresolveOutput:
        return DashboardInstanceMonitorAlertsUnresolveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        monitor=mapDashboardInstanceMonitorAlertsUnresolveOutputMonitor.from_dict(data.get('monitor')) if data.get('monitor') else None,
        proto_guard_alert_id=data.get('proto_guard_alert_id'),
        proto_guard_run_id=data.get('proto_guard_run_id'),
        specification_change_notification=mapDashboardInstanceMonitorAlertsUnresolveOutputSpecificationChangeNotification.from_dict(data.get('specification_change_notification')) if data.get('specification_change_notification') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        recipients=[mapDashboardInstanceMonitorAlertsUnresolveOutputRecipients.from_dict(item) for item in data.get('recipients', []) if item],
        events=[mapDashboardInstanceMonitorAlertsUnresolveOutputEvents.from_dict(item) for item in data.get('events', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsUnresolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

