from core.domains import Chat
from core.base import Service


class Location(Service):
    def send(self, lat: float, lng: float, chat: Chat, live_period: int = None):
        data = {
            'chat_id': chat.id,
            'latitude': lat,
            'longitude': lng
        }
        if isinstance(live_period, int):
            if 60 <= live_period <= 86400:
                data['live_period'] = live_period

        response = self.http.request('/sendLocation', data=data)
