from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsCreateOutputHierarchyCreatorConsumer] = None
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyForkCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyForkCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsCreateOutputHierarchyForkCreatorConsumer] = None
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorConsumer] = None
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyFork:
    id: str
    parent_skill_id: str
    created_at: datetime
    creator: Optional[ManagementInstanceSkillsCreateOutputHierarchyForkCreator] = None
    original_creator: Optional[ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreator] = None
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchyEntity:
    object: str
    id: str
    name: str
    slug: str
    parent_skill_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsCreateOutputHierarchy:
    object: str
    type: str
    entity: ManagementInstanceSkillsCreateOutputHierarchyEntity
    parent_skill_id: Optional[str] = None
    creator: Optional[ManagementInstanceSkillsCreateOutputHierarchyCreator] = None
    fork: Optional[ManagementInstanceSkillsCreateOutputHierarchyFork] = None
@dataclass
class ManagementInstanceSkillsCreateOutputIntegrationsConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceSkillsCreateOutputIntegrations:
    object: str
    id: str
    slug: str
    name: str
    configuration: ManagementInstanceSkillsCreateOutputIntegrationsConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsCreateOutputProviders:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsCreateOutput:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    client_name: str
    metadata: Dict[str, Any]
    store_id: str
    hierarchy: ManagementInstanceSkillsCreateOutputHierarchy
    integrations: List[ManagementInstanceSkillsCreateOutputIntegrations]
    providers: List[ManagementInstanceSkillsCreateOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None


class mapManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActorTeams:
        return ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActor:
        return ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyCreatorConsumer:
        return ManagementInstanceSkillsCreateOutputHierarchyCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyCreator:
        return ManagementInstanceSkillsCreateOutputHierarchyCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsCreateOutputHierarchyCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsCreateOutputHierarchyCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActorTeams:
        return ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActor:
        return ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyForkCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyForkCreatorConsumer:
        return ManagementInstanceSkillsCreateOutputHierarchyForkCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyForkCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyForkCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyForkCreator:
        return ManagementInstanceSkillsCreateOutputHierarchyForkCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsCreateOutputHierarchyForkCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsCreateOutputHierarchyForkCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyForkCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
        return ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActor:
        return ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        teams=[mapManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorConsumer:
        return ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreator:
        return ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyFork:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyFork:
        return ManagementInstanceSkillsCreateOutputHierarchyFork(
        id=data.get('id'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapManagementInstanceSkillsCreateOutputHierarchyForkCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        original_creator=mapManagementInstanceSkillsCreateOutputHierarchyForkOriginalCreator.from_dict(data.get('original_creator')) if data.get('original_creator') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyFork, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchyEntity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchyEntity:
        return ManagementInstanceSkillsCreateOutputHierarchyEntity(
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
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchyEntity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputHierarchy:
        return ManagementInstanceSkillsCreateOutputHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapManagementInstanceSkillsCreateOutputHierarchyCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        fork=mapManagementInstanceSkillsCreateOutputHierarchyFork.from_dict(data.get('fork')) if data.get('fork') else None,
        entity=mapManagementInstanceSkillsCreateOutputHierarchyEntity.from_dict(data.get('entity')) if data.get('entity') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputIntegrationsConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputIntegrationsConfiguration:
        return ManagementInstanceSkillsCreateOutputIntegrationsConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputIntegrationsConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputIntegrations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputIntegrations:
        return ManagementInstanceSkillsCreateOutputIntegrations(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapManagementInstanceSkillsCreateOutputIntegrationsConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputIntegrations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutputProviders:
        return ManagementInstanceSkillsCreateOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsCreateOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateOutput:
        return ManagementInstanceSkillsCreateOutput(
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
        hierarchy=mapManagementInstanceSkillsCreateOutputHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        integrations=[mapManagementInstanceSkillsCreateOutputIntegrations.from_dict(item) for item in data.get('integrations', []) if item],
        providers=[mapManagementInstanceSkillsCreateOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsCreateBody:
    name: str
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    client_name: Optional[str] = None
    client_description: Optional[str] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    image_file_id: Optional[str] = None
    template_id: Optional[str] = None
    skill_group_id: Optional[str] = None


class mapManagementInstanceSkillsCreateBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsCreateBody:
        return ManagementInstanceSkillsCreateBody(
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        client_name=data.get('client_name'),
        client_description=data.get('client_description'),
        license=data.get('license'),
        compatibility=data.get('compatibility'),
        client_metadata=data.get('client_metadata'),
        image_file_id=data.get('image_file_id'),
        template_id=data.get('template_id'),
        skill_group_id=data.get('skill_group_id')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsCreateBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

