import requests
from typing import Dict
from time import sleep
from core.base import Response


class HttpClient:
    def __init__(self, base_url: str):
        self.__base_url = base_url

    @property
    def base_url(self) -> str:
        return self.__base_url

    def request(self, path: str, data: Dict = None, files: Dict = None, **opt) -> Response:
        total = 3
        count = 0
        while count < total:
            if not files:
                query = requests.post(
                    url=self.base_url + path,
                    json=data
                )
            else:
                query = requests.post(
                    url=self.base_url + path,
                    params=data,
                    files=files
                )
            if not query:
                return Response(
                    status=False,
                    message='Empty data'
                )
            if query.status_code == 429:
                sleep(1)
                count += 1
                continue
            data = query.json()
            if data.get('ok', False):
                return Response(
                    status=True,
                    data=data.get('result', dict())
                )
            return Response(
                status=False,
                message='Response ok = False'
            )
        return Response(
            status=False,
            message='Can not getting data'
        )
