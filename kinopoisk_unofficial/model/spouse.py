from dataclasses import dataclass
from typing import Optional

from kinopoisk_unofficial.model.dictonary.sex import Sex


@dataclass
class Spouse:
    person_id: Optional[int] = None
    name: Optional[str] = None
    divorced: Optional[bool] = None
    divorced_reason: Optional[str] = None
    sex: Optional[Sex] = None
    children: Optional[int] = None
    web_url: Optional[str] = None
    relation: Optional[str] = None
