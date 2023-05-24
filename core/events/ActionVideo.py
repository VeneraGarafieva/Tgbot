from core.base import Event, IncomingMessage
from core import Pythogram


class ActionVideo(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ['video', 'видео']

    def action(self, message: IncomingMessage, *args, **kwargs):
        self.__sender.video.send(
            file='/home/bgu-user/code/pythogram/tmp/sample_640x360.mp4',
            chat=message.chat
        )
