from dataclasses import dataclass, field
from typing import Optional, List

from kinopoisk_unofficial.model.country import Country
from kinopoisk_unofficial.model.dictonary.film_type import FilmType
from kinopoisk_unofficial.model.genre import Genre


@dataclass
class FoundFilm:
    kinopoisk_id: Optional[int] = None
    imdb_id: Optional[str] = None
    name_ru: Optional[str] = None
    name_en: Optional[str] = None
    name_original: Optional[str] = None
    countries: List[Country] = field(default_factory=list)
    genres: List[Genre] = field(default_factory=list)
    rating_kinopoisk: Optional[float] = None
    rating_imdb: Optional[float] = None
    year: Optional[int] = None
    type: Optional[FilmType] = None
    film_length: Optional[str] = None
    poster_url: Optional[str] = None
    poster_url_preview: Optional[str] = None
