from typing import List, Optional

from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.model.dictonary.film_type import FilmType
from kinopoisk_unofficial.model.filter_order import FilterOrder
from kinopoisk_unofficial.response.films.film_search_by_filters_response import FilmSearchByFiltersResponse


class FilmSearchByFiltersRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v2.1/films/search-by-filters'
    RESPONSE: type = FilmSearchByFiltersResponse

    __country: List[int] = []
    __genre: List[int] = []
    __order: Optional[FilterOrder] = None
    __type: Optional[FilmType] = None
    __rating_from: Optional[int] = None
    __rating_to: Optional[int] = None
    __year_from: Optional[int] = None
    __year_to: Optional[int] = None
    __page: int = 1

    @property
    def country(self) -> List[int]:
        return self.__country

    @country.setter
    def country(self, country: List[int]) -> None:
        self.__country = country

    @property
    def genre(self) -> List[int]:
        return self.__genre

    @genre.setter
    def genre(self, genre: List[int]) -> None:
        self.__genre = genre

    @property
    def order(self) -> Optional[FilterOrder]:
        return self.__order

    @order.setter
    def order(self, order: Optional[FilterOrder]) -> None:
        self.__order = order

    @property
    def type(self) -> Optional[FilmType]:
        return self.__type

    @type.setter
    def type(self, film_type: Optional[FilmType]) -> None:
        self.__type = film_type

    @property
    def rating_from(self) -> Optional[int]:
        return self.__rating_from

    @rating_from.setter
    def rating_from(self, rating_from: Optional[int]) -> None:
        self.__rating_from = rating_from

    @property
    def rating_to(self) -> Optional[int]:
        return self.__rating_to

    @rating_to.setter
    def rating_to(self, rating_from: Optional[int]) -> None:
        self.__rating_to = rating_from

    @property
    def year_from(self) -> Optional[int]:
        return self.__year_from

    @year_from.setter
    def year_from(self, year_from: Optional[int]) -> None:
        self.__year_from = year_from

    @property
    def year_to(self) -> Optional[int]:
        return self.__year_to

    @year_to.setter
    def year_to(self, year_to: Optional[int]) -> None:
        self.__year_to = year_to

    @property
    def page(self) -> int:
        return self.__page

    def path(self) -> str:
        options = {
            'country': ','.join(str(c) for c in self.country),
            'genre': ','.join(str(g) for g in self.genre),
            'order': self.order.value if self.order is not None else None,
            'type': self.type.value if self.type is not None else None,
            'ratingFrom': self.rating_from,
            'ratingTo': self.rating_to,
            'yearFrom': self.year_from,
            'yearTo': self.year_to,
            'page': self.page
        }

        for key, value in dict(options).items():
            if value is None \
                    or (type(value) == list and len(value) == 0):
                del options[key]

        return self._build_url(self.PATH, options)
