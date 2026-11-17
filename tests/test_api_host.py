from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import Mock

import pytest

from metorial._api_host import DEFAULT_API_HOST, api_host_from_token
from metorial._base import MetorialBase
from metorial._endpoint import MetorialEndpointManager, MetorialRequest
from metorial._magnetar_sdk import create_magnetar_sdk
from metorial._sdk_shared import get_api_host

FIXTURES = json.loads(
  (Path(__file__).parents[1] / "testdata/api-key-hosts.json").read_text()
)


@pytest.mark.parametrize("fixture", FIXTURES, ids=lambda fixture: fixture["name"])
def test_api_host_vectors(fixture):
  token, host = fixture["token"], fixture["host"]

  assert api_host_from_token(token) == host
  assert get_api_host({"apiKey": token}) == (host or DEFAULT_API_HOST)
  assert get_api_host({"apiKey": token, "apiHost": "https://override.test"}) == (
    "https://override.test"
  )


@pytest.mark.parametrize(
  "api_host, expected",
  [(None, "https://metorial.test/v1"), (DEFAULT_API_HOST, DEFAULT_API_HOST), ("", "")],
)
@pytest.mark.parametrize("dictionary", [False, True])
async def test_base_client_precedence(api_host, expected, dictionary):
  token = FIXTURES[0]["token"]
  client = (
    MetorialBase({"apiKey": token, "apiHost": api_host})
    if dictionary
    else MetorialBase(token, api_host=api_host)
  )

  try:
    assert client._config_data["apiHost"] == expected
  finally:
    await client._http_client.aclose()


async def test_mcp_host_does_not_replace_explicit_api_host():
  client = MetorialBase(
    FIXTURES[0]["token"],
    api_host=DEFAULT_API_HOST,
    mcp_host="https://custom.connect.test",
  )

  try:
    assert client._config_data["apiHost"] == DEFAULT_API_HOST
    assert client._config_data["mcpHost"] == "https://custom.connect.test"
  finally:
    await client._http_client.aclose()


def test_default_and_oversized_token():
  assert get_api_host({}) == DEFAULT_API_HOST
  assert api_host_from_token("metorial_sk_" + "A" * 8192 + "v2") is None


@pytest.mark.parametrize("token", [None, 123, {}, []])
def test_non_string_token_falls_back(token):
  assert get_api_host({"apiKey": token}) == DEFAULT_API_HOST


@pytest.mark.parametrize("api_host", [None, "https://override.test"])
def test_generated_sdk_records_resolved_host(api_host):
  sdk = create_magnetar_sdk({"apiKey": FIXTURES[0]["token"], "apiHost": api_host})

  assert sdk._config["apiHost"] == (api_host or "https://metorial.test/v1")


def test_request_preserves_path_and_credentials(monkeypatch):
  token = FIXTURES[0]["token"]
  request = Mock(return_value=Mock(status_code=200, json=dict))
  monkeypatch.setattr("requests.request", request)
  manager = MetorialEndpointManager(
    {"apiKey": token},
    get_api_host({"apiKey": token}),
    lambda config: {"Authorization": f"Bearer {config['apiKey']}"},
  )

  manager._request("GET", MetorialRequest(path=["instance"]))

  assert request.call_args.args == ("GET", "https://metorial.test/v1/instance")
  assert request.call_args.kwargs["headers"]["Authorization"] == f"Bearer {token}"
