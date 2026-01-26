from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class CallbacksGetOutputSchedule:
  object: str
  interval_seconds: float
  next_run_at: datetime


@dataclass
class CallbacksGetOutput:
  object: str
  id: str
  type: str
  schedule: CallbacksGetOutputSchedule
  created_at: datetime
  updated_at: datetime
  url: Optional[str] = None
  name: Optional[str] = None
  description: Optional[str] = None


class mapCallbacksGetOutputSchedule:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksGetOutputSchedule:
    return CallbacksGetOutputSchedule(
      object=data.get("object"),
      interval_seconds=data.get("interval_seconds"),
      next_run_at=parse_iso_datetime(data.get("next_run_at"))
      if data.get("next_run_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksGetOutputSchedule, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapCallbacksGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> CallbacksGetOutput:
    return CallbacksGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      url=data.get("url"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      schedule=mapCallbacksGetOutputSchedule.from_dict(data.get("schedule"))
      if data.get("schedule")
      else None,
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[CallbacksGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
