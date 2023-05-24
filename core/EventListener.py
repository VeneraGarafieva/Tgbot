from core.base import Event


class EventListener:
    def __init__(self):
        self.__events = dict()

    def subscribe(self, event: Event):
        self.__events[event.id] = event

    def unsubscribe(self, event):
        if event.id in self.__events:
            del self.__events[event.id]

    def call(self, *args, **kwargs):
        for event in self.__events.values():
            if event.check(*args, **kwargs):
                event.action(*args, **kwargs)