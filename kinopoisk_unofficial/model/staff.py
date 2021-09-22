from dataclasses import dataclass
from typing import Union

from kinopoisk_unofficial.model.dictonary.profession_key import ProfessionKey


@dataclass
class Staff:
    staff_id: int
    name_ru: str
    name_en: str
    description: Union[str, None]
    poster_url: str
    profession_text: str
    profession_key: ProfessionKey
