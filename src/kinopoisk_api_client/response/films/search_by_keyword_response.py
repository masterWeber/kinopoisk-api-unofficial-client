from dataclasses import dataclass, field
from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.found_film import FoundFilm


@dataclass(frozen=True)
class SearchByKeywordResponse(Response):
    keyword: str
    pages_count: int
    search_films_count_result: int
    films: List[FoundFilm] = field(default_factory=list)
