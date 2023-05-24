from dataclasses import dataclass
from core.base import Dataclass


@dataclass
class Chat(Dataclass.__class__):
    id: int
    is_private: bool = False


