from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
from metorial.utils import parse_iso_datetime
import dataclasses


@dataclass
class ManagementInstanceMagicMcpServersDeleteOutputEndpointsUrls:
  sse: str
  streamable_http: str


@dataclass
class ManagementInstanceMagicMcpServersDeleteOutputEndpoints:
  id: str
  alias: str
  urls: ManagementInstanceMagicMcpServersDeleteOutputEndpointsUrls


@dataclass
class ManagementInstanceMagicMcpServersDeleteOutputServerDeploymentsServer:
  object: str
  id: str
  name: str
  type: str
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersDeleteOutputServerDeployments:
  object: str
  id: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  server: ManagementInstanceMagicMcpServersDeleteOutputServerDeploymentsServer
  name: Optional[str] = None
  description: Optional[str] = None


@dataclass
class ManagementInstanceMagicMcpServersDeleteOutput:
  object: str
  id: str
  status: str
  endpoints: List[ManagementInstanceMagicMcpServersDeleteOutputEndpoints]
  server_deployments: List[
    ManagementInstanceMagicMcpServersDeleteOutputServerDeployments
  ]
  name: str
  metadata: Dict[str, Any]
  created_at: datetime
  updated_at: datetime
  description: Optional[str] = None


class mapManagementInstanceMagicMcpServersDeleteOutputEndpointsUrls:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersDeleteOutputEndpointsUrls:
    return ManagementInstanceMagicMcpServersDeleteOutputEndpointsUrls(
      sse=data.get("sse"), streamable_http=data.get("streamable_http")
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersDeleteOutputEndpointsUrls, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersDeleteOutputEndpoints:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersDeleteOutputEndpoints:
    return ManagementInstanceMagicMcpServersDeleteOutputEndpoints(
      id=data.get("id"),
      alias=data.get("alias"),
      urls=mapManagementInstanceMagicMcpServersDeleteOutputEndpointsUrls.from_dict(
        data.get("urls")
      )
      if data.get("urls")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersDeleteOutputEndpoints, Dict[str, Any], None
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersDeleteOutputServerDeploymentsServer:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersDeleteOutputServerDeploymentsServer:
    return ManagementInstanceMagicMcpServersDeleteOutputServerDeploymentsServer(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      type=data.get("type"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersDeleteOutputServerDeploymentsServer,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersDeleteOutputServerDeployments:
  @staticmethod
  def from_dict(
    data: Dict[str, Any]
  ) -> ManagementInstanceMagicMcpServersDeleteOutputServerDeployments:
    return ManagementInstanceMagicMcpServersDeleteOutputServerDeployments(
      object=data.get("object"),
      id=data.get("id"),
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
      server=mapManagementInstanceMagicMcpServersDeleteOutputServerDeploymentsServer.from_dict(
        data.get("server")
      )
      if data.get("server")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[
      ManagementInstanceMagicMcpServersDeleteOutputServerDeployments,
      Dict[str, Any],
      None,
    ]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    return dataclasses.asdict(value)


class mapManagementInstanceMagicMcpServersDeleteOutput:
  @staticmethod
  def from_dict(data: Dict[str, Any]) -> ManagementInstanceMagicMcpServersDeleteOutput:
    return ManagementInstanceMagicMcpServersDeleteOutput(
      object=data.get("object"),
      id=data.get("id"),
      status=data.get("status"),
      endpoints=[
        mapManagementInstanceMagicMcpServersDeleteOutputEndpoints.from_dict(item)
        for item in data.get("endpoints", [])
        if item
      ],
      server_deployments=[
        mapManagementInstanceMagicMcpServersDeleteOutputServerDeployments.from_dict(
          item
        )
        for item in data.get("server_deployments", [])
        if item
      ],
      name=data.get("name"),
      description=data.get("description"),
      metadata=data.get("metadata"),
      created_at=parse_iso_datetime(data.get("created_at"))
      if data.get("created_at")
      else None,
      updated_at=parse_iso_datetime(data.get("updated_at"))
      if data.get("updated_at")
      else None,
    )

  @staticmethod
  def to_dict(
    value: Union[ManagementInstanceMagicMcpServersDeleteOutput, Dict[str, Any], None]
  ) -> Optional[Dict[str, Any]]:
    if value is None:
      return None
    if isinstance(value, dict):
      return value
    # assume dataclass for generated models
    return dataclasses.asdict(value)
