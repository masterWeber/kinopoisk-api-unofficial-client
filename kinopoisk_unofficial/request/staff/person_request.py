from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.response.staff.person_response import PersonResponse


class PersonRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v1/staff/{id}'
    RESPONSE: type = PersonResponse

    __id: int
    __page: int

    def __init__(self, person_id: int) -> None:
        self.__id = person_id

    @property
    def person_id(self) -> int:
        return self.__id

    def path(self) -> str:
        return self.PATH.replace('{id}', str(self.person_id))
