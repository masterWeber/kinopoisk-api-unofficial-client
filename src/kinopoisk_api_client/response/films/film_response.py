from dataclasses import dataclass, field

from apischema import deserializer, serializer
from apischema.conversions import identity
from apischema.metadata import conversion

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.film import Film


@dataclass(frozen=True)
class FilmResponse(Response):
    film: Film = field(
        metadata=conversion(deserialization=identity, serialization=identity)
    )


@serializer
def unwrap_film(film_response: FilmResponse) -> Film:
    return film_response.film


@deserializer
def wrap_film(film: Film) -> FilmResponse:
    return FilmResponse(film)
