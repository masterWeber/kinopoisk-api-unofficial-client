from abc import ABC
from typing import Union, Any

from src.kinopoisk_api_client.client.exception.bad_request import BadRequest
from src.kinopoisk_api_client.client.exception.not_found import NotFound
from src.kinopoisk_api_client.client.exception.too_many_requests import TooManyRequests
from src.kinopoisk_api_client.client.exception.unauthorized import Unauthorized
from src.kinopoisk_api_client.client.http_client import HttpClient
from src.kinopoisk_api_client.contract.request import Request
from src.kinopoisk_api_client.contract.response import Response


class ApiClient(ABC):
    __http_client: HttpClient
    __token: str

    def __init__(
            self,
            http_client: HttpClient,
            serializer,
            token: str
    ) -> None:
        self.__http_client = http_client
        self.__serializer = serializer
        self.__token = token

    def _send_request(self, request: Request) -> Union[Response, Any]:
        method = request.method()
        address = request.route()
        headers = {'X-API-KEY': self.__token}

        response = self.__http_client.request(method, address, headers)

        if response.status_code != 200:

            if response.status_code == 400:
                raise BadRequest()
            elif response.status_code == 401:
                raise Unauthorized()
            elif response.status_code == 404:
                raise NotFound()
            elif response.status_code == 429:
                raise TooManyRequests()

        return self.__deserialize_response(
            response.json(),
            request.response_class()
        )

    def __deserialize_response(
            self,
            response_body: dict,
            response_class: type
    ) -> Response:
        return self.__serializer.deserialize(response_class, response_body)
