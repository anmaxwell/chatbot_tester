from dataclasses import dataclass, field
from typing import Literal
from enum import Enum

import mesop as me

Role = Literal["user", "model"]

@dataclass(kw_only=True)
class ChatMessage:
    role: Role = "user"
    content: str = ""
    in_progress: bool = False

@dataclass
class Conversation:
    model: str = ""
    messages: list[ChatMessage] = field(default_factory=list)

@me.stateclass
class State:
  title: str = "My test chatbot"
  input: str
  output: list[ChatMessage]
  is_open: bool = False
  gemini_api_key: str = ""