from typing import Any, Dict, List, Optional, Union
from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapDashboardOrganizationsProjectsBrandingGetOutput, DashboardOrganizationsProjectsBrandingGetOutput, mapDashboardOrganizationsProjectsBrandingUpdateOutput, DashboardOrganizationsProjectsBrandingUpdateOutput, mapDashboardOrganizationsProjectsBrandingUpdateBody, DashboardOrganizationsProjectsBrandingUpdateBody

class MetorialManagementOrganizationProjectsBrandingEndpoint(BaseMetorialEndpoint):
    """Read and write project information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def get(self, project_id: str) -> DashboardOrganizationsProjectsBrandingGetOutput:
        """
    Get project branding
    Get branding information for a specific project

    :param project_id: str
    :return: DashboardOrganizationsProjectsBrandingGetOutput
    """
        request = MetorialRequest(
            path=['organization', 'projects', project_id, 'branding']
        )
        return self._get(request).transform(mapDashboardOrganizationsProjectsBrandingGetOutput.from_dict)

    def update(self, project_id: str, *, name: Optional[str] = None, image_file_id: Optional[str] = None) -> DashboardOrganizationsProjectsBrandingUpdateOutput:
        """
    Update project branding
    Update branding information for a specific project

    :param project_id: str
    :param name: Optional[str] (optional)
    :param image_file_id: Optional[str] (optional)
    :return: DashboardOrganizationsProjectsBrandingUpdateOutput
    """
        # Build body parameters from keyword arguments
        body_dict = {}
        if name is not None:
            body_dict["name"] = name
        if image_file_id is not None:
            body_dict["image_file_id"] = image_file_id

        request = MetorialRequest(
            path=['organization', 'projects', project_id, 'branding'],
            body=body_dict
        )
        return self._patch(request).transform(mapDashboardOrganizationsProjectsBrandingUpdateOutput.from_dict)