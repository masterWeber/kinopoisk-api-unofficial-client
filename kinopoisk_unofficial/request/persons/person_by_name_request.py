from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.response.persons.person_by_name_response import PersonByNameResponse


class PersonByNameRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v1/persons'
    RESPONSE: type = PersonByNameResponse

    __name: str
    __page: int

    def __init__(self, name: str, page: int = 1) -> None:
        self.__name = name
        self.__page = page

    @property
    def name(self) -> str:
        return self.__name

    @property
    def page(self) -> int:
        return self.__page

    def path(self) -> str:
        return self._build_url(self.PATH, {
            'name': self.name,
            'page': self.page
        })
