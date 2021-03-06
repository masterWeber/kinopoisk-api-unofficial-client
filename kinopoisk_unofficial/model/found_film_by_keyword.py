from dataclasses import dataclass, field
from typing import Optional, List, Union

from kinopoisk_unofficial.model.country import Country
from kinopoisk_unofficial.model.dictonary.film_type import FilmType
from kinopoisk_unofficial.model.genre import Genre


@dataclass
class FoundFilmByKeyword:
    film_id: Optional[int] = None
    name_ru: Optional[str] = None
    name_en: Optional[str] = None
    type: Optional[FilmType] = None
    year: Optional[Union[str, int]] = None
    description: Optional[str] = None
    film_length: Optional[str] = None
    countries: List[Country] = field(default_factory=list)
    genres: List[Genre] = field(default_factory=list)
    rating: Optional[str] = None
    rating_vote_count: Optional[int] = None
    poster_url: Optional[str] = None
    poster_url_preview: Optional[str] = None
