from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxMachinesAccessShellOutput, DashboardInstanceSandboxMachinesAccessShellOutput, mapDashboardInstanceSandboxMachinesAccessShellBody, DashboardInstanceSandboxMachinesAccessShellBody, mapDashboardInstanceSandboxMachinesAccessFilesOutput, DashboardInstanceSandboxMachinesAccessFilesOutput, mapDashboardInstanceSandboxMachinesAccessFilesBody, DashboardInstanceSandboxMachinesAccessFilesBody, mapDashboardInstanceSandboxMachinesAccessPortsOutput, DashboardInstanceSandboxMachinesAccessPortsOutput, mapDashboardInstanceSandboxMachinesAccessPortsBody, DashboardInstanceSandboxMachinesAccessPortsBody

class MetorialDashboardInstanceSandboxMachinesAccessEndpoint(BaseMetorialEndpoint):
    """Create and operate sandbox machines. A machine boots from an image, can mount disks, and moves between running, paused, and hibernated states."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def shell(self, instance_id: str, machine_id: str, *, ttl_seconds: Optional[float] = None) -> DashboardInstanceSandboxMachinesAccessShellOutput:
        """
    Create shell access
    Creates a short-lived token for an interactive shell in the machine.

    :param instance_id: str
    :param machine_id: str
    :param ttl_seconds: Optional[float] (optional)
    :return: DashboardInstanceSandboxMachinesAccessShellOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if ttl_seconds is not None:
            body_dict["ttl_seconds"] = ttl_seconds

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'access', 'shell'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesAccessShellOutput.from_dict)

    def files(self, instance_id: str, machine_id: str, *, ttl_seconds: Optional[float] = None) -> DashboardInstanceSandboxMachinesAccessFilesOutput:
        """
    Create files access
    Creates a short-lived token for the machine's file service.

    :param instance_id: str
    :param machine_id: str
    :param ttl_seconds: Optional[float] (optional)
    :return: DashboardInstanceSandboxMachinesAccessFilesOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if ttl_seconds is not None:
            body_dict["ttl_seconds"] = ttl_seconds

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'access', 'files'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesAccessFilesOutput.from_dict)

    def ports(self, instance_id: str, machine_id: str, *, ports: Union[List[float], Any], ttl_seconds: Optional[float] = None) -> DashboardInstanceSandboxMachinesAccessPortsOutput:
        """
    Create port access
    Creates a short-lived token for reaching ports inside the machine.

    :param instance_id: str
    :param machine_id: str
    :param ports: Union[List[float], Any]
    :param ttl_seconds: Optional[float] (optional)
    :return: DashboardInstanceSandboxMachinesAccessPortsOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["ports"] = ports
        if ttl_seconds is not None:
            body_dict["ttl_seconds"] = ttl_seconds

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'access', 'ports'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesAccessPortsOutput.from_dict)