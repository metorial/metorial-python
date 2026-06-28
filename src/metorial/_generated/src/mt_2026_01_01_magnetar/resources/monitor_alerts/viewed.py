from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MonitorAlertsViewedOutputMonitor:
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
class MonitorAlertsViewedOutputSpecificationChangeNotificationFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsViewedOutputSpecificationChangeNotificationToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsViewedOutputSpecificationChangeNotificationFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsViewedOutputSpecificationChangeNotificationToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsViewedOutputSpecificationChangeNotification:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[MonitorAlertsViewedOutputSpecificationChangeNotificationFromSpecification] = None
    to_specification: Optional[MonitorAlertsViewedOutputSpecificationChangeNotificationToSpecification] = None
    from_provider_version: Optional[MonitorAlertsViewedOutputSpecificationChangeNotificationFromProviderVersion] = None
    to_provider_version: Optional[MonitorAlertsViewedOutputSpecificationChangeNotificationToProviderVersion] = None
@dataclass
class MonitorAlertsViewedOutputRecipients:
    object: str
    id: str
    recipient_id: str
    created_at: datetime
    viewed_at: Optional[datetime] = None
@dataclass
class MonitorAlertsViewedOutputEvents:
    object: str
    id: str
    type: str
    created_at: datetime
    actor_id: Optional[str] = None
@dataclass
class MonitorAlertsViewedOutput:
    object: str
    id: str
    status: str
    monitor: MonitorAlertsViewedOutputMonitor
    created_at: datetime
    recipients: List[MonitorAlertsViewedOutputRecipients]
    events: List[MonitorAlertsViewedOutputEvents]
    proto_guard_alert_id: Optional[str] = None
    proto_guard_run_id: Optional[str] = None
    specification_change_notification: Optional[MonitorAlertsViewedOutputSpecificationChangeNotification] = None
    resolved_at: Optional[datetime] = None


class mapMonitorAlertsViewedOutputMonitor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutputMonitor:
        return MonitorAlertsViewedOutputMonitor(
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
    def to_dict(value: Union[MonitorAlertsViewedOutputMonitor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsViewedOutputSpecificationChangeNotificationFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutputSpecificationChangeNotificationFromSpecification:
        return MonitorAlertsViewedOutputSpecificationChangeNotificationFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsViewedOutputSpecificationChangeNotificationFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsViewedOutputSpecificationChangeNotificationToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutputSpecificationChangeNotificationToSpecification:
        return MonitorAlertsViewedOutputSpecificationChangeNotificationToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsViewedOutputSpecificationChangeNotificationToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsViewedOutputSpecificationChangeNotificationFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutputSpecificationChangeNotificationFromProviderVersion:
        return MonitorAlertsViewedOutputSpecificationChangeNotificationFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsViewedOutputSpecificationChangeNotificationFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsViewedOutputSpecificationChangeNotificationToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutputSpecificationChangeNotificationToProviderVersion:
        return MonitorAlertsViewedOutputSpecificationChangeNotificationToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsViewedOutputSpecificationChangeNotificationToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsViewedOutputSpecificationChangeNotification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutputSpecificationChangeNotification:
        return MonitorAlertsViewedOutputSpecificationChangeNotification(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapMonitorAlertsViewedOutputSpecificationChangeNotificationFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapMonitorAlertsViewedOutputSpecificationChangeNotificationToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapMonitorAlertsViewedOutputSpecificationChangeNotificationFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapMonitorAlertsViewedOutputSpecificationChangeNotificationToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsViewedOutputSpecificationChangeNotification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsViewedOutputRecipients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutputRecipients:
        return MonitorAlertsViewedOutputRecipients(
        object=data.get('object'),
        id=data.get('id'),
        recipient_id=data.get('recipient_id'),
        viewed_at=datetime.fromisoformat(data.get('viewed_at').replace('Z', '+00:00')) if data.get('viewed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsViewedOutputRecipients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsViewedOutputEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutputEvents:
        return MonitorAlertsViewedOutputEvents(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsViewedOutputEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsViewedOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsViewedOutput:
        return MonitorAlertsViewedOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        monitor=mapMonitorAlertsViewedOutputMonitor.from_dict(data.get('monitor')) if data.get('monitor') else None,
        proto_guard_alert_id=data.get('proto_guard_alert_id'),
        proto_guard_run_id=data.get('proto_guard_run_id'),
        specification_change_notification=mapMonitorAlertsViewedOutputSpecificationChangeNotification.from_dict(data.get('specification_change_notification')) if data.get('specification_change_notification') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        recipients=[mapMonitorAlertsViewedOutputRecipients.from_dict(item) for item in data.get('recipients', []) if item],
        events=[mapMonitorAlertsViewedOutputEvents.from_dict(item) for item in data.get('events', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsViewedOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

