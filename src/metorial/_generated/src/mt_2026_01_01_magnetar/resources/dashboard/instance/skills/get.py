from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsGetOutputHierarchyCreatorConsumer] = None
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyForkCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyForkCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsGetOutputHierarchyForkCreatorConsumer] = None
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActor] = None
    consumer: Optional[DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorConsumer] = None
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyFork:
    id: str
    parent_skill_id: str
    created_at: datetime
    creator: Optional[DashboardInstanceSkillsGetOutputHierarchyForkCreator] = None
    original_creator: Optional[DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreator] = None
@dataclass
class DashboardInstanceSkillsGetOutputHierarchyEntity:
    object: str
    id: str
    name: str
    slug: str
    parent_skill_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGetOutputHierarchy:
    object: str
    type: str
    entity: DashboardInstanceSkillsGetOutputHierarchyEntity
    parent_skill_id: Optional[str] = None
    creator: Optional[DashboardInstanceSkillsGetOutputHierarchyCreator] = None
    fork: Optional[DashboardInstanceSkillsGetOutputHierarchyFork] = None
@dataclass
class DashboardInstanceSkillsGetOutputIntegrationsConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class DashboardInstanceSkillsGetOutputIntegrations:
    object: str
    id: str
    slug: str
    name: str
    configuration: DashboardInstanceSkillsGetOutputIntegrationsConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class DashboardInstanceSkillsGetOutputProviders:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class DashboardInstanceSkillsGetOutput:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    client_name: str
    metadata: Dict[str, Any]
    store_id: str
    hierarchy: DashboardInstanceSkillsGetOutputHierarchy
    integrations: List[DashboardInstanceSkillsGetOutputIntegrations]
    providers: List[DashboardInstanceSkillsGetOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None


class mapDashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActorTeams:
        return DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActor:
        return DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyCreatorConsumer:
        return DashboardInstanceSkillsGetOutputHierarchyCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyCreator:
        return DashboardInstanceSkillsGetOutputHierarchyCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsGetOutputHierarchyCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsGetOutputHierarchyCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActorTeams:
        return DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActor:
        return DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyForkCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyForkCreatorConsumer:
        return DashboardInstanceSkillsGetOutputHierarchyForkCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyForkCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyForkCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyForkCreator:
        return DashboardInstanceSkillsGetOutputHierarchyForkCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsGetOutputHierarchyForkCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsGetOutputHierarchyForkCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyForkCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
        return DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActor:
        return DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapDashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorConsumer:
        return DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyForkOriginalCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreator:
        return DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapDashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapDashboardInstanceSkillsGetOutputHierarchyForkOriginalCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyForkOriginalCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyFork:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyFork:
        return DashboardInstanceSkillsGetOutputHierarchyFork(
        id=data.get('id'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapDashboardInstanceSkillsGetOutputHierarchyForkCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        original_creator=mapDashboardInstanceSkillsGetOutputHierarchyForkOriginalCreator.from_dict(data.get('original_creator')) if data.get('original_creator') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyFork, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchyEntity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchyEntity:
        return DashboardInstanceSkillsGetOutputHierarchyEntity(
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
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchyEntity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputHierarchy:
        return DashboardInstanceSkillsGetOutputHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapDashboardInstanceSkillsGetOutputHierarchyCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        fork=mapDashboardInstanceSkillsGetOutputHierarchyFork.from_dict(data.get('fork')) if data.get('fork') else None,
        entity=mapDashboardInstanceSkillsGetOutputHierarchyEntity.from_dict(data.get('entity')) if data.get('entity') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputIntegrationsConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputIntegrationsConfiguration:
        return DashboardInstanceSkillsGetOutputIntegrationsConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputIntegrationsConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputIntegrations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputIntegrations:
        return DashboardInstanceSkillsGetOutputIntegrations(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapDashboardInstanceSkillsGetOutputIntegrationsConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputIntegrations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutputProviders:
        return DashboardInstanceSkillsGetOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapDashboardInstanceSkillsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSkillsGetOutput:
        return DashboardInstanceSkillsGetOutput(
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
        hierarchy=mapDashboardInstanceSkillsGetOutputHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        integrations=[mapDashboardInstanceSkillsGetOutputIntegrations.from_dict(item) for item in data.get('integrations', []) if item],
        providers=[mapDashboardInstanceSkillsGetOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSkillsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

