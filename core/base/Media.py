from os import path
import requests


class Media:
    max_local_size: float = 1
    max_url_size: float = 1

    @classmethod
    def check_by_file(cls, file: str) -> bool:
        if not path.exists(file) or not path.isfile(file):
            return False
        size = path.getsize(file)
        if size / 1024 ** 2 > cls.max_local_size:
            return False
        return True

    @classmethod
    def check_by_url(cls, url: str) -> bool:
        if not url.lower().startswith('http'):
            return False
        try:
            request = requests.head(url)
            if not request or not request.headers:
                return False
            size = int(request.headers.get('Content-Length', 0))
            if size / 1024 ** 2 > cls.max_url_size:
                return False
            return True
        except:
            return False

