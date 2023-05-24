from dataclasses import dataclass
from core.base import Dataclass


@dataclass
class User(Dataclass.__class__):
    id: int
    is_premium: bool = False
    is_bot: bool = False
    first_name: str = None
    last_name: str = None
    username: str = None
    language_code: str = None
