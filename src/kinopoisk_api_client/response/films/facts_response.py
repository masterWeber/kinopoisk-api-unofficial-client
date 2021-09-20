from dataclasses import dataclass, field

from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.fact import Fact


@dataclass(frozen=True)
class FactsResponse(Response):
    total: int
    items: List[Fact] = field(default_factory=list)
