from typing import Optional

from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.model.dictonary.image_type import ImageType
from kinopoisk_unofficial.response.films.image_response import ImageResponse


class ImageRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v2.2/films/{id}/images'
    RESPONSE: type = ImageResponse

    __id: int
    __type: Optional[ImageType]
    __page: int = 1

    def __init__(self, film_id: int) -> None:
        self.__id = film_id

    @property
    def id(self) -> int:
        return self.__id

    @property
    def type(self) -> Optional[ImageType]:
        return self.__type

    @type.setter
    def type(self, type_: Optional[ImageType]) -> None:
        self.__type = type_

    def path(self) -> str:
        return self.PATH.replace('{id}', str(self.id))
