from dataclasses import dataclass, field
from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.found_film_by_keyword import FoundFilmByKeyword


@dataclass(frozen=True)
class SearchByKeywordResponse(Response):
    keyword: str
    pages_count: int
    search_films_count_result: int
    films: List[FoundFilmByKeyword] = field(default_factory=list)
