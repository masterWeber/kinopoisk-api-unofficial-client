from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.response.films.film_sequels_and_prequels_response import FilmSequelsAndPrequelsResponse


class FilmSequelsAndPrequelsRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v2.1/films/{id}/sequels_and_prequels'
    RESPONSE: type = FilmSequelsAndPrequelsResponse

    __id: int

    def __init__(self, film_id: int) -> None:
        self.__id = film_id

    @property
    def id(self) -> int:
        return self.__id

    def path(self) -> str:
        return self.PATH.replace('{id}', str(self.id))
