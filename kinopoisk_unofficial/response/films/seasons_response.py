from dataclasses import field, dataclass
from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.season import Season


@dataclass(frozen=True)
class SeasonsResponse(Response):
    total: int
    items: List[Season] = field(default_factory=list)
