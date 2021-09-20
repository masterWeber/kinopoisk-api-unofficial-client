from dataclasses import dataclass, field

from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.related_film import RelatedFilm


@dataclass(frozen=True)
class RelatedFilmResponse(Response):
    total: int
    items: List[RelatedFilm] = field(default_factory=list)
