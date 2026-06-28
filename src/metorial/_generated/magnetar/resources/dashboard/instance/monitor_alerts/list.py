from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceMonitorAlertsListOutputItemsMonitor:
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
class DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification] = None
    to_specification: Optional[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification] = None
    from_provider_version: Optional[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion] = None
    to_provider_version: Optional[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion] = None
@dataclass
class DashboardInstanceMonitorAlertsListOutputItemsRecipients:
    object: str
    id: str
    recipient_id: str
    created_at: datetime
    viewed_at: Optional[datetime] = None
@dataclass
class DashboardInstanceMonitorAlertsListOutputItemsEvents:
    object: str
    id: str
    type: str
    created_at: datetime
    actor_id: Optional[str] = None
@dataclass
class DashboardInstanceMonitorAlertsListOutputItems:
    object: str
    id: str
    status: str
    monitor: DashboardInstanceMonitorAlertsListOutputItemsMonitor
    created_at: datetime
    recipients: List[DashboardInstanceMonitorAlertsListOutputItemsRecipients]
    events: List[DashboardInstanceMonitorAlertsListOutputItemsEvents]
    proto_guard_alert_id: Optional[str] = None
    proto_guard_run_id: Optional[str] = None
    specification_change_notification: Optional[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification] = None
    resolved_at: Optional[datetime] = None
@dataclass
class DashboardInstanceMonitorAlertsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceMonitorAlertsListOutput:
    items: List[DashboardInstanceMonitorAlertsListOutputItems]
    pagination: DashboardInstanceMonitorAlertsListOutputPagination


class mapDashboardInstanceMonitorAlertsListOutputItemsMonitor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItemsMonitor:
        return DashboardInstanceMonitorAlertsListOutputItemsMonitor(
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
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItemsMonitor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
        return DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
        return DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
        return DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
        return DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification:
        return DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputItemsRecipients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItemsRecipients:
        return DashboardInstanceMonitorAlertsListOutputItemsRecipients(
        object=data.get('object'),
        id=data.get('id'),
        recipient_id=data.get('recipient_id'),
        viewed_at=datetime.fromisoformat(data.get('viewed_at').replace('Z', '+00:00')) if data.get('viewed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItemsRecipients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputItemsEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItemsEvents:
        return DashboardInstanceMonitorAlertsListOutputItemsEvents(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItemsEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputItems:
        return DashboardInstanceMonitorAlertsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        monitor=mapDashboardInstanceMonitorAlertsListOutputItemsMonitor.from_dict(data.get('monitor')) if data.get('monitor') else None,
        proto_guard_alert_id=data.get('proto_guard_alert_id'),
        proto_guard_run_id=data.get('proto_guard_run_id'),
        specification_change_notification=mapDashboardInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification.from_dict(data.get('specification_change_notification')) if data.get('specification_change_notification') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        recipients=[mapDashboardInstanceMonitorAlertsListOutputItemsRecipients.from_dict(item) for item in data.get('recipients', []) if item],
        events=[mapDashboardInstanceMonitorAlertsListOutputItemsEvents.from_dict(item) for item in data.get('events', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutputPagination:
        return DashboardInstanceMonitorAlertsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceMonitorAlertsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListOutput:
        return DashboardInstanceMonitorAlertsListOutput(
        items=[mapDashboardInstanceMonitorAlertsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceMonitorAlertsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceMonitorAlertsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceMonitorAlertsListQueryResolvedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceMonitorAlertsListQuery:
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
    created_at: Optional[DashboardInstanceMonitorAlertsListQueryCreatedAt] = None
    resolved_at: Optional[DashboardInstanceMonitorAlertsListQueryResolvedAt] = None


class mapDashboardInstanceMonitorAlertsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceMonitorAlertsListQuery:
        return DashboardInstanceMonitorAlertsListQuery(
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
        created_at=mapDashboardInstanceMonitorAlertsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        resolved_at=mapDashboardInstanceMonitorAlertsListQueryResolvedAt.from_dict(data.get('resolved_at')) if data.get('resolved_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceMonitorAlertsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

