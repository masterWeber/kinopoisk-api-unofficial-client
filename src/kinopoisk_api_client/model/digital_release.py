from dataclasses import dataclass, field
from datetime import datetime
from typing import Union, List

from src.kinopoisk_api_client.model.country import Country
from src.kinopoisk_api_client.model.genre import Genre


@dataclass
class DigitalRelease:
    film_id: int
    name_ru: str
    name_en: Union[str, None]
    year: int
    poster_url: str
    poster_url_preview: str
    rating: Union[float, None]
    rating_vote_count: int
    expectations_rating: Union[float, None]
    expectations_rating_vote_count: int
    duration: int
    release_date: datetime
    genres: List[Genre] = field(default_factory=list)
    countries: List[Country] = field(default_factory=list)
