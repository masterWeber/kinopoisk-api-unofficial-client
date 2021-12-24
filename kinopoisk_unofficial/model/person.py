from dataclasses import dataclass
from typing import Optional

from kinopoisk_unofficial.model.dictonary.sex import Sex


@dataclass
class Person:
    kinopoisk_id: Optional[int] = None
    web_url: Optional[str] = None
    name_ru: Optional[str] = None
    name_en: Optional[str] = None
    sex: Optional[Sex] = None
    poster_url: Optional[str] = None
