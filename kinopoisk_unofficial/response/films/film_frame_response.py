from dataclasses import dataclass, field
from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.film_frame import FilmFrame


@dataclass(frozen=True)
class FilmFrameResponse(Response):
    frames: List[FilmFrame] = field(default_factory=list)
