from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.top_film import TopFilm


@dataclass(frozen=True)
class FilmTopResponse(Response):
    pages_count: int
    films: List[TopFilm] = field(default_factory=list)
