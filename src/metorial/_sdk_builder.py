from collections.abc import Callable
from typing import Any, Generic, TypeVar, cast

from metorial._endpoint import MetorialEndpointManager

ConfigT = TypeVar("ConfigT")
ApiVersionT = TypeVar("ApiVersionT")


class MetorialSDKBuilder(Generic[ApiVersionT, ConfigT]):
  def __init__(self, api_name: str, api_version: ApiVersionT) -> None:
    self.api_name = api_name
    self.api_version = api_version
    self._get_api_host: Callable[[ConfigT], str] | None = None
    self._get_headers: Callable[[ConfigT], dict[str, str]] | None = None

  @classmethod
  def create(
    cls, api_name: str, api_version: ApiVersionT
  ) -> "MetorialSDKBuilder[ApiVersionT, ConfigT]":
    return cls(api_name, api_version)

  def set_get_api_host(
    self, get_api_host: Callable[[ConfigT], str]
  ) -> "MetorialSDKBuilder[ApiVersionT, ConfigT]":
    self._get_api_host = get_api_host
    return self

  def set_get_headers(
    self, get_headers: Callable[[ConfigT], dict[str, str]]
  ) -> "MetorialSDKBuilder[ApiVersionT, ConfigT]":
    self._get_headers = get_headers
    return self

  def build(
    self, get_config: Callable[[dict[str, Any]], dict[str, Any]]
  ) -> Callable[
    [Callable[[MetorialEndpointManager], dict[str, Any]]],
    Callable[[dict[str, Any]], dict[str, Any]],
  ]:
    if not self._get_headers:
      raise ValueError("get_headers must be set")
    if not self._get_api_host:
      raise ValueError("api_host must be set")

    def builder(
      get_endpoints: Callable[[MetorialEndpointManager], dict[str, Any]],
    ) -> Callable[[dict[str, Any]], dict[str, Any]]:
      def sdk(config: dict[str, Any]) -> dict[str, Any]:
        full_config = get_config(config)
        get_api_host = cast(Callable[["dict[str, Any]"], str], self._get_api_host)
        get_headers = cast(
          Callable[["dict[str, Any]"], "dict[str, str]"], self._get_headers
        )
        api_host = get_api_host(full_config)
        manager = MetorialEndpointManager(
          full_config,
          api_host,
          get_headers,
          enable_debug_logging=bool(config.get("enableDebugLogging", False)),
        )
        endpoints = get_endpoints(manager)
        result: dict[str, Any] = {"_config": {"apiHost": api_host, **full_config}}
        result.update(endpoints)
        return result

      return sdk

    return builder
