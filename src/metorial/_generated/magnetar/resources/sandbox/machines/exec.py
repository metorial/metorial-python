from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from datetime import datetime
import dataclasses

@dataclass
class SandboxMachinesExecOutput:
    object: str
    timed_out: bool
    stdout: str
    stderr: str
    stdout_truncated: bool
    stderr_truncated: bool
    exit_code: Optional[float] = None
    signal: Optional[str] = None


class mapSandboxMachinesExecOutput:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesExecOutput:
        return SandboxMachinesExecOutput(
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
    def to_dict(value: Union[SandboxMachinesExecOutput, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

@dataclass
class SandboxMachinesExecBody:
    command: str
    cwd: Optional[str] = None
    env: Optional[Dict[str, str]] = None
    timeout_seconds: Optional[float] = None


class mapSandboxMachinesExecBody:
    @staticmethod
    def from_dict(data: Dict[str, Any]) -> SandboxMachinesExecBody:
        return SandboxMachinesExecBody(
        command=data.get('command'),
        cwd=data.get('cwd'),
        env=data.get('env'),
        timeout_seconds=data.get('timeout_seconds')
        )

    @staticmethod
    def to_dict(value: Union[SandboxMachinesExecBody, Dict[str, Any], None]) -> Optional[Dict[str, Any]]:
        if value is None:
            return None
        if isinstance(value, dict):
            return value
        # assume dataclass for generated models
        return dataclasses.asdict(value)

