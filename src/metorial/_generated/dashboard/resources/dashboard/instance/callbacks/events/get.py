from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class DashboardInstanceCallbacksEventsGetOutputProcessingAttempts:
  object: str
  id: str
  status: str
  index: float
  created_at: datetime
  error_code: Optional[str] = None
  error_message: Optional[str] = None


@dataclass
class DashboardInstanceCallbacksEventsGetOutput:
  object: str
  id: str
  status: str
  payload_incoming: str
  processing_attempts: List[DashboardInstanceCallbacksEventsGetOutputProcessingAttempts]
  created_at: datetime
  type: Optional[str] = None
  payload_outgoing: Optional[str] = None


class mapDashboardInstanceCallbacksEventsGetOutputProcessingAttempts:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> DashboardInstanceCallbacksEventsGetOutputProcessingAttempts:
    return DashboardInstanceCallbacksEventsGetOutputProcessingAttempts(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      index=data.get("index"),
      error_code=data.get("error_code"),
      error_message=data.get("error_message"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      DashboardInstanceCallbacksEventsGetOutputProcessingAttempts, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardInstanceCallbacksEventsGetOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardInstanceCallbacksEventsGetOutput:
    return DashboardInstanceCallbacksEventsGetOutput(
      object=data.get("object"),
      id=data.get("id"),
      type=data.get("type"),
      status=data.get("status"),
      payload_incoming=data.get("payload_incoming"),
      payload_outgoing=data.get("payload_outgoing"),
      processing_attempts=[
        mapDashboardInstanceCallbacksEventsGetOutputProcessingAttempts.from_dict(item)
        for item in data.get("processing_attempts", [])
        if item
      ],
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardInstanceCallbacksEventsGetOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
