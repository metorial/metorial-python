"""
Shared message conversion utilities for provider adapters.

This module provides common functionality for converting messages between
the standardized ChatMessage format and provider-specific formats.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
  from .base import ChatMessage


def convert_messages_to_openai(messages: list[ChatMessage]) -> list[dict[str, Any]]:
  """Convert ChatMessages to OpenAI message format.

  Args:
      messages: List of standardized ChatMessage objects

  Returns:
      List of OpenAI-format message dicts
  """
  openai_messages: list[dict[str, Any]] = []
  for msg in messages:
    openai_msg: dict[str, Any] = {"role": msg.role}
    if msg.content is not None:
      openai_msg["content"] = msg.content
    if msg.tool_calls:
      openai_msg["tool_calls"] = msg.tool_calls
    if msg.tool_call_id:
      openai_msg["tool_call_id"] = msg.tool_call_id
    openai_messages.append(openai_msg)
  return openai_messages


def convert_messages_to_anthropic(
  messages: list[ChatMessage],
) -> list[dict[str, Any]]:
  """Convert ChatMessages to Anthropic message format.

  Note: Anthropic uses "user" role for tool results instead of "tool".

  Args:
      messages: List of standardized ChatMessage objects

  Returns:
      List of Anthropic-format message dicts
  """
  anthropic_messages: list[dict[str, Any]] = []
  for msg in messages:
    if msg.role == "tool":
      # Anthropic uses "user" role for tool results
      anthropic_messages.append({"role": "user", "content": msg.content or ""})
    else:
      anthropic_msg: dict[str, Any] = {"role": msg.role}
      if msg.content is not None:
        anthropic_msg["content"] = msg.content
      anthropic_messages.append(anthropic_msg)
  return anthropic_messages


def convert_messages_to_google(messages: list[ChatMessage]) -> list[dict[str, Any]]:
  """Convert ChatMessages to Google Generative AI message format.

  Note: Google uses "model" role instead of "assistant".

  Args:
      messages: List of standardized ChatMessage objects

  Returns:
      List of Google-format message dicts
  """
  google_messages: list[dict[str, Any]] = []
  for msg in messages:
    role = "model" if msg.role == "assistant" else msg.role
    google_msg: dict[str, Any] = {"role": role}
    if msg.content is not None:
      google_msg["parts"] = [{"text": msg.content}]
    google_messages.append(google_msg)
  return google_messages


def extract_openai_tool_calls(response: Any) -> list[dict[str, Any]]:
  """Extract tool calls from OpenAI response format.

  Args:
      response: OpenAI API response

  Returns:
      List of standardized tool call dicts
  """
  tool_calls: list[dict[str, Any]] = []
  if response.choices and response.choices[0].message.tool_calls:
    for tool_call in response.choices[0].message.tool_calls:
      tool_calls.append(
        {
          "id": tool_call.id,
          "type": tool_call.type,
          "function": {
            "name": tool_call.function.name,
            "arguments": tool_call.function.arguments,
          },
        }
      )
  return tool_calls


def extract_anthropic_tool_calls(response: Any) -> list[dict[str, Any]]:
  """Extract tool calls from Anthropic response format.

  Args:
      response: Anthropic API response

  Returns:
      List of standardized tool call dicts
  """
  tool_calls: list[dict[str, Any]] = []
  if response.content:
    for content_block in response.content:
      if hasattr(content_block, "type") and content_block.type == "tool_use":
        tool_calls.append(
          {
            "id": content_block.id,
            "type": "function",
            "function": {
              "name": content_block.name,
              "arguments": str(content_block.input),
            },
          }
        )
  return tool_calls


def deduplicate_tools(
  tools: list[dict[str, Any]], key: str = "name"
) -> list[dict[str, Any]]:
  """Remove duplicate tools based on a key field.

  Args:
      tools: List of tool dicts
      key: Field to use for deduplication (default: "name")

  Returns:
      List with duplicates removed (keeps last occurrence)
  """
  return list({t[key]: t for t in tools}.values())


__all__ = [
  "convert_messages_to_openai",
  "convert_messages_to_anthropic",
  "convert_messages_to_google",
  "extract_openai_tool_calls",
  "extract_anthropic_tool_calls",
  "deduplicate_tools",
]
