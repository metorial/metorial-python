from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceMonitorAlertsListOutputItemsMonitor:
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
class ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
    object: str
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
    object: str
    id: str
    version: str
    name: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification:
    object: str
    id: str
    provider_id: str
    provider_version_id: str
    created_at: datetime
    from_specification: Optional[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification] = None
    to_specification: Optional[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification] = None
    from_provider_version: Optional[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion] = None
    to_provider_version: Optional[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion] = None
@dataclass
class ManagementInstanceMonitorAlertsListOutputItemsRecipients:
    object: str
    id: str
    recipient_id: str
    created_at: datetime
    viewed_at: Optional[datetime] = None
@dataclass
class ManagementInstanceMonitorAlertsListOutputItemsEvents:
    object: str
    id: str
    type: str
    created_at: datetime
    actor_id: Optional[str] = None
@dataclass
class ManagementInstanceMonitorAlertsListOutputItems:
    object: str
    id: str
    status: str
    monitor: ManagementInstanceMonitorAlertsListOutputItemsMonitor
    created_at: datetime
    recipients: List[ManagementInstanceMonitorAlertsListOutputItemsRecipients]
    events: List[ManagementInstanceMonitorAlertsListOutputItemsEvents]
    proto_guard_alert_id: Optional[str] = None
    proto_guard_run_id: Optional[str] = None
    specification_change_notification: Optional[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification] = None
    resolved_at: Optional[datetime] = None
@dataclass
class ManagementInstanceMonitorAlertsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class ManagementInstanceMonitorAlertsListOutput:
    items: List[ManagementInstanceMonitorAlertsListOutputItems]
    pagination: ManagementInstanceMonitorAlertsListOutputPagination


class mapManagementInstanceMonitorAlertsListOutputItemsMonitor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItemsMonitor:
        return ManagementInstanceMonitorAlertsListOutputItemsMonitor(
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
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItemsMonitor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification:
        return ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification:
        return ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion:
        return ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion:
        return ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion(
        object=data.get('object'),
        id=data.get('id'),
        version=data.get('version'),
        name=data.get('name'),
        description=data.get('description'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification:
        return ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification(
        object=data.get('object'),
        id=data.get('id'),
        provider_id=data.get('provider_id'),
        provider_version_id=data.get('provider_version_id'),
        from_specification=mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromSpecification.from_dict(data.get('from_specification')) if data.get('from_specification') else None,
        to_specification=mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToSpecification.from_dict(data.get('to_specification')) if data.get('to_specification') else None,
        from_provider_version=mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationFromProviderVersion.from_dict(data.get('from_provider_version')) if data.get('from_provider_version') else None,
        to_provider_version=mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotificationToProviderVersion.from_dict(data.get('to_provider_version')) if data.get('to_provider_version') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputItemsRecipients:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItemsRecipients:
        return ManagementInstanceMonitorAlertsListOutputItemsRecipients(
        object=data.get('object'),
        id=data.get('id'),
        recipient_id=data.get('recipient_id'),
        viewed_at=datetime.fromisoformat(data.get('viewed_at').replace('Z', '+00:00')) if data.get('viewed_at') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItemsRecipients, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputItemsEvents:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItemsEvents:
        return ManagementInstanceMonitorAlertsListOutputItemsEvents(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        actor_id=data.get('actor_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItemsEvents, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputItems:
        return ManagementInstanceMonitorAlertsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        monitor=mapManagementInstanceMonitorAlertsListOutputItemsMonitor.from_dict(data.get('monitor')) if data.get('monitor') else None,
        proto_guard_alert_id=data.get('proto_guard_alert_id'),
        proto_guard_run_id=data.get('proto_guard_run_id'),
        specification_change_notification=mapManagementInstanceMonitorAlertsListOutputItemsSpecificationChangeNotification.from_dict(data.get('specification_change_notification')) if data.get('specification_change_notification') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        resolved_at=datetime.fromisoformat(data.get('resolved_at').replace('Z', '+00:00')) if data.get('resolved_at') else None,
        recipients=[mapManagementInstanceMonitorAlertsListOutputItemsRecipients.from_dict(item) for item in data.get('recipients', []) if item],
        events=[mapManagementInstanceMonitorAlertsListOutputItemsEvents.from_dict(item) for item in data.get('events', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutputPagination:
        return ManagementInstanceMonitorAlertsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceMonitorAlertsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListOutput:
        return ManagementInstanceMonitorAlertsListOutput(
        items=[mapManagementInstanceMonitorAlertsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapManagementInstanceMonitorAlertsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceMonitorAlertsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceMonitorAlertsListQueryResolvedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class ManagementInstanceMonitorAlertsListQuery:
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
    created_at: Optional[ManagementInstanceMonitorAlertsListQueryCreatedAt] = None
    resolved_at: Optional[ManagementInstanceMonitorAlertsListQueryResolvedAt] = None


class mapManagementInstanceMonitorAlertsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceMonitorAlertsListQuery:
        return ManagementInstanceMonitorAlertsListQuery(
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
        created_at=mapManagementInstanceMonitorAlertsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        resolved_at=mapManagementInstanceMonitorAlertsListQueryResolvedAt.from_dict(data.get('resolved_at')) if data.get('resolved_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceMonitorAlertsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

