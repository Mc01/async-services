from urllib.parse import urljoin

from .request_parser import RequestParser


class Service:
    def __init__(self, endpoint: str, location: str, request_parser: RequestParser):
        self.endpoint = endpoint
        self.location = location
        self.request_parser = request_parser

    @property
    def url(self) -> str:
        return urljoin(self.endpoint, self.location)
