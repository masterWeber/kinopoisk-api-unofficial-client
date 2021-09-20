from typing import Optional

from src.kinopoisk_api_client.client.http_method import HttpMethod
from src.kinopoisk_api_client.contract.request import Request
from src.kinopoisk_api_client.model.dictonary.top_type import TopType
from src.kinopoisk_api_client.response.films.film_top_response import FilmTopResponse


class FilmTopRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v2.2/films/top'
    RESPONSE: type = FilmTopResponse

    __top_type: Optional[TopType]
    __page: int

    def __init__(self, top_type: TopType, page: int = 1) -> None:
        self.__top_type = top_type
        self.__page = page

    @property
    def top_type(self) -> Optional[TopType]:
        return self.__top_type

    @property
    def page(self) -> int:
        return self.__page

    def path(self) -> str:
        options = {'page': self.page}
        if self.top_type is not None:
            options.type = str(self.top_type)

        return self._build_url(self.PATH, options)
