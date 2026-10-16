from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceSandboxMachinesListOutput, DashboardInstanceSandboxMachinesListOutput, mapDashboardInstanceSandboxMachinesListQuery, DashboardInstanceSandboxMachinesListQuery, mapDashboardInstanceSandboxMachinesGetOutput, DashboardInstanceSandboxMachinesGetOutput, mapDashboardInstanceSandboxMachinesCreateOutput, DashboardInstanceSandboxMachinesCreateOutput, mapDashboardInstanceSandboxMachinesCreateBody, DashboardInstanceSandboxMachinesCreateBody, mapDashboardInstanceSandboxMachinesUpdateOutput, DashboardInstanceSandboxMachinesUpdateOutput, mapDashboardInstanceSandboxMachinesUpdateBody, DashboardInstanceSandboxMachinesUpdateBody, mapDashboardInstanceSandboxMachinesDeleteOutput, DashboardInstanceSandboxMachinesDeleteOutput, mapDashboardInstanceSandboxMachinesStartOutput, DashboardInstanceSandboxMachinesStartOutput, mapDashboardInstanceSandboxMachinesPauseOutput, DashboardInstanceSandboxMachinesPauseOutput, mapDashboardInstanceSandboxMachinesHibernateOutput, DashboardInstanceSandboxMachinesHibernateOutput, mapDashboardInstanceSandboxMachinesRestartOutput, DashboardInstanceSandboxMachinesRestartOutput, mapDashboardInstanceSandboxMachinesTouchOutput, DashboardInstanceSandboxMachinesTouchOutput, mapDashboardInstanceSandboxMachinesUsageOutput, DashboardInstanceSandboxMachinesUsageOutput, mapDashboardInstanceSandboxMachinesUsageQuery, DashboardInstanceSandboxMachinesUsageQuery

