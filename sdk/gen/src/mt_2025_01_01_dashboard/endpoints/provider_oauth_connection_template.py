from metorial_util_endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapProviderOauthConnectionTemplateListOutput, ProviderOauthConnectionTemplateListOutput, mapProviderOauthConnectionTemplateListQuery, ProviderOauthConnectionTemplateListQuery, mapProviderOauthConnectionTemplateGetOutput, ProviderOauthConnectionTemplateGetOutput

class MetorialProviderOauthConnectionTemplateEndpoint(BaseMetorialEndpoint):
    """Get OAuth connection template information"""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, query: ProviderOauthConnectionTemplateListQuery = None):
        """
    List oauth connection templates
    List all oauth connection templates

    :param query: ProviderOauthConnectionTemplateListQuery
    :return: ProviderOauthConnectionTemplateListOutput
    """
        request = MetorialRequest(
            path=['provider-oauth-connection-template'],
            query=mapProviderOauthConnectionTemplateListQuery.to_dict(query) if query is not None else None,
        )
        return self._get(request).transform(mapProviderOauthConnectionTemplateListOutput.from_dict)

    def get(self, oauthTemplateId: str):
        """
    Get oauth connection template
    Get the information of a specific oauth connection template

    :param oauthTemplateId: str
    :return: ProviderOauthConnectionTemplateGetOutput
    """
        request = MetorialRequest(
            path=['provider-oauth-connection-template', oauthTemplateId]
        )
        return self._get(request).transform(mapProviderOauthConnectionTemplateGetOutput.from_dict)