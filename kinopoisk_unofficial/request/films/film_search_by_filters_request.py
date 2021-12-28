from typing import List, Optional

from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.model.dictonary.film_type import FilmType
from kinopoisk_unofficial.model.filter_country import FilterCountry
from kinopoisk_unofficial.model.filter_genre import FilterGenre
from kinopoisk_unofficial.model.filter_order import FilterOrder
from kinopoisk_unofficial.response.films.film_search_by_filters_response import FilmSearchByFiltersResponse


class FilmSearchByFiltersRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v2.2/films'
    RESPONSE: type = FilmSearchByFiltersResponse

    __countries: List[FilterCountry] = []
    __genres: List[FilterGenre] = []
    __order: Optional[FilterOrder] = None
    __type: Optional[FilmType] = None
    __rating_from: Optional[int] = None
    __rating_to: Optional[int] = None
    __year_from: Optional[int] = None
    __year_to: Optional[int] = None
    __imdb_id: Optional[str] = None
    __keyword: Optional[str] = None
    __page: int = 1

    @property
    def countries(self) -> List[FilterCountry]:
        return self.__countries

    @countries.setter
    def countries(self, countries: List[FilterCountry]) -> None:
        self.__countries = countries

    def add_country(self, country: FilterCountry) -> None:
        self.__countries.append(country)

    @property
    def genres(self) -> List[FilterGenre]:
        return self.__genres

    @genres.setter
    def genres(self, genres: List[FilterGenre]) -> None:
        self.__genres = genres

    def add_genre(self, genre: FilterGenre) -> None:
        self.__genres.append(genre)

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
    def imdb_id(self) -> Optional[str]:
        return self.__imdb_id

    @imdb_id.setter
    def imdb_id(self, imdb_id: Optional[str]) -> None:
        self.__imdb_id = imdb_id

    @property
    def keyword(self) -> Optional[str]:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: Optional[str]) -> None:
        self.__keyword = keyword

    @property
    def page(self) -> int:
        return self.__page

    @page.setter
    def page(self, page: Optional[int]) -> None:
        self.__page = page

    def path(self) -> str:
        options = {
            'countries': ','.join(str(c.id) for c in self.countries),
            'genres': ','.join(str(g.id) for g in self.genres),
            'order': self.order.value if self.order is not None else None,
            'type': self.type.value if self.type is not None else None,
            'ratingFrom': self.rating_from,
            'ratingTo': self.rating_to,
            'yearFrom': self.year_from,
            'yearTo': self.year_to,
            'imdbId': self.imdb_id,
            'keyword': self.keyword,
            'page': self.page
        }

        for key, value in dict(options).items():
            if value is None \
                    or (type(value) == list and len(value) == 0):
                del options[key]

        return self._build_url(self.PATH, options)
