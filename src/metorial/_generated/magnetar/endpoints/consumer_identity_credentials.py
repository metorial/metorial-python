from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerIdentityCredentialsListOutput, ConsumerIdentityCredentialsListOutput, mapConsumerIdentityCredentialsListQuery, ConsumerIdentityCredentialsListQuery, mapConsumerIdentityCredentialsGetOutput, ConsumerIdentityCredentialsGetOutput

class MetorialConsumerIdentityCredentialsEndpoint(BaseMetorialEndpoint):
    """Inspect runtime clients, connections, operations, and credentials for the authenticated consumer profile."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, provider_id: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> ConsumerIdentityCredentialsListOutput:
        """
    List consumer identity credentials
    Returns read-only credentials for identities owned by the authenticated profile actor.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param provider_id: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: ConsumerIdentityCredentialsListOutput
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
        if provider_id is not None:
            query_dict["provider_id"] = provider_id
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['consumer', 'identity-credentials'],
            query=query_dict
        )
        return self._get(request).transform(mapConsumerIdentityCredentialsListOutput.from_dict)

    def get(self, identity_credential_id: str) -> ConsumerIdentityCredentialsGetOutput:
        """
    Get consumer identity credential
    Retrieves one credential belonging to an identity owned by the authenticated profile actor.

    :param identity_credential_id: str
    :return: ConsumerIdentityCredentialsGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'identity-credentials', identity_credential_id]
        )
        return self._get(request).transform(mapConsumerIdentityCredentialsGetOutput.from_dict)