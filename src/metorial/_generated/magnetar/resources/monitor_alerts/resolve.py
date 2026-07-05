from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MonitorAlertsResolveOutputMonitor:
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
class MonitorAlertsResolveOutputSpecificationChangeNotificationFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsResolveOutputSpecificationChangeNotificationToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsResolveOutputSpecificationChangeNotificationFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsResolveOutputSpecificationChangeNotificationToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsResolveOutputSpecificationChangeNotification:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[MonitorAlertsResolveOutputSpecificationChangeNotificationFromSpecification] = None
    to_specification: Optional[MonitorAlertsResolveOutputSpecificationChangeNotificationToSpecification] = None
    from_provider_version: Optional[MonitorAlertsResolveOutputSpecificationChangeNotificationFromProviderVersion] = None
    to_provider_version: Optional[MonitorAlertsResolveOutputSpecificationChangeNotificationToProviderVersion] = None
@dataclass
class MonitorAlertsResolveOutputRecipients:
    object: str
    id: str
    recipient_id: str
    created_at: datetime
    viewed_at: Optional[datetime] = None
@dataclass
class MonitorAlertsResolveOutputEvents:
    object: str
    id: str
    type: str
    created_at: datetime
    actor_id: Optional[str] = None
@dataclass
class MonitorAlertsResolveOutput:
    object: str
    id: str
    status: str
    monitor: MonitorAlertsResolveOutputMonitor
    created_at: datetime
    recipients: List[MonitorAlertsResolveOutputRecipients]
    events: List[MonitorAlertsResolveOutputEvents]
    proto_guard_alert_id: Optional[str] = None
    proto_guard_run_id: Optional[str] = None
    specification_change_notification: Optional[MonitorAlertsResolveOutputSpecificationChangeNotification] = None
    resolved_at: Optional[datetime] = None


class mapMonitorAlertsResolveOutputMonitor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutputMonitor:
        return MonitorAlertsResolveOutputMonitor(
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
    def to_dict(value: Union[MonitorAlertsResolveOutputMonitor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsResolveOutputSpecificationChangeNotificationFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutputSpecificationChangeNotificationFromSpecification:
        return MonitorAlertsResolveOutputSpecificationChangeNotificationFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsResolveOutputSpecificationChangeNotificationFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsResolveOutputSpecificationChangeNotificationToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutputSpecificationChangeNotificationToSpecification:
        return MonitorAlertsResolveOutputSpecificationChangeNotificationToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsResolveOutputSpecificationChangeNotificationToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsResolveOutputSpecificationChangeNotificationFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutputSpecificationChangeNotificationFromProviderVersion:
        return MonitorAlertsResolveOutputSpecificationChangeNotificationFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsResolveOutputSpecificationChangeNotificationFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsResolveOutputSpecificationChangeNotificationToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutputSpecificationChangeNotificationToProviderVersion:
        return MonitorAlertsResolveOutputSpecificationChangeNotificationToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsResolveOutputSpecificationChangeNotificationToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsResolveOutputSpecificationChangeNotification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutputSpecificationChangeNotification:
        return MonitorAlertsResolveOutputSpecificationChangeNotification(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapMonitorAlertsResolveOutputSpecificationChangeNotificationFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapMonitorAlertsResolveOutputSpecificationChangeNotificationToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapMonitorAlertsResolveOutputSpecificationChangeNotificationFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapMonitorAlertsResolveOutputSpecificationChangeNotificationToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsResolveOutputSpecificationChangeNotification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsResolveOutputRecipients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutputRecipients:
        return MonitorAlertsResolveOutputRecipients(
        object=data.get('object'),
        id=data.get('id'),
        recipient_id=data.get('recipient_id'),
        viewed_at=datetime.fromisoformat(data.get('viewed_at').replace('Z', '+00:00')) if data.get('viewed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsResolveOutputRecipients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsResolveOutputEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutputEvents:
        return MonitorAlertsResolveOutputEvents(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsResolveOutputEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsResolveOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsResolveOutput:
        return MonitorAlertsResolveOutput(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        monitor=mapMonitorAlertsResolveOutputMonitor.from_dict(data.get('monitor')) if data.get('monitor') else None,
        proto_guard_alert_id=data.get('proto_guard_alert_id'),
        proto_guard_run_id=data.get('proto_guard_run_id'),
        specification_change_notification=mapMonitorAlertsResolveOutputSpecificationChangeNotification.from_dict(data.get('specification_change_notification')) if data.get('specification_change_notification') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        recipients=[mapMonitorAlertsResolveOutputRecipients.from_dict(item) for item in data.get('recipients', []) if item],
        events=[mapMonitorAlertsResolveOutputEvents.from_dict(item) for item in data.get('events', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsResolveOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

