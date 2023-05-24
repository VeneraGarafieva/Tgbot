import json
from datetime import datetime
from dataclasses import dataclass


@dataclass(repr=False, init=False)
class Dataclass:
    def __repr__(self) -> str:
        params = dict()
        for field in dir(self):
            if field.startswith('__'):
                continue
            value = getattr(self, field)
            if callable(value):
                continue
            if isinstance(value, datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
            params[field] = value
        return 'test'
            # json.dumps(params, indent=4, separators=(',', ':'))
