from src.kinopoisk_api_client.client.http_method import HttpMethod
from src.kinopoisk_api_client.contract.request import Request
from src.kinopoisk_api_client.response.films.film_sequels_and_prequels_response import FilmSequelsAndPrequelsResponse


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
