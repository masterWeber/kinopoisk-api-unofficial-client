from dataclasses import dataclass, field
from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.premiere_film import PremiereFilm


@dataclass(frozen=True)
class PremiereResponse(Response):
    total: int
    items: List[PremiereFilm] = field(default_factory=list)