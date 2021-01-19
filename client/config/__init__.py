from os import getenv
from typing import List

from integrations import Service
from integrations.parsers import (
    AniaRequestParser,
    JanekRequestParser,
    MagdaRequestParser,
    MichalRequestParser,
)


class Config:
    def __init__(self):
        ania_service = Service(
            name='Ania',
            endpoint=self.require_env('ANIA_ASYNC'),
            location='/api/',
            request_parser=AniaRequestParser(),
        )
        janek_service = Service(
            name='Janek',
            endpoint=self.require_env('JANEK_ASYNC'),
            location='/firstone/',
            request_parser=JanekRequestParser(),
        )
        magda_service = Service(
            name='Magda',
            endpoint=self.require_env('MAGDA_ASYNC'),
            location='/api/',
            request_parser=MagdaRequestParser(),
        )
        michal_service = Service(
            name='Michal',
            endpoint=self.require_env('MICHAL_ASYNC'),
            location='/api/',
            request_parser=MichalRequestParser()
        )
        self.services: List[Service] = [
            # ania_service,
            # janek_service,
            # magda_service,
            michal_service,
        ]

    @staticmethod
    def require_env(env) -> str:
        value = getenv(env)
        assert value is not None, f"{env} is not set"
        return value
