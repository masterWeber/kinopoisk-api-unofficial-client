from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.model.dictonary.month import Month
from kinopoisk_unofficial.response.films.premiere_response import PremiereResponse


class PremiereRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v2.2/films/premieres'
    RESPONSE: type = PremiereResponse

    __year: int
    __month: Month

    def __init__(self, year: int, month: Month) -> None:
        self.__year = year
        self.__month = month

    @property
    def year(self) -> int:
        return self.__year

    @property
    def month(self) -> Month:
        return self.__month

    def path(self) -> str:
        return self._build_url(self.PATH, {
            'year': self.year,
            'month': self.month.value
        })
