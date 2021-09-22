from dataclasses import dataclass, field
from typing import List

from apischema import serializer, deserializer

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.film_sequels_and_prequels import FilmSequelOrPrequel


@dataclass(frozen=True)
class FilmSequelsAndPrequelsResponse(Response):
    items: List[FilmSequelOrPrequel] = field(default_factory=list)


@serializer
def unwrap_film(response: FilmSequelsAndPrequelsResponse) -> List[FilmSequelOrPrequel]:
    return response.items


@deserializer
def wrap_film(items: List[FilmSequelOrPrequel]) -> FilmSequelsAndPrequelsResponse:
    return FilmSequelsAndPrequelsResponse(items)
