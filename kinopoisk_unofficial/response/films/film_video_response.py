from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.film_video import FilmVideo


@dataclass(frozen=True)
class FilmVideoResponse(Response):
    total: int
    items: List[FilmVideo] = field(default_factory=list)
