from dataclasses import dataclass, field

from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.found_film import FoundFilm


@dataclass(frozen=True)
class FilmSearchByFiltersResponse(Response):
    pages_count: int
    films: List[FoundFilm] = field(default_factory=list)
