from dataclasses import field, dataclass
from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.season import Season


@dataclass(frozen=True)
class SeasonsResponse(Response):
    total: int
    items: List[Season] = field(default_factory=list)
