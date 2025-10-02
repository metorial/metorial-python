from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class ProviderOauthConnectionTemplateEvaluateOutput:
  object: str
  id: str
  template_id: str
  config: Dict[str, Any]
  created_at: datetime


class mapProviderOauthConnectionTemplateEvaluateOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateEvaluateOutput:
    return ProviderOauthConnectionTemplateEvaluateOutput(
      object=data.get("object"),
      id=data.get("id"),
      template_id=data.get("template_id"),
      config=data.get("config"),
      created_at=datetime.fromisoformat(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionTemplateEvaluateOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class ProviderOauthConnectionTemplateEvaluateBody:
  data: Dict[str, Any]


class mapProviderOauthConnectionTemplateEvaluateBody:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ProviderOauthConnectionTemplateEvaluateBody:
    return ProviderOauthConnectionTemplateEvaluateBody(data=data.get("data"))

  @staticmethod
  def to_dict(
    value: Union[ProviderOauthConnectionTemplateEvaluateBody, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
