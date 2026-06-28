from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class MonitorAlertsListOutputItemsMonitor:
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
class MonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class MonitorAlertsListOutputItemsSpecificationChangeNotification:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[MonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification] = None
    to_specification: Optional[MonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification] = None
    from_provider_version: Optional[MonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion] = None
    to_provider_version: Optional[MonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion] = None
@dataclass
class MonitorAlertsListOutputItemsRecipients:
    object: str
    id: str
    recipient_id: str
    created_at: datetime
    viewed_at: Optional[datetime] = None
@dataclass
class MonitorAlertsListOutputItemsEvents:
    object: str
    id: str
    type: str
    created_at: datetime
    actor_id: Optional[str] = None
@dataclass
class MonitorAlertsListOutputItems:
    object: str
    id: str
    status: str
    monitor: MonitorAlertsListOutputItemsMonitor
    created_at: datetime
    recipients: List[MonitorAlertsListOutputItemsRecipients]
    events: List[MonitorAlertsListOutputItemsEvents]
    proto_guard_alert_id: Optional[str] = None
    proto_guard_run_id: Optional[str] = None
    specification_change_notification: Optional[MonitorAlertsListOutputItemsSpecificationChangeNotification] = None
    resolved_at: Optional[datetime] = None
@dataclass
class MonitorAlertsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class MonitorAlertsListOutput:
    items: List[MonitorAlertsListOutputItems]
    pagination: MonitorAlertsListOutputPagination


class mapMonitorAlertsListOutputItemsMonitor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItemsMonitor:
        return MonitorAlertsListOutputItemsMonitor(
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
    def to_dict(value: Union[MonitorAlertsListOutputItemsMonitor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
        return MonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
        return MonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
        return MonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
        return MonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputItemsSpecificationChangeNotification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItemsSpecificationChangeNotification:
        return MonitorAlertsListOutputItemsSpecificationChangeNotification(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputItemsSpecificationChangeNotification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputItemsRecipients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItemsRecipients:
        return MonitorAlertsListOutputItemsRecipients(
        object=data.get('object'),
        id=data.get('id'),
        recipient_id=data.get('recipient_id'),
        viewed_at=datetime.fromisoformat(data.get('viewed_at').replace('Z', '+00:00')) if data.get('viewed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputItemsRecipients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputItemsEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItemsEvents:
        return MonitorAlertsListOutputItemsEvents(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputItemsEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputItems:
        return MonitorAlertsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        monitor=mapMonitorAlertsListOutputItemsMonitor.from_dict(data.get('monitor')) if data.get('monitor') else None,
        proto_guard_alert_id=data.get('proto_guard_alert_id'),
        proto_guard_run_id=data.get('proto_guard_run_id'),
        specification_change_notification=mapMonitorAlertsListOutputItemsSpecificationChangeNotification.from_dict(data.get('specification_change_notification')) if data.get('specification_change_notification') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        recipients=[mapMonitorAlertsListOutputItemsRecipients.from_dict(item) for item in data.get('recipients', []) if item],
        events=[mapMonitorAlertsListOutputItemsEvents.from_dict(item) for item in data.get('events', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutputPagination:
        return MonitorAlertsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapMonitorAlertsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListOutput:
        return MonitorAlertsListOutput(
        items=[mapMonitorAlertsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapMonitorAlertsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class MonitorAlertsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class MonitorAlertsListQueryResolvedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class MonitorAlertsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    id: Optional[Union[str, List[str]]] = None
    monitor_id: Optional[Union[str, List[str]]] = None
    status: Optional[Union[str, List[str]]] = None
    target: Optional[Union[str, List[str]]] = None
    source: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    proto_guard_alert_id: Optional[Union[str, List[str]]] = None
    proto_guard_run_id: Optional[Union[str, List[str]]] = None
    proto_guard_filter_id: Optional[Union[str, List[str]]] = None
    specification_change_notification_id: Optional[Union[str, List[str]]] = None
    session_id: Optional[Union[str, List[str]]] = None
    session_message_id: Optional[Union[str, List[str]]] = None
    session_connection_id: Optional[Union[str, List[str]]] = None
    provider_run_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[MonitorAlertsListQueryCreatedAt] = None
    resolved_at: Optional[MonitorAlertsListQueryResolvedAt] = None


class mapMonitorAlertsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> MonitorAlertsListQuery:
        return MonitorAlertsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        id=data.get('id'),
        monitor_id=data.get('monitor_id'),
        status=data.get('status'),
        target=data.get('target'),
        source=data.get('source'),
        provider_id=data.get('provider_id'),
        proto_guard_alert_id=data.get('proto_guard_alert_id'),
        proto_guard_run_id=data.get('proto_guard_run_id'),
        proto_guard_filter_id=data.get('proto_guard_filter_id'),
        specification_change_notification_id=data.get('specification_change_notification_id'),
        session_id=data.get('session_id'),
        session_message_id=data.get('session_message_id'),
        session_connection_id=data.get('session_connection_id'),
        provider_run_id=data.get('provider_run_id'),
        created_at=mapMonitorAlertsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        resolved_at=mapMonitorAlertsListQueryResolvedAt.from_dict(data.get('resolved_at')) if data.get('resolved_at') else None
        )

    @staticmethod
    def to_dict(value: Union[MonitorAlertsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

