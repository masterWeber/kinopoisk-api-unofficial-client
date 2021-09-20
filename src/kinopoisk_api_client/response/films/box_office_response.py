from dataclasses import dataclass, field

from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.box_office import BoxOffice


@dataclass(frozen=True)
class BoxOfficeResponse(Response):
    total: int
    items: List[BoxOffice] = field(default_factory=list)
