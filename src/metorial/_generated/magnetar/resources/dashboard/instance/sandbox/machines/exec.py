from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class DashboardInstanceSandboxMachinesExecOutput:
    object: str
    timed_out: bool
    stdout: str
    stderr: str
    stdout_truncated: bool
    stderr_truncated: bool
    exit_code: Optional[float] = None
    signal: Optional[str] = None


class mapDashboardInstanceSandboxMachinesExecOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesExecOutput:
        return DashboardInstanceSandboxMachinesExecOutput(
        object=data.get('object'),
        exit_code=data.get('exit_code'),
        signal=data.get('signal'),
        timed_out=data.get('timed_out'),
        stdout=data.get('stdout'),
        stderr=data.get('stderr'),
        stdout_truncated=data.get('stdout_truncated'),
        stderr_truncated=data.get('stderr_truncated')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesExecOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class DashboardInstanceSandboxMachinesExecBody:
    command: str
    cwd: Optional[str] = None
    env: Optional[Dict[str, str]] = None
    timeout_seconds: Optional[float] = None


class mapDashboardInstanceSandboxMachinesExecBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> DashboardInstanceSandboxMachinesExecBody:
        return DashboardInstanceSandboxMachinesExecBody(
        command=data.get('command'),
        cwd=data.get('cwd'),
        env=data.get('env'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[DashboardInstanceSandboxMachinesExecBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

