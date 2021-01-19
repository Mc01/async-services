from dataclasses import dataclass
from urllib.parse import urljoin

from .request_parser import RequestParser


@dataclass
class Service:
    name: str
    endpoint: str
    location: str
    request_parser: RequestParser

    @property
    def url(self) -> str:
        return urljoin(self.endpoint, self.location)
