from dataclasses import dataclass
from typing import Optional

from src.kinopoisk_api_client.model.dictonary.relation_type import RelationType


@dataclass
class RelatedFilm:
    film_id: Optional[int] = None
    name_ru: Optional[str] = None
    name_en: Optional[str] = None
    name_original: Optional[str] = None
    poster_url: Optional[str] = None
    poster_url_preview: Optional[str] = None
    relation_type: Optional[RelationType] = None
