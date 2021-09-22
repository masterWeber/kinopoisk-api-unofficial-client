from dataclasses import dataclass
from typing import Union

from kinopoisk_unofficial.model.dictonary.relation_type import RelationType


@dataclass
class FilmSequelOrPrequel:
    film_id: Union[int, None]
    name_ru: Union[str, None]
    name_en: Union[str, None]
    name_original: str
    poster_url: Union[str, None]
    poster_url_preview: Union[str, None]
    relation_type: RelationType
