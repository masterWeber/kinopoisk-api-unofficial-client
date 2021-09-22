from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.filter_country import FilterCountry
from kinopoisk_unofficial.model.filter_genre import FilterGenre


@dataclass(frozen=True)
class FiltersResponse(Response):
    genres: List[FilterGenre] = field(default_factory=list)
    countries: List[FilterCountry] = field(default_factory=list)
