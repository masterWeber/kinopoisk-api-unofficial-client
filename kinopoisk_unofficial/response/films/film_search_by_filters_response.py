from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.found_film_by_filters import FoundFilmByFilters


@dataclass(frozen=True)
class FilmSearchByFiltersResponse(Response):
    total: int
    totalPages: int
    items: List[FoundFilmByFilters] = field(default_factory=list)
