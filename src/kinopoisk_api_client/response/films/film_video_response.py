from dataclasses import dataclass, field

from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.film_video import FilmVideo


@dataclass(frozen=True)
class FilmVideoResponse(Response):
    total: int
    items: List[FilmVideo] = field(default_factory=list)
