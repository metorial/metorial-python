from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class SecretsGetOutputType:
  identifier: str
  name: str


@dataclass
class SecretsGetOutput:
  object: str
  id: str
  status: str
  type: SecretsGetOutputType
  description: str
  metadata: Dict[str, Any]
  organization_id: str
  instance_id: str
  fingerprint: str
  created_at: datetime
  last_used_at: Optional[datetime] = None


class mapSecretsGetOutputType:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SecretsGetOutputType:
    return SecretsGetOutputType(
      identifier=data.get("identifier"), name=data.get("name")
    )

  @staticmethod
  def to_dict(
    value: Union[SecretsGetOutputType, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapSecretsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> SecretsGetOutput:
    return SecretsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      type=mapSecretsGetOutputType.from_dict(data.get("type"))
      if data.get("type")
      else None,
      description=data.get("description"),
      metadata=data.get("metadata"),
      organization_id=data.get("organization_id"),
      instance_id=data.get("instance_id"),
      fingerprint=data.get("fingerprint"),
      last_used_at=datetime.fromisoformat(data.get("last_used_at"))
      if data.get("last_used_at")
      else None,
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[SecretsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
