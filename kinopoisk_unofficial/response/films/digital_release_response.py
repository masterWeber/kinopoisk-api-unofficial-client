from dataclasses import dataclass, field

from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.digital_release import DigitalRelease


@dataclass(frozen=True)
class DigitalReleaseResponse(Response):
    page: int
    total: int
    releases: List[DigitalRelease] = field(default_factory=list)
