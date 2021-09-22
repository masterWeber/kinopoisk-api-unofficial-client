from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.model.dictonary.month import Month
from kinopoisk_unofficial.response.films.digital_release_response import DigitalReleaseResponse


class DigitalReleaseRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v2.1/films/releases'
    RESPONSE: type = DigitalReleaseResponse

    __year: int
    __month: Month
    __page: int

    def __init__(self, year: int, month: Month, page: int = 1) -> None:
        self.__year = year
        self.__month = month
        self.__page = page

    @property
    def year(self) -> int:
        return self.__year

    @property
    def month(self) -> Month:
        return self.__month

    @property
    def page(self) -> int:
        return self.__page

    def path(self) -> str:
        return self._build_url(self.PATH, {
            'year': self.year,
            'month': self.month.value,
            'page': self.page
        })
