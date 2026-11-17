from __future__ import annotations

import json
import re
from urllib.parse import urlsplit

DEFAULT_API_HOST = "https://api.metorial.com"
BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
TOKEN_PATTERN = re.compile(r"metorial_[a-z]+_[A-Za-z0-9]{60}([A-Za-z0-9]+)v[12]")
MAX_TOKEN_LENGTH = 8192


def api_host_from_token(token: object) -> str | None:
  if not isinstance(token, str) or not token or len(token) > MAX_TOKEN_LENGTH:
    return None

  match = TOKEN_PATTERN.fullmatch(token)
  if match is None:
    return None

  try:
    value = 0
    for character in match[1]:
      value = value * 62 + BASE62_ALPHABET.index(character)

    config = json.loads(
      value.to_bytes((value.bit_length() + 7) // 8, "big").decode("utf-8")
    )
    if (
      not isinstance(config, list)
      or len(config) != 2
      or not isinstance(config[0], str)
      or not isinstance(config[1], str)
      or not config[1]
    ):
      return None

    host = config[0]
    if not re.match(r"https?://", host, re.IGNORECASE) or re.search(r"[\s\\?#]", host):
      return None

    url = urlsplit(host)
    if not url.hostname or url.username is not None or url.password is not None:
      return None
    _ = url.port

    return host
  except (ValueError, UnicodeError):
    return None
