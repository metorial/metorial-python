from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsShareOutputHierarchyCreatorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsShareOutputHierarchyForkCreatorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember:
    object: str
    id: str
    status: str
    role: str
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
    id: str
    name: str
    slug: str
    assignment_id: str
    created_at: datetime
    updated_at: datetime
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor:
    object: str
    id: str
    type: str
    organization_id: str
    name: str
    image_url: str
    teams: List[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams]
    created_at: datetime
    updated_at: datetime
    email: Optional[str] = None
    member: Optional[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorConsumer:
    object: str
    id: str
    name: str
    email: str
    image_url: str
    created_at: datetime
    updated_at: datetime
    user_id: Optional[str] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreator:
    type: str
    name: str
    image_url: Optional[str] = None
    email: Optional[str] = None
    organization_actor: Optional[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor] = None
    consumer: Optional[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorConsumer] = None
    consumer_profile: Optional[Dict[str, Any]] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyFork:
    id: str
    parent_skill_id: str
    created_at: datetime
    creator: Optional[ManagementInstanceSkillsShareOutputHierarchyForkCreator] = None
    original_creator: Optional[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreator] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchyEntity:
    object: str
    id: str
    name: str
    slug: str
    parent_skill_id: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsShareOutputHierarchy:
    object: str
    type: str
    entity: ManagementInstanceSkillsShareOutputHierarchyEntity
    parent_skill_id: Optional[str] = None
    creator: Optional[ManagementInstanceSkillsShareOutputHierarchyCreator] = None
    fork: Optional[ManagementInstanceSkillsShareOutputHierarchyFork] = None
@dataclass
class ManagementInstanceSkillsShareOutputIntegrationsConfiguration:
    can_attach_custom_tool_filters: bool
    can_attach_custom_provider_config: bool
    can_override_tool_filters: bool
    use_integration_name_in_tool_names: Optional[bool] = None
@dataclass
class ManagementInstanceSkillsShareOutputIntegrations:
    object: str
    id: str
    slug: str
    name: str
    configuration: ManagementInstanceSkillsShareOutputIntegrationsConfiguration
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    archived_at: Optional[datetime] = None
@dataclass
class ManagementInstanceSkillsShareOutputProviders:
    object: str
    id: str
    name: str
    slug: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
@dataclass
class ManagementInstanceSkillsShareOutput:
    object: str
    id: str
    status: str
    slug: str
    name: str
    image_url: str
    client_name: str
    metadata: Dict[str, Any]
    store_id: str
    hierarchy: ManagementInstanceSkillsShareOutputHierarchy
    integrations: List[ManagementInstanceSkillsShareOutputIntegrations]
    providers: List[ManagementInstanceSkillsShareOutputProviders]
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    client_description: Optional[str] = None
    client_metadata: Optional[Dict[str, Any]] = None
    license: Optional[str] = None
    compatibility: Optional[str] = None


class mapManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorMember:
        return ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorTeams:
        return ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActor:
        return ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyCreatorConsumer:
        return ManagementInstanceSkillsShareOutputHierarchyCreatorConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyCreator:
        return ManagementInstanceSkillsShareOutputHierarchyCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsShareOutputHierarchyCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsShareOutputHierarchyCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorMember:
        return ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams:
        return ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActor:
        return ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkCreatorConsumer:
        return ManagementInstanceSkillsShareOutputHierarchyForkCreatorConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkCreator:
        return ManagementInstanceSkillsShareOutputHierarchyForkCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsShareOutputHierarchyForkCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsShareOutputHierarchyForkCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember:
        return ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember(
        object=data.get('object'),
        id=data.get('id'),
        status=data.get('status'),
        role=data.get('role')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams:
        return ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams(
        id=data.get('id'),
        name=data.get('name'),
        slug=data.get('slug'),
        assignment_id=data.get('assignment_id'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor:
        return ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor(
        object=data.get('object'),
        id=data.get('id'),
        type=data.get('type'),
        organization_id=data.get('organization_id'),
        name=data.get('name'),
        email=data.get('email'),
        image_url=data.get('image_url'),
        member=mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorMember.from_dict(data.get('member')) if data.get('member') else None,
        teams=[mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActorTeams.from_dict(item) for item in data.get('teams', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorConsumer:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorConsumer:
        return ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorConsumer(
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
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorConsumer, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreator:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreator:
        return ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreator(
        type=data.get('type'),
        name=data.get('name'),
        image_url=data.get('image_url'),
        email=data.get('email'),
        organization_actor=mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorOrganizationActor.from_dict(data.get('organization_actor')) if data.get('organization_actor') else None,
        consumer=mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreatorConsumer.from_dict(data.get('consumer')) if data.get('consumer') else None,
        consumer_profile=data.get('consumer_profile')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyForkOriginalCreator, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyFork:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyFork:
        return ManagementInstanceSkillsShareOutputHierarchyFork(
        id=data.get('id'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapManagementInstanceSkillsShareOutputHierarchyForkCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        original_creator=mapManagementInstanceSkillsShareOutputHierarchyForkOriginalCreator.from_dict(data.get('original_creator')) if data.get('original_creator') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyFork, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchyEntity:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchyEntity:
        return ManagementInstanceSkillsShareOutputHierarchyEntity(
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
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchyEntity, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputHierarchy:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputHierarchy:
        return ManagementInstanceSkillsShareOutputHierarchy(
        object=data.get('object'),
        type=data.get('type'),
        parent_skill_id=data.get('parent_skill_id'),
        creator=mapManagementInstanceSkillsShareOutputHierarchyCreator.from_dict(data.get('creator')) if data.get('creator') else None,
        fork=mapManagementInstanceSkillsShareOutputHierarchyFork.from_dict(data.get('fork')) if data.get('fork') else None,
        entity=mapManagementInstanceSkillsShareOutputHierarchyEntity.from_dict(data.get('entity')) if data.get('entity') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputHierarchy, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputIntegrationsConfiguration:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputIntegrationsConfiguration:
        return ManagementInstanceSkillsShareOutputIntegrationsConfiguration(
        can_attach_custom_tool_filters=data.get('can_attach_custom_tool_filters'),
        can_attach_custom_provider_config=data.get('can_attach_custom_provider_config'),
        can_override_tool_filters=data.get('can_override_tool_filters'),
        use_integration_name_in_tool_names=data.get('use_integration_name_in_tool_names')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputIntegrationsConfiguration, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputIntegrations:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputIntegrations:
        return ManagementInstanceSkillsShareOutputIntegrations(
        object=data.get('object'),
        id=data.get('id'),
        slug=data.get('slug'),
        name=data.get('name'),
        description=data.get('description'),
        metadata=data.get('metadata'),
        configuration=mapManagementInstanceSkillsShareOutputIntegrationsConfiguration.from_dict(data.get('configuration')) if data.get('configuration') else None,
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None,
        archived_at=datetime.fromisoformat(data.get('archived_at').replace('Z', '+00:00')) if data.get('archived_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputIntegrations, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutputProviders:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutputProviders:
        return ManagementInstanceSkillsShareOutputProviders(
        object=data.get('object'),
        id=data.get('id'),
        name=data.get('name'),
        description=data.get('description'),
        slug=data.get('slug'),
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutputProviders, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceSkillsShareOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareOutput:
        return ManagementInstanceSkillsShareOutput(
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
        hierarchy=mapManagementInstanceSkillsShareOutputHierarchy.from_dict(data.get('hierarchy')) if data.get('hierarchy') else None,
        integrations=[mapManagementInstanceSkillsShareOutputIntegrations.from_dict(item) for item in data.get('integrations', []) if item],
        providers=[mapManagementInstanceSkillsShareOutputProviders.from_dict(item) for item in data.get('providers', []) if item],
        created_at=datetime.fromisoformat(data.get('created_at').replace('Z', '+00:00')) if data.get('created_at') else None,
        updated_at=datetime.fromisoformat(data.get('updated_at').replace('Z', '+00:00')) if data.get('updated_at') else None
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceSkillsShareBody:
    permission: str
    consumer_profile_ids: Optional[List[str]] = None
    organization_member_ids: Optional[List[str]] = None


class mapManagementInstanceSkillsShareBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceSkillsShareBody:
        return ManagementInstanceSkillsShareBody(
        consumer_profile_ids=data.get('consumer_profile_ids', []),
        organization_member_ids=data.get('organization_member_ids', []),
        permission=data.get('permission')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceSkillsShareBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

