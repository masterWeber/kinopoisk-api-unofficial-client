from dataclasses import dataclass

from typing import List

from src.kinopoisk_api_client.model.episode import Episode


@dataclass
class Season:
    number: int
    episodes: List[Episode]