class MetorialDashboardInstanceSandboxMachinesEndpoint(BaseMetorialEndpoint):
    """Create and operate sandbox machines. A machine boots from an image, can mount disks, and moves between running, paused, and hibernated states."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, instance_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, id: Optional[Union[str, List[str]]] = None, status: Optional[Union[str, List[str]]] = None, state: Optional[Union[str, List[str]]] = None, image_id: Optional[Union[str, List[str]]] = None, region: Optional[Union[str, List[str]]] = None, search: Optional[str] = None) -> DashboardInstanceSandboxMachinesListOutput:
        """
    List sandbox machines
    Returns a paginated list of machines.

    :param instance_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param id: Optional[Union[str, List[str]]] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :param state: Optional[Union[str, List[str]]] (optional)
    :param image_id: Optional[Union[str, List[str]]] (optional)
    :param region: Optional[Union[str, List[str]]] (optional)
    :param search: Optional[str] (optional)
    :return: DashboardInstanceSandboxMachinesListOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if limit is not None:
            query_dict["limit"] = limit
        if after is not None:
            query_dict["after"] = after
        if before is not None:
            query_dict["before"] = before
        if cursor is not None:
            query_dict["cursor"] = cursor
        if order is not None:
            query_dict["order"] = order
        if id is not None:
            query_dict["id"] = id
        if status is not None:
            query_dict["status"] = status
        if state is not None:
            query_dict["state"] = state
        if image_id is not None:
            query_dict["image_id"] = image_id
        if region is not None:
            query_dict["region"] = region
        if search is not None:
            query_dict["search"] = search

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesListOutput.from_dict)

    def get(self, instance_id: str, machine_id: str) -> DashboardInstanceSandboxMachinesGetOutput:
        """
    Get sandbox machine
    Retrieves a machine by ID.

    :param instance_id: str
    :param machine_id: str
    :return: DashboardInstanceSandboxMachinesGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id]
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesGetOutput.from_dict)

    def create(self, instance_id: str, *, region: str, image_id: str, metadata: Optional[Dict[str, Any]] = None, name: Optional[str] = None, spec_id: Optional[str] = None, spec_identifier: Optional[str] = None, memory_gib: Optional[float] = None, cpus: Optional[float] = None, lifecycle_policy: Optional[Dict[str, Any]] = None, runtime: Optional[Dict[str, Any]] = None, lifecycle_hooks: Optional[List[Union[Dict[str, Any], Dict[str, Any]]]] = None, ignore_image_hooks: Optional[bool] = None, entrypoint_wait_seconds: Optional[float] = None, mounts: Optional[List[Dict[str, Any]]] = None, firewall_ids: Optional[List[str]] = None, public_ports: Optional[List[float]] = None, start: Optional[bool] = None) -> DashboardInstanceSandboxMachinesCreateOutput:
        """
    Create sandbox machine
    Creates a machine and, unless disabled, starts it.

    :param instance_id: str
    :param region: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param name: Optional[str] (optional)
    :param image_id: str
    :param spec_id: Optional[str] (optional)
    :param spec_identifier: Optional[str] (optional)
    :param memory_gib: Optional[float] (optional)
    :param cpus: Optional[float] (optional)
    :param lifecycle_policy: Optional[Dict[str, Any]] (optional)
    :param runtime: Optional[Dict[str, Any]] (optional)
    :param lifecycle_hooks: Optional[List[Union[Dict[str, Any], Dict[str, Any]]]] (optional)
    :param ignore_image_hooks: Optional[bool] (optional)
    :param entrypoint_wait_seconds: Optional[float] (optional)
    :param mounts: Optional[List[Dict[str, Any]]] (optional)
    :param firewall_ids: Optional[List[str]] (optional)
    :param public_ports: Optional[List[float]] (optional)
    :param start: Optional[bool] (optional)
    :return: DashboardInstanceSandboxMachinesCreateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        body_dict["region"] = region
        if metadata is not None:
            body_dict["metadata"] = metadata
        if name is not None:
            body_dict["name"] = name
        body_dict["image_id"] = image_id
        if spec_id is not None:
            body_dict["spec_id"] = spec_id
        if spec_identifier is not None:
            body_dict["spec_identifier"] = spec_identifier
        if memory_gib is not None:
            body_dict["memory_gib"] = memory_gib
        if cpus is not None:
            body_dict["cpus"] = cpus
        if lifecycle_policy is not None:
            body_dict["lifecycle_policy"] = lifecycle_policy
        if runtime is not None:
            body_dict["runtime"] = runtime
        if lifecycle_hooks is not None:
            body_dict["lifecycle_hooks"] = lifecycle_hooks
        if ignore_image_hooks is not None:
            body_dict["ignore_image_hooks"] = ignore_image_hooks
        if entrypoint_wait_seconds is not None:
            body_dict["entrypoint_wait_seconds"] = entrypoint_wait_seconds
        if mounts is not None:
            body_dict["mounts"] = mounts
        if firewall_ids is not None:
            body_dict["firewall_ids"] = firewall_ids
        if public_ports is not None:
            body_dict["public_ports"] = public_ports
        if start is not None:
            body_dict["start"] = start

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesCreateOutput.from_dict)

    def update(self, instance_id: str, machine_id: str, *, metadata: Optional[Dict[str, Any]] = None, name: Optional[str] = None, spec_id: Optional[str] = None, spec_identifier: Optional[str] = None, memory_gib: Optional[float] = None, cpus: Optional[float] = None, lifecycle_policy: Optional[Dict[str, Any]] = None, runtime: Optional[Dict[str, Any]] = None, lifecycle_hooks: Optional[List[Union[Dict[str, Any], Dict[str, Any]]]] = None, ignore_image_hooks: Optional[bool] = None, entrypoint_wait_seconds: Optional[float] = None, mounts: Optional[List[Dict[str, Any]]] = None, firewall_ids: Optional[List[str]] = None, public_ports: Optional[List[float]] = None) -> DashboardInstanceSandboxMachinesUpdateOutput:
        """
    Update sandbox machine
    Updates a machine. Changes to its size, runtime, or mounts take effect once the machine restarts, which happens on its own for a running machine, and the machine reports restart_required until then.

    :param instance_id: str
    :param machine_id: str
    :param metadata: Optional[Dict[str, Any]] (optional)
    :param name: Optional[str] (optional)
    :param spec_id: Optional[str] (optional)
    :param spec_identifier: Optional[str] (optional)
    :param memory_gib: Optional[float] (optional)
    :param cpus: Optional[float] (optional)
    :param lifecycle_policy: Optional[Dict[str, Any]] (optional)
    :param runtime: Optional[Dict[str, Any]] (optional)
    :param lifecycle_hooks: Optional[List[Union[Dict[str, Any], Dict[str, Any]]]] (optional)
    :param ignore_image_hooks: Optional[bool] (optional)
    :param entrypoint_wait_seconds: Optional[float] (optional)
    :param mounts: Optional[List[Dict[str, Any]]] (optional)
    :param firewall_ids: Optional[List[str]] (optional)
    :param public_ports: Optional[List[float]] (optional)
    :return: DashboardInstanceSandboxMachinesUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if metadata is not None:
            body_dict["metadata"] = metadata
        if name is not None:
            body_dict["name"] = name
        if spec_id is not None:
            body_dict["spec_id"] = spec_id
        if spec_identifier is not None:
            body_dict["spec_identifier"] = spec_identifier
        if memory_gib is not None:
            body_dict["memory_gib"] = memory_gib
        if cpus is not None:
            body_dict["cpus"] = cpus
        if lifecycle_policy is not None:
            body_dict["lifecycle_policy"] = lifecycle_policy
        if runtime is not None:
            body_dict["runtime"] = runtime
        if lifecycle_hooks is not None:
            body_dict["lifecycle_hooks"] = lifecycle_hooks
        if ignore_image_hooks is not None:
            body_dict["ignore_image_hooks"] = ignore_image_hooks
        if entrypoint_wait_seconds is not None:
            body_dict["entrypoint_wait_seconds"] = entrypoint_wait_seconds
        if mounts is not None:
            body_dict["mounts"] = mounts
        if firewall_ids is not None:
            body_dict["firewall_ids"] = firewall_ids
        if public_ports is not None:
            body_dict["public_ports"] = public_ports

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardInstanceSandboxMachinesUpdateOutput.from_dict)

    def delete(self, instance_id: str, machine_id: str) -> DashboardInstanceSandboxMachinesDeleteOutput:
        """
    Terminate sandbox machine
    Terminates a machine and deletes its root disk.

    :param instance_id: str
    :param machine_id: str
    :return: DashboardInstanceSandboxMachinesDeleteOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id]
        )
        return self._delete(request).transform(mapDashboardInstanceSandboxMachinesDeleteOutput.from_dict)

    def start(self, instance_id: str, machine_id: str) -> DashboardInstanceSandboxMachinesStartOutput:
        """
    Start sandbox machine
    Starts a paused or hibernated machine.

    :param instance_id: str
    :param machine_id: str
    :return: DashboardInstanceSandboxMachinesStartOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'start']
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesStartOutput.from_dict)

    def pause(self, instance_id: str, machine_id: str) -> DashboardInstanceSandboxMachinesPauseOutput:
        """
    Pause sandbox machine
    Pauses a running machine and keeps its memory state.

    :param instance_id: str
    :param machine_id: str
    :return: DashboardInstanceSandboxMachinesPauseOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'pause']
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesPauseOutput.from_dict)

    def hibernate(self, instance_id: str, machine_id: str) -> DashboardInstanceSandboxMachinesHibernateOutput:
        """
    Hibernate sandbox machine
    Hibernates a machine so it stops consuming compute resources.

    :param instance_id: str
    :param machine_id: str
    :return: DashboardInstanceSandboxMachinesHibernateOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'hibernate']
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesHibernateOutput.from_dict)

    def restart(self, instance_id: str, machine_id: str) -> DashboardInstanceSandboxMachinesRestartOutput:
        """
    Restart sandbox machine
    Restarts a machine on a fresh instance.

    :param instance_id: str
    :param machine_id: str
    :return: DashboardInstanceSandboxMachinesRestartOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'restart']
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesRestartOutput.from_dict)

    def touch(self, instance_id: str, machine_id: str) -> DashboardInstanceSandboxMachinesTouchOutput:
        """
    Touch sandbox machine
    Records activity so the machine is not paused for being idle.

    :param instance_id: str
    :param machine_id: str
    :return: DashboardInstanceSandboxMachinesTouchOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'touch']
        )
        return self._post(request).transform(mapDashboardInstanceSandboxMachinesTouchOutput.from_dict)

    def usage(self, instance_id: str, machine_id: str, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, machine_instance_id: Optional[Union[str, List[str]]] = None) -> DashboardInstanceSandboxMachinesUsageOutput:
        """
    List sandbox machine usage
    Returns resource usage samples of a machine, newest first.

    :param instance_id: str
    :param machine_id: str
    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param machine_instance_id: Optional[Union[str, List[str]]] (optional)
    :return: DashboardInstanceSandboxMachinesUsageOutput
    """
        # Build query parameters from keyword arguments
        query_dict = {}
        if limit is not None:
            query_dict["limit"] = limit
        if after is not None:
            query_dict["after"] = after
        if before is not None:
            query_dict["before"] = before
        if cursor is not None:
            query_dict["cursor"] = cursor
        if order is not None:
            query_dict["order"] = order
        if machine_instance_id is not None:
            query_dict["machine_instance_id"] = machine_instance_id

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'sandbox', 'machines', machine_id, 'usage'],
            query=query_dict
        )
        return self._get(request).transform(mapDashboardInstanceSandboxMachinesUsageOutput.from_dict)