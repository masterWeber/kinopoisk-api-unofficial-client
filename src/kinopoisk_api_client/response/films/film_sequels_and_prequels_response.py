from dataclasses import dataclass, field
from typing import List

from apischema import serializer, deserializer

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.film_sequels_and_prequels import FilmSequelOrPrequel


@dataclass(frozen=True)
class FilmSequelsAndPrequelsResponse(Response):
    items: List[FilmSequelOrPrequel] = field(default_factory=list)


@serializer
def unwrap_film(response: FilmSequelsAndPrequelsResponse) -> List[FilmSequelOrPrequel]:
    return response.items


@deserializer
def wrap_film(items: List[FilmSequelOrPrequel]) -> FilmSequelsAndPrequelsResponse:
    return FilmSequelsAndPrequelsResponse(items)
