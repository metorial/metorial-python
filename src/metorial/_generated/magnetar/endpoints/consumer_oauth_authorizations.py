from typing import Any, Dict, List, Optional, Union
from metorial._endpoint import BaseMetorialEndpoint, MetorialEndpointManager, MetorialRequest
from ..resources import mapConsumerOauthAuthorizationsListOutput, ConsumerOauthAuthorizationsListOutput, mapConsumerOauthAuthorizationsListQuery, ConsumerOauthAuthorizationsListQuery, mapConsumerOauthAuthorizationsGetOutput, ConsumerOauthAuthorizationsGetOutput, mapConsumerOauthAuthorizationsRevokeOutput, ConsumerOauthAuthorizationsRevokeOutput

class MetorialConsumerOauthAuthorizationsEndpoint(BaseMetorialEndpoint):
    """Inspect and revoke the applications the consumer has authorized."""

    def __init__(self, config: MetorialEndpointManager):
        super().__init__(config)

    def list(self, *, limit: Optional[float] = None, after: Optional[str] = None, before: Optional[str] = None, cursor: Optional[str] = None, order: Optional[str] = None, status: Optional[Union[str, List[str]]] = None) -> ConsumerOauthAuthorizationsListOutput:
        """
    List consumer OAuth authorizations
    Returns the applications the authenticated consumer has authorized.

    :param limit: Optional[float] (optional)
    :param after: Optional[str] (optional)
    :param before: Optional[str] (optional)
    :param cursor: Optional[str] (optional)
    :param order: Optional[str] (optional)
    :param status: Optional[Union[str, List[str]]] (optional)
    :return: ConsumerOauthAuthorizationsListOutput
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
        if status is not None:
            query_dict["status"] = status

        request = MetorialRequest(
            path=['consumer', 'oauth', 'authorizations'],
            query=query_dict
        )
        return self._get(request).transform(mapConsumerOauthAuthorizationsListOutput.from_dict)

    def get(self, oauth_authorization_id: str) -> ConsumerOauthAuthorizationsGetOutput:
        """
    Get consumer OAuth authorization
    Returns an application authorization of the authenticated consumer.

    :param oauth_authorization_id: str
    :return: ConsumerOauthAuthorizationsGetOutput
    """
        request = MetorialRequest(
            path=['consumer', 'oauth', 'authorizations', oauth_authorization_id]
        )
        return self._get(request).transform(mapConsumerOauthAuthorizationsGetOutput.from_dict)

    def revoke(self, oauth_authorization_id: str) -> ConsumerOauthAuthorizationsRevokeOutput:
        """
    Revoke consumer OAuth authorization
    Revokes an application authorization of the authenticated consumer, signing the application out.

    :param oauth_authorization_id: str
    :return: ConsumerOauthAuthorizationsRevokeOutput
    """
        request = MetorialRequest(
            path=['consumer', 'oauth', 'authorizations', oauth_authorization_id, 'revoke']
        )
        return self._post(request).transform(mapConsumerOauthAuthorizationsRevokeOutput.from_dict)