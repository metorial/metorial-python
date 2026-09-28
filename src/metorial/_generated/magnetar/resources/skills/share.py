from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SkillsShareOutputHierarchyCreatorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsShareOutputHierarchyCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsShareOutputHierarchyCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsShareOutputHierarchyCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsShareOutputHierarchyCreatorOrganizationActorMember] = None
@dataclass
class SkillsShareOutputHierarchyCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsShareOutputHierarchyCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsShareOutputHierarchyCreatorOrganizationActor] = None
    consumer: Optional[SkillsShareOutputHierarchyCreatorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsShareOutputHierarchyForkCreatorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsShareOutputHierarchyForkCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsShareOutputHierarchyForkCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsShareOutputHierarchyForkCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsShareOutputHierarchyForkCreatorOrganizationActorMember] = None
@dataclass
class SkillsShareOutputHierarchyForkCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsShareOutputHierarchyForkCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsShareOutputHierarchyForkCreatorOrganizationActor] = None
    consumer: Optional[SkillsShareOutputHierarchyForkCreatorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember] = None
@dataclass
class SkillsShareOutputHierarchyForkOriginalCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class SkillsShareOutputHierarchyForkOriginalCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor] = None
    consumer: Optional[SkillsShareOutputHierarchyForkOriginalCreatorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class SkillsShareOutputHierarchyFork:
    id: str
    parent_skill_id: str
    created_at: datetime
    creator: Optional[SkillsShareOutputHierarchyForkCreator] = None
    original_creator: Optional[SkillsShareOutputHierarchyForkOriginalCreator] = None
@dataclass
class SkillsShareOutputHierarchyEntity:
    object: str
    id: str
    name: str
    slug: str
    parent_skill_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class SkillsShareOutputHierarchy:
    object: str
    type: str
    entity: SkillsShareOutputHierarchyEntity
    parent_skill_id: Optional[str] = None
    creator: Optional[SkillsShareOutputHierarchyCreator] = None
    fork: Optional[SkillsShareOutputHierarchyFork] = None
@dataclass
class SkillsShareOutputIntegrationsConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    enable_callback_tools: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class SkillsShareOutputIntegrations:
    object: str
    id: str
    slug: str
    name: str
    configuration: SkillsShareOutputIntegrationsConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class SkillsShareOutputProviders:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class SkillsShareOutput:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    client_name: str
    metadata: Dict[str, Any]
    store_id: str
    hierarchy: SkillsShareOutputHierarchy
    integrations: List[SkillsShareOutputIntegrations]
    providers: List[SkillsShareOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None


class mapSkillsShareOutputHierarchyCreatorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyCreatorOrganizationActorMember:
        return SkillsShareOutputHierarchyCreatorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyCreatorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyCreatorOrganizationActorTeams:
        return SkillsShareOutputHierarchyCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyCreatorOrganizationActor:
        return SkillsShareOutputHierarchyCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsShareOutputHierarchyCreatorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsShareOutputHierarchyCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyCreatorConsumer:
        return SkillsShareOutputHierarchyCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        user_id=data.get('user_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyCreator:
        return SkillsShareOutputHierarchyCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsShareOutputHierarchyCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsShareOutputHierarchyCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkCreatorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkCreatorOrganizationActorMember:
        return SkillsShareOutputHierarchyForkCreatorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkCreatorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkCreatorOrganizationActorTeams:
        return SkillsShareOutputHierarchyForkCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkCreatorOrganizationActor:
        return SkillsShareOutputHierarchyForkCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsShareOutputHierarchyForkCreatorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkCreatorConsumer:
        return SkillsShareOutputHierarchyForkCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        user_id=data.get('user_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkCreator:
        return SkillsShareOutputHierarchyForkCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsShareOutputHierarchyForkCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsShareOutputHierarchyForkCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember:
        return SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
        return SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor:
        return SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkOriginalCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkOriginalCreatorConsumer:
        return SkillsShareOutputHierarchyForkOriginalCreatorConsumer(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        user_id=data.get('user_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkOriginalCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyForkOriginalCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyForkOriginalCreator:
        return SkillsShareOutputHierarchyForkOriginalCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapSkillsShareOutputHierarchyForkOriginalCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyForkOriginalCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyFork:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyFork:
        return SkillsShareOutputHierarchyFork(
        id=data.get('id'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapSkillsShareOutputHierarchyForkCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        original_creator=mapSkillsShareOutputHierarchyForkOriginalCreator.from_dict(data.get('original_creator')) if data.get('original_creator') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchyFork, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchyEntity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchyEntity:
        return SkillsShareOutputHierarchyEntity(
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
    def to_dict(value: Union[SkillsShareOutputHierarchyEntity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputHierarchy:
        return SkillsShareOutputHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapSkillsShareOutputHierarchyCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        fork=mapSkillsShareOutputHierarchyFork.from_dict(data.get('fork')) if data.get('fork') else None,
        entity=mapSkillsShareOutputHierarchyEntity.from_dict(data.get('entity')) if data.get('entity') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputIntegrationsConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputIntegrationsConfiguration:
        return SkillsShareOutputIntegrationsConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        enable_callback_tools=data.get('enable_callback_tools'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputIntegrationsConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputIntegrations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputIntegrations:
        return SkillsShareOutputIntegrations(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapSkillsShareOutputIntegrationsConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputIntegrations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutputProviders:
        return SkillsShareOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapSkillsShareOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareOutput:
        return SkillsShareOutput(
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
        hierarchy=mapSkillsShareOutputHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        integrations=[mapSkillsShareOutputIntegrations.from_dict(item) for item in data.get('integrations', []) if item],
        providers=[mapSkillsShareOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SkillsShareBody:
    permission: str
    consumer_profile_ids: Optional[List[str]] = None
    organization_member_ids: Optional[List[str]] = None


class mapSkillsShareBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SkillsShareBody:
        return SkillsShareBody(
        consumer_profile_ids=data.get('consumer_profile_ids', []),
        organization_member_ids=data.get('organization_member_ids', []),
        permission=data.get('permission')
        )

    @staticmethod
    def to_dict(value: Union[SkillsShareBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

