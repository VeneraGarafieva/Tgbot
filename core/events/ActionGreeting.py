from core.base import Event, IncomingMessage
from core import Pythogram


class ActionGreeting(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['hi', 'hello', 'привет', 'хай']

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = f'Hello, {message.user.username.capitalize()}! How are you?'
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
