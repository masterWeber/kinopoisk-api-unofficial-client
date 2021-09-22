from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.dictonary.found_film import FoundFilm


@dataclass(frozen=True)
class FilmSearchByFiltersResponse(Response):
    pages_count: int
    films: List[FoundFilm] = field(default_factory=list)
