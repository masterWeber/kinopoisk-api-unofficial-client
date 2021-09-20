from typing import Union
import requests
from requests import Response

from src.kinopoisk_api_client.client.http_method import HttpMethod


class HttpClient:
    __base_url: str

    def __init__(self, base_url: str) -> None:
        self.__base_url = base_url

    def request(self, method: HttpMethod, path: str, headers: Union[dict, None] = None) -> Response:
        url = self.__base_url + path

        if method == HttpMethod.GET:
            return requests.get(url=url, headers=headers)
        elif method == HttpMethod.POST:
            return requests.get(url=url, headers=headers)

        return requests.request(method=str(method), url=url, headers=headers)
