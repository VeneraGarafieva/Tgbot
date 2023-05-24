from core.domains import Chat
from core.base import Service


class Message(Service):
    def send(self, text: str, chat: Chat):
        response = self.http.request('/sendMessage', data={
            'chat_id': chat.id,
            'text': text
        })
