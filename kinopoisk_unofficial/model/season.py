from dataclasses import dataclass

from typing import List

from kinopoisk_unofficial.model.episode import Episode


@dataclass
class Season:
    number: int
    episodes: List[Episode]
