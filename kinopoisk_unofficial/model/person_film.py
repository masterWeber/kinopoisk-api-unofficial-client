from dataclasses import dataclass
from typing import Optional

from kinopoisk_unofficial.model.dictonary.profession_key import ProfessionKey


@dataclass
class PersonFilm:
    film_id: Optional[int] = None
    name_ru: Optional[str] = None
    name_en: Optional[str] = None
    rating: Optional[str] = None
    general: Optional[bool] = None
    description: Optional[str] = None
    profession_key: Optional[ProfessionKey] = None
