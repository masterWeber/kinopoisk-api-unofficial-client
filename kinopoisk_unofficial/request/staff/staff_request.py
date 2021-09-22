from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.response.staff.staff_response import StaffResponse


class StaffRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v1/staff'
    RESPONSE: type = StaffResponse

    __film_id: int

    def __init__(self, film_id: int) -> None:
        self.__film_id = film_id

    @property
    def film_id(self) -> int:
        return self.__film_id

    def path(self) -> str:
        return self._build_url(self.PATH, {
            'filmId': self.film_id,
        })
