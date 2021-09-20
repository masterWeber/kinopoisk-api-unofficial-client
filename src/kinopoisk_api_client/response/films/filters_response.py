from dataclasses import dataclass, field

from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.filter_country import FilterCountry
from src.kinopoisk_api_client.model.filter_genre import FilterGenre


@dataclass(frozen=True)
class FiltersResponse(Response):
    genres: List[FilterGenre] = field(default_factory=list)
    countries: List[FilterCountry] = field(default_factory=list)
