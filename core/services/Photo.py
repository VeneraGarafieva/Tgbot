from core.domains import Chat
from core.base import Service, Media


class Photo(Service, Media):
    max_local_size: float = 10
    max_url_size: float = 5

    def send(self, file: str, chat: Chat):
        if '/' not in file:
            self.http.request('/sendPhoto', data={
                'chat_id': chat.id,
                'photo': file
            })
        elif file.lower().startswith('http'):
            if self.check_by_url(file):
                self.http.request('/sendPhoto', data={
                    'chat_id': chat.id,
                    'photo': file
                })
        elif self.check_by_file(file):
            self.http.request('/sendPhoto', data={
                'chat_id': chat.id
            }, files={
                'photo': open(file, 'rb')
            })