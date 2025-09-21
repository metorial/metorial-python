from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses


@dataclass
class DashboardUsageTimelineOutputTimelineEntries:
  ts: datetime
  count: float


@dataclass
class DashboardUsageTimelineOutputTimeline:
  entity_id: str
  entity_type: str
  owner_id: str
  entries: List[DashboardUsageTimelineOutputTimelineEntries]


@dataclass
class DashboardUsageTimelineOutput:
  object: str
  timeline: List[DashboardUsageTimelineOutputTimeline]


class mapDashboardUsageTimelineOutputTimelineEntries:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardUsageTimelineOutputTimelineEntries:
    return DashboardUsageTimelineOutputTimelineEntries(
      ts=datetime.fromisoformat(data.get("ts")) if data.get("ts") else None,
      count=data.get("count"),
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardUsageTimelineOutputTimelineEntries, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardUsageTimelineOutputTimeline:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardUsageTimelineOutputTimeline:
    return DashboardUsageTimelineOutputTimeline(
      entity_id=data.get("entity_id"),
      entity_type=data.get("entity_type"),
      owner_id=data.get("owner_id"),
      entries=[
        mapDashboardUsageTimelineOutputTimelineEntries.from_dict(item)
        for item in data.get("entries", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardUsageTimelineOutputTimeline, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardUsageTimelineOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardUsageTimelineOutput:
    return DashboardUsageTimelineOutput(
      object=data.get("object"),
      timeline=[
        mapDashboardUsageTimelineOutputTimeline.from_dict(item)
        for item in data.get("timeline", [])
        if item
      ],
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardUsageTimelineOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)


@dataclass
class DashboardUsageTimelineQueryEntities:
  type: str
  id: str


@dataclass
class DashboardUsageTimelineQueryInterval:
  unit: str
  count: float


@dataclass
class DashboardUsageTimelineQuery:
  entities: List[DashboardUsageTimelineQueryEntities]
  from_: datetime
  to: datetime
  interval: DashboardUsageTimelineQueryInterval


class mapDashboardUsageTimelineQueryEntities:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardUsageTimelineQueryEntities:
    return DashboardUsageTimelineQueryEntities(type=data.get("type"), id=data.get("id"))

  @staticmethod
  def to_dict(
    value: Union[DashboardUsageTimelineQueryEntities, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardUsageTimelineQueryInterval:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardUsageTimelineQueryInterval:
    return DashboardUsageTimelineQueryInterval(
      unit=data.get("unit"), count=data.get("count")
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardUsageTimelineQueryInterval, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapDashboardUsageTimelineQuery:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> DashboardUsageTimelineQuery:
    return DashboardUsageTimelineQuery(
      entities=[
        mapDashboardUsageTimelineQueryEntities.from_dict(item)
        for item in data.get("entities", [])
        if item
      ],
      from_=datetime.fromisoformat(data.get("from")) if data.get("from") else None,
      to=datetime.fromisoformat(data.get("to")) if data.get("to") else None,
      interval=mapDashboardUsageTimelineQueryInterval.from_dict(data.get("interval"))
      if data.get("interval")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[DashboardUsageTimelineQuery, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
