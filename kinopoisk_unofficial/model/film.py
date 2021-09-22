from dataclasses import dataclass
from typing import List, Optional, Union

from kinopoisk_unofficial.model.country import Country
from kinopoisk_unofficial.model.dictonary.film_type import FilmType
from kinopoisk_unofficial.model.dictonary.production_status import ProductionStatus
from kinopoisk_unofficial.model.genre import Genre


@dataclass
class Film:
    kinopoisk_id: int
    imdb_id: str
    name_ru: str
    name_en: Union[str, None]
    name_original: str
    poster_url: str
    poster_url_preview: str
    reviews_count: int
    rating_good_review: float
    rating_good_review_vote_count: int
    rating_kinopoisk: float
    rating_kinopoisk_vote_count: int
    rating_imdb: float
    rating_imdb_vote_count: int
    rating_film_critics: float
    rating_film_critics_vote_count: int
    rating_await: Union[float, None]
    rating_await_count: int
    rating_rf_critics: Union[float, None]
    rating_rf_critics_vote_count: int
    year: int
    film_length: int
    is_tickets_available: bool
    production_status: Union[ProductionStatus, None]
    type: FilmType
    has_imax: bool
    has_3_d: bool
    countries: List[Country]
    genres: List[Genre]
    start_year: Union[int, None]
    end_year: Union[int, None]
    web_url: Optional[str] = None
    slogan: Optional[str] = None
    description: Optional[str] = None
    short_description: Optional[str] = None
    editor_annotation: Optional[str] = None
    rating_mpaa: Optional[str] = None
    rating_age_limits: Optional[str] = None
    last_sync: Optional[str] = None
    serial: Optional[bool] = None
    short_film: Optional[bool] = None
    completed: Optional[bool] = None
