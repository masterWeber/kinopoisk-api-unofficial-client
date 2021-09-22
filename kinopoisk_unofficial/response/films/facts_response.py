from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.fact import Fact


@dataclass(frozen=True)
class FactsResponse(Response):
    total: int
    items: List[Fact] = field(default_factory=list)
