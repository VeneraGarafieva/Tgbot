from core.base import Event, IncomingMessage
from core import Pythogram
import random
from core.events.Taro import *


class ActionFortune(Event):
    def __init__(self, sender: Pythogram):
        self.__sender = sender

    def check(self, message: IncomingMessage, *args, **kwargs) -> bool:
        text = message.text.strip().lower()
        return text in ["Разложи мне на сегодня", "сегодня", "погадай"]

    def action(self, message: IncomingMessage, *args, **kwargs):
        random.shuffle(taro_deck)
        text = f"Ваша карта на сегодня: {taro_deck[0].get('name')}. Совет дня: {taro_deck[0].get('advise')}"
        self.__sender.message.send(
            text=text,
            chat=message.chat
        )
        self.__sender.photo.send(
            file=taro_deck[0].get("picture"),
            chat=message.chat
        )