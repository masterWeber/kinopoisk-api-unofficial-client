from dataclasses import dataclass
from datetime import datetime


@dataclass
class Episode:
    season_number: int
    episode_number: int
    name_ru: str
    name_en: str
    synopsis: str
    release_date: datetime
