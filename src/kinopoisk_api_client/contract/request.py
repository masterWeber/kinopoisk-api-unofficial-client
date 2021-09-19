from __future__ import annotations
from abc import ABC
from typing import Dict
from urllib.parse import urlencode

from src.kinopoisk_api_client.client.http_method import HttpMethod
from src.kinopoisk_api_client.contract.response import Response


class Request(ABC):
    METHOD: HttpMethod = HttpMethod.GET
    ROUTE: str = '/'
    RESPONSE: type = Response

    def method(self) -> HttpMethod:
        return self.METHOD

    def route(self) -> str:
        return self.ROUTE

    def response_class(self) -> type:
        return self.RESPONSE

    @staticmethod
    def _build_url(url: str, params: Dict) -> str:
        return url + '?' + urlencode(params)
