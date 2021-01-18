from os import getenv
from typing import List


class Config:
    def __init__(self):
        ania_service = self.require_env('ANIA_ASYNC')
        janek_service = self.require_env('JANEK_ASYNC')
        magda_service = self.require_env('MAGDA_ASYNC')
        michal_service = self.require_env('MICHAL_ASYNC')
        self.services: List[str] = [
            ania_service,
            janek_service,
            magda_service,
            michal_service,
        ]

    @staticmethod
    def require_env(env) -> str:
        value = getenv(env)
        assert value is not None, f"{env} is not set"
        return value
