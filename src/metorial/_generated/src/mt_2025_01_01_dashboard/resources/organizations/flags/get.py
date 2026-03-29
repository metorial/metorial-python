from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class OrganizationsFlagsGetOutputFlags:
    slug: str
    value: bool
@dataclass
class OrganizationsFlagsGetOutput:
    object: str
    flags: List[OrganizationsFlagsGetOutputFlags]


class mapOrganizationsFlagsGetOutputFlags:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> OrganizationsFlagsGetOutputFlags:
        return OrganizationsFlagsGetOutputFlags(
        slug=data.get('slug'),
        value=data.get('value')
        )

    @staticmethod
    def to_dict(value: Union[OrganizationsFlagsGetOutputFlags, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapOrganizationsFlagsGetOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> OrganizationsFlagsGetOutput:
        return OrganizationsFlagsGetOutput(
        object=data.get('object'),
        flags=[mapOrganizationsFlagsGetOutputFlags.from_dict(item) for item in data.get('flags', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[OrganizationsFlagsGetOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

