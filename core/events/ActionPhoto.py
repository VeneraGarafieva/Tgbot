from core.base import Event, IncomingMessage
from core import Pythogram


class ActionPhoto(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        return bool(message.photos)

    def action(self, message: IncomingMessage, *args, **kwargs):
        text = f'Ты прислал мне фотку с текстом {message.text}'
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
        photos = list(filter(lambda item: item.width == 320, message.photos))
        if len(photos):
            photo = photos.pop(0)
            self.__sender.photo.send(
                file=photo.id,
                chat=message.chat
            )
