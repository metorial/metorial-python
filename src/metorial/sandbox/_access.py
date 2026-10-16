from __future__ import annotations

import asyncio
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from datetime import datetime, timezone

_EXPIRY_MARGIN_SECONDS = 30


@dataclass
class SandboxAccessGrant:
  url: str
  token: str
  expires_at: datetime | None = None


SandboxAccessProvider = Callable[[], Awaitable[SandboxAccessGrant]]


class SandboxAccessCache:
  def __init__(self, provider: SandboxAccessProvider) -> None:
    self._provider = provider
    self._grant: SandboxAccessGrant | None = None
    self._lock = asyncio.Lock()

  def _is_usable(self, grant: SandboxAccessGrant) -> bool:
    if grant.expires_at is None:
      return True

    expires_at = grant.expires_at
    if expires_at.tzinfo is None:
      expires_at = expires_at.replace(tzinfo=timezone.utc)

    remaining = (expires_at - datetime.now(timezone.utc)).total_seconds()
    return remaining > _EXPIRY_MARGIN_SECONDS

  async def get(self) -> SandboxAccessGrant:
    grant = self._grant
    if grant is not None and self._is_usable(grant):
      return grant

    async with self._lock:
      grant = self._grant
      if grant is not None and self._is_usable(grant):
        return grant

      self._grant = await self._provider()
      return self._grant

  def invalidate(self) -> None:
    self._grant = None
