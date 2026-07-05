from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsListOutputItemsHierarchyCreatorConsumer] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyForkCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorConsumer] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorConsumer] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyFork:
    id: str
    parent_skill_id: str
    created_at: datetime
    creator: Optional[DashboardInstanceSkillsListOutputItemsHierarchyForkCreator] = None
    original_creator: Optional[DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreator] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchyEntity:
    object: str
    id: str
    name: str
    slug: str
    parent_skill_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsHierarchy:
    object: str
    type: str
    entity: DashboardInstanceSkillsListOutputItemsHierarchyEntity
    parent_skill_id: Optional[str] = None
    creator: Optional[DashboardInstanceSkillsListOutputItemsHierarchyCreator] = None
    fork: Optional[DashboardInstanceSkillsListOutputItemsHierarchyFork] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsIntegrationsConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsIntegrations:
    object: str
    id: str
    slug: str
    name: str
    configuration: DashboardInstanceSkillsListOutputItemsIntegrationsConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsListOutputItemsProviders:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsListOutputItems:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    client_name: str
    metadata: Dict[str, Any]
    store_id: str
    hierarchy: DashboardInstanceSkillsListOutputItemsHierarchy
    integrations: List[DashboardInstanceSkillsListOutputItemsIntegrations]
    providers: List[DashboardInstanceSkillsListOutputItemsProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
@dataclass
class DashboardInstanceSkillsListOutputPagination:
    has_more_before: bool
    has_more_after: bool
@dataclass
class DashboardInstanceSkillsListOutput:
    items: List[DashboardInstanceSkillsListOutputItems]
    pagination: DashboardInstanceSkillsListOutputPagination


class mapDashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActorTeams:
        return DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActor:
        return DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyCreatorConsumer:
        return DashboardInstanceSkillsListOutputItemsHierarchyCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyCreator:
        return DashboardInstanceSkillsListOutputItemsHierarchyCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsListOutputItemsHierarchyCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsListOutputItemsHierarchyCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActorTeams:
        return DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActor:
        return DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyForkCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorConsumer:
        return DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyForkCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyForkCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyForkCreator:
        return DashboardInstanceSkillsListOutputItemsHierarchyForkCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsListOutputItemsHierarchyForkCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsListOutputItemsHierarchyForkCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyForkCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActorTeams:
        return DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActor:
        return DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorConsumer:
        return DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreator:
        return DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyFork:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyFork:
        return DashboardInstanceSkillsListOutputItemsHierarchyFork(
        id=data.get('id'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapDashboardInstanceSkillsListOutputItemsHierarchyForkCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        original_creator=mapDashboardInstanceSkillsListOutputItemsHierarchyForkOriginalCreator.from_dict(data.get('original_creator')) if data.get('original_creator') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyFork, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchyEntity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchyEntity:
        return DashboardInstanceSkillsListOutputItemsHierarchyEntity(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        description=data.get('description'),
        parent_skill_id=data.get('parent_skill_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchyEntity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsHierarchy:
        return DashboardInstanceSkillsListOutputItemsHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapDashboardInstanceSkillsListOutputItemsHierarchyCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        fork=mapDashboardInstanceSkillsListOutputItemsHierarchyFork.from_dict(data.get('fork')) if data.get('fork') else None,
        entity=mapDashboardInstanceSkillsListOutputItemsHierarchyEntity.from_dict(data.get('entity')) if data.get('entity') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsIntegrationsConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsIntegrationsConfiguration:
        return DashboardInstanceSkillsListOutputItemsIntegrationsConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsIntegrationsConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsIntegrations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsIntegrations:
        return DashboardInstanceSkillsListOutputItemsIntegrations(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapDashboardInstanceSkillsListOutputItemsIntegrationsConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsIntegrations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItemsProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItemsProviders:
        return DashboardInstanceSkillsListOutputItemsProviders(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItemsProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputItems:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputItems:
        return DashboardInstanceSkillsListOutputItems(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        image_url=data.get('image_url'),
        client_name=data.get('client_name'),
        client_description=data.get('client_description'),
        client_metadata=data.get('client_metadata'),
        license=data.get('license'),
        compatibility=data.get('compatibility'),
        metadata=data.get('metadata'),
        store_id=data.get('store_id'),
        hierarchy=mapDashboardInstanceSkillsListOutputItemsHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        integrations=[mapDashboardInstanceSkillsListOutputItemsIntegrations.from_dict(item) for item in data.get('integrations', []) if item],
        providers=[mapDashboardInstanceSkillsListOutputItemsProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputItems, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutputPagination:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutputPagination:
        return DashboardInstanceSkillsListOutputPagination(
        has_more_before=data.get('has_more_before'),
        has_more_after=data.get('has_more_after')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutputPagination, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsListOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListOutput:
        return DashboardInstanceSkillsListOutput(
        items=[mapDashboardInstanceSkillsListOutputItems.from_dict(item) for item in data.get('items', []) if item],
        pagination=mapDashboardInstanceSkillsListOutputPagination.from_dict(data.get('pagination')) if data.get('pagination') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSkillsListQueryCreatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsListQueryUpdatedAt:
    gt: Optional[datetime] = None
    lt: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsListQuery:
    limit: Optional[float] = None
    after: Optional[str] = None
    before: Optional[str] = None
    cursor: Optional[str] = None
    order: Optional[str] = None
    search: Optional[str] = None
    status: Optional[Union[str, List[str]]] = None
    id: Optional[Union[str, List[str]]] = None
    skill_group_id: Optional[Union[str, List[str]]] = None
    integration_id: Optional[Union[str, List[str]]] = None
    provider_id: Optional[Union[str, List[str]]] = None
    created_at: Optional[DashboardInstanceSkillsListQueryCreatedAt] = None
    updated_at: Optional[DashboardInstanceSkillsListQueryUpdatedAt] = None


class mapDashboardInstanceSkillsListQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsListQuery:
        return DashboardInstanceSkillsListQuery(
        limit=data.get('limit'),
        after=data.get('after'),
        before=data.get('before'),
        cursor=data.get('cursor'),
        order=data.get('order'),
        search=data.get('search'),
        status=data.get('status'),
        id=data.get('id'),
        skill_group_id=data.get('skill_group_id'),
        integration_id=data.get('integration_id'),
        provider_id=data.get('provider_id'),
        created_at=mapDashboardInstanceSkillsListQueryCreatedAt.from_dict(data.get('created_at')) if data.get('created_at') else None,
        updated_at=mapDashboardInstanceSkillsListQueryUpdatedAt.from_dict(data.get('updated_at')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsListQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

