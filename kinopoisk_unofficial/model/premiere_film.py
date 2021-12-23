from datetime import datetime
from dataclasses import dataclass, field
from typing import List

from kinopoisk_unofficial.model.country import Country
from kinopoisk_unofficial.model.genre import Genre


@dataclass
class PremiereFilm:
    kinopoisk_id: int
    name_ru: str
    name_en: str
    year: int
    poster_url: str
    poster_url_preview: str
    duration: int
    premiereRu: datetime
    countries: List[Country] = field(default_factory=list)
    genres: List[Genre] = field(default_factory=list)
