from core.domains import Chat
from core.base import Service, Media


class Video(Service, Media):
    max_local_size: float = 50
    max_url_size: float = 20

    def send(self, file: str, chat: Chat):
        if '/' not in file:
            self.http.request('/sendVideo', data={
                'chat_id': chat.id,
                'video': file
            })
        elif file.lower().startswith('http'):
            if self.check_by_url(file):
                self.http.request('/sendVideo', data={
                    'chat_id': chat.id,
                    'video': file
                })
        elif self.check_by_file(file):
            self.http.request('/sendVideo', data={
                'chat_id': chat.id
            }, files={
                'video': open(file, 'rb')
            })
