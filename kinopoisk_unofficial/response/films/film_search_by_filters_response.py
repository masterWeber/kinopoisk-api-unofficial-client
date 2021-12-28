from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.found_film import FoundFilm


@dataclass(frozen=True)
class FilmSearchByFiltersResponse(Response):
    total: int
    totalPages: int
    items: List[FoundFilm] = field(default_factory=list)
