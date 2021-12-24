from dataclasses import dataclass, field
from typing import List

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.person import Person


@dataclass(frozen=True)
class PersonByNameResponse(Response):
    total: int
    items: List[Person] = field(default_factory=list)
