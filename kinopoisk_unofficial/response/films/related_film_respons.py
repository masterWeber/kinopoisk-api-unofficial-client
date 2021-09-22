from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.related_film import RelatedFilm


@dataclass(frozen=True)
class RelatedFilmResponse(Response):
    total: int
    items: List[RelatedFilm] = field(default_factory=list)
