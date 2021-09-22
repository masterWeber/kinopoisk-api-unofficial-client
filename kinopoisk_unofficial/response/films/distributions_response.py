from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.distribution import Distribution


@dataclass(frozen=True)
class DistributionsResponse(Response):
    total: int
    items: List[Distribution] = field(default_factory=list)
