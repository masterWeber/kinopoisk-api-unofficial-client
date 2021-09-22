from dataclasses import dataclass, field

from typing import List, Union

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.dictonary.sex import Sex
from kinopoisk_unofficial.model.person_film import PersonFilm
from kinopoisk_unofficial.model.spouse import Spouse


@dataclass(frozen=True)
class PersonResponse(Response):
    personId: int
    webUrl: str
    nameRu: str
    nameEn: str
    sex: Sex
    posterUrl: str
    growth: int
    birthday: str
    death: Union[str, None]
    age: int
    birthplace: str
    deathplace: Union[str, None]
    hasAwards: int
    profession: str
    facts: List[str] = field(default_factory=list)
    spouses: List[Spouse] = field(default_factory=list)
    films: List[PersonFilm] = field(default_factory=list)
