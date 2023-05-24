from core.base import Event, IncomingMessage
from core import Pythogram


class ActionRussia(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['аниме']

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = f'Наруто'
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
        self.__sender.photo.send(
            file='https://webmg.ru/wp-content/uploads/2022/09/i-23-26.jpeg',
            chat=message.chat
        )
