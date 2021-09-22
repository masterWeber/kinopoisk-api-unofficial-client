from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.box_office import BoxOffice


@dataclass(frozen=True)
class BoxOfficeResponse(Response):
    total: int
    items: List[BoxOffice] = field(default_factory=list)
