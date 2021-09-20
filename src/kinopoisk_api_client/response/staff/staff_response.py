from dataclasses import dataclass, field

from typing import List

from apischema import serializer, deserializer
from apischema.conversions import identity
from apischema.metadata import conversion

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.staff import Staff


@dataclass(frozen=True)
class StaffResponse(Response):
    items: List[Staff] = field(
        metadata=conversion(deserialization=identity, serialization=identity)
    )


@serializer
def unwrap_staff(staff_response: StaffResponse) -> List[Staff]:
    return staff_response.items


@deserializer
def wrap_staff(items: List[Staff]) -> StaffResponse:
    return StaffResponse(items)
