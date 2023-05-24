from core.base import Event, IncomingMessage
from core import Pythogram


class ActionLocation(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['geo', 'гео']

    def action(self, message: IncomingMessage, *args, **kwargs):
        self.__sender.location.send(
            lat=59.934199,
            lng=30.324456,
            chat=message.chat
        )
