from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutputRecords:
    object: str
    direction: str
    enclave_id: str
    bucket_start: str
    hostname: str
    ip: str
    port: float
    count: float
    first_seen_at: str
    last_seen_at: str
    result: Optional[str] = None
@dataclass
class ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutput:
    object: str
    direction: str
    enclave_ids: List[str]
    records: List[ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutputRecords]


class mapManagementInstanceIntegrationInternetGatewayListNetworkLogsOutputRecords:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutputRecords:
        return ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutputRecords(
        object=data.get('object'),
        direction=data.get('direction'),
        enclave_id=data.get('enclave_id'),
        bucket_start=data.get('bucket_start'),
        hostname=data.get('hostname'),
        ip=data.get('ip'),
        port=data.get('port'),
        count=data.get('count'),
        result=data.get('result'),
        first_seen_at=data.get('first_seen_at'),
        last_seen_at=data.get('last_seen_at')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutputRecords, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        return dataclasses.asdict(value)

class mapManagementInstanceIntegrationInternetGatewayListNetworkLogsOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutput:
        return ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutput(
        object=data.get('object'),
        direction=data.get('direction'),
        enclave_ids=data.get('enclave_ids', []),
        records=[mapManagementInstanceIntegrationInternetGatewayListNetworkLogsOutputRecords.from_dict(item) for item in data.get('records', []) if item]
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationInternetGatewayListNetworkLogsOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class ManagementInstanceIntegrationInternetGatewayListNetworkLogsQuery:
    direction: str
    enclave_id: Optional[Union[str, List[str]]] = None
    hostname: Optional[Union[str, List[str]]] = None
    ip: Optional[Union[str, List[str]]] = None
    from_: Optional[str] = None
    to: Optional[str] = None
    interval_minutes: Optional[float] = None


class mapManagementInstanceIntegrationInternetGatewayListNetworkLogsQuery:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> ManagementInstanceIntegrationInternetGatewayListNetworkLogsQuery:
        return ManagementInstanceIntegrationInternetGatewayListNetworkLogsQuery(
        direction=data.get('direction'),
        enclave_id=data.get('enclave_id'),
        hostname=data.get('hostname'),
        ip=data.get('ip'),
        from_=data.get('from'),
        to=data.get('to'),
        interval_minutes=data.get('interval_minutes')
        )

    @staticmethod
    def to_dict(value: Union[ManagementInstanceIntegrationInternetGatewayListNetworkLogsQuery, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

