from datetime import datetime
from typing import Dict
from core.utils import HttpClient
from core.services import Webhook as WebhookService
from core.services import Message as MessageService
from core.services import Photo as PhotoService
from core.services import Location as LocationService
from core.services import Video as VideoService
from core.base import IncomingMessage
from core.domains import User, Chat, Photo


class Pythogram:
    url: str = 'https://api.telegram.org/bot'

    def __init__(self, token: str):
        self.__token = token
        http_client = HttpClient(f'{self.url}{token}')
        self.__webhook = WebhookService(http_client)
        self.__message = MessageService(http_client)
        self.__photo = PhotoService(http_client)
        self.__video= VideoService(http_client)
        self.__location = LocationService(http_client)

    @property
    def webhook(self) -> WebhookService:
        return self.__webhook

    @property
    def message(self) -> MessageService:
        return self.__message

    @property
    def photo(self) -> PhotoService:
        return self.__photo

    @property
    def video(self) -> VideoService:
        return self.__video

    @property
    def location(self) -> LocationService:
        return self.__location

    @staticmethod
    def parse_message(data: Dict) -> IncomingMessage | None:
        message = IncomingMessage(
            id=int(data.get('message_id', 0)),
            date=datetime.fromtimestamp(
                data.get('date', 0)
            ),
            text=data.get('text', data.get('caption', ''))
        )
        if data.get('from'):
            _from = data.get('from')
            message.user = User(
                id=_from.get('id'),
                is_bot=_from.get('is_bot', False),
                is_premium=_from.get('is_premium', False),
                first_name=_from.get('first_name'),
                last_name=_from.get('last_name'),
                username=_from.get('username'),
                language_code=_from.get('language_code')
            )
        if data.get('chat'):
            chat = data.get('chat')
            message.chat = Chat(
                id=chat.get('id'),
                is_private=chat.get('type') == 'private'
            )
        if data.get('photo'):
            photos = list()
            for item in data.get('photo', list()):
                photos.append(
                    Photo(
                        id=item.get('file_id'),
                        unique_id=item.get('file_unique_id'),
                        size=int(item.get('file_size')),
                        width=int(item.get('width')),
                        height=int(item.get('height'))
                    )
                )
            message.photos = photos
        return message
