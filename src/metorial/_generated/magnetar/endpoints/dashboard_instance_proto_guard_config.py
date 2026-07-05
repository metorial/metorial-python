from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardInstanceProtoGuardConfigGetOutput, DashboardInstanceProtoGuardConfigGetOutput, mapDashboardInstanceProtoGuardConfigUpdateFilterOutput, DashboardInstanceProtoGuardConfigUpdateFilterOutput, mapDashboardInstanceProtoGuardConfigUpdateFilterBody, DashboardInstanceProtoGuardConfigUpdateFilterBody, mapDashboardInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput, DashboardInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput, mapDashboardInstanceProtoGuardConfigSetAlertFilterCountThresholdBody, DashboardInstanceProtoGuardConfigSetAlertFilterCountThresholdBody

class MetorialDashboardInstanceProtoGuardConfigEndpoint(BaseMetorialEndpoint):
    """ProtoGuard config controls prompt-injection filters and alert thresholds."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, instance_id: str) -> DashboardInstanceProtoGuardConfigGetOutput:
        """
    Get ProtoGuard config
    Retrieves ProtoGuard filter configuration for this instance.

    :param instance_id: str
    :return: DashboardInstanceProtoGuardConfigGetOutput
    """
        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'protoguard-config']
        )
        return self._get(request).transform(mapDashboardInstanceProtoGuardConfigGetOutput.from_dict)

    def update_filter(self, instance_id: str, filter_id: str, *, enabled: Optional[bool] = None, alert_confidence_threshold: Optional[float] = None) -> DashboardInstanceProtoGuardConfigUpdateFilterOutput:
        """
    Update ProtoGuard filter config
    Updates ProtoGuard filter settings for this instance.

    :param instance_id: str
    :param filter_id: str
    :param enabled: Optional[bool] (optional)
    :param alert_confidence_threshold: Optional[float] (optional)
    :return: DashboardInstanceProtoGuardConfigUpdateFilterOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if enabled is not None:
            body_dict["enabled"] = enabled
        if alert_confidence_threshold is not None:
            body_dict["alert_confidence_threshold"] = alert_confidence_threshold

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'protoguard-config', 'filters', filter_id],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProtoGuardConfigUpdateFilterOutput.from_dict)

    def set_alert_filter_count_threshold(self, instance_id: str, *, threshold: Optional[float] = None) -> DashboardInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput:
        """
    Set ProtoGuard alert filter count threshold
    Sets or clears the number of matching ProtoGuard filters required to create an alert.

    :param instance_id: str
    :param threshold: Optional[float] (optional)
    :return: DashboardInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if threshold is not None:
            body_dict["threshold"] = threshold

        request = MetorialRequest(
            path=['dashboard', 'instances', instance_id, 'protoguard-config', 'alert-filter-count-threshold'],
            body=body_dict
        )
        return self._post(request).transform(mapDashboardInstanceProtoGuardConfigSetAlertFilterCountThresholdOutput.from_dict)