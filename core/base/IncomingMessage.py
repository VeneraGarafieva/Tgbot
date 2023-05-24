from typing import List
from dataclasses import dataclass
from datetime import datetime
from core.domains import User, Chat, Photo
from core.base import Dataclass


@dataclass(repr=True)
class IncomingMessage(Dataclass.__class__):
    id: int
    date: datetime
    text: str = None
    user: User = None
    chat: Chat = None
    photos: List[Photo] = None


