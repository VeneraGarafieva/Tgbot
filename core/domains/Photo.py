from dataclasses import dataclass
from core.base import Dataclass


@dataclass
class Photo(Dataclass.__class__):
    id: str
    unique_id: str
    size: int = 0
    width: int = 0
    height: int = 0

