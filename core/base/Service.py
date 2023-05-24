from core.utils import HttpClient


class Service:
    def __init__(self, http: HttpClient):
        self.__http = http

    @property
    def http(self) -> HttpClient:
        return self.__http
