from dataclasses import dataclass
from typing import Dict


@dataclass(frozen=True)
class Response:
    status: bool
    message: str = None
    data: Dict = None
