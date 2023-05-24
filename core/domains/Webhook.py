from dataclasses import dataclass
from core.base import Dataclass


@dataclass
class Webhook(Dataclass.__class__):
    url: str
    has_certificate: bool = False

