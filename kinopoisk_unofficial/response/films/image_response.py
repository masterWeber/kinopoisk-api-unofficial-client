from dataclasses import dataclass, field
from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.image import Image


@dataclass(frozen=True)
class ImageResponse(Response):
    total: int
    totalPages: int
    items: List[Image] = field(default_factory=list)
