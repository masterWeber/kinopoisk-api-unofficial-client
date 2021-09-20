from dataclasses import dataclass, field

from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.digital_release import DigitalRelease


@dataclass(frozen=True)
class DigitalReleaseResponse(Response):
    page: int
    total: int
    releases: List[DigitalRelease] = field(default_factory=list)
