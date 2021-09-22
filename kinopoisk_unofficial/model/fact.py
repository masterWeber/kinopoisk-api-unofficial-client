from dataclasses import dataclass

from kinopoisk_unofficial.model.dictonary.fact_type import FactType


@dataclass
class Fact:
    text: str
    type: FactType
    spoiler: bool
