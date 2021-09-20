from src.kinopoisk_api_client.client.http_method import HttpMethod
from src.kinopoisk_api_client.contract.request import Request
from src.kinopoisk_api_client.response.reviews.reviews_response import ReviewsResponse


class ReviewsRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v1/reviews'
    RESPONSE: type = ReviewsResponse

    __film_id: int
    __page: int

    def __init__(self, film_id: int, page: int = 1) -> None:
        self.__film_id = film_id
        self.__page = page

    @property
    def film_id(self) -> int:
        return self.__film_id

    @property
    def page(self) -> int:
        return self.__page

    def path(self) -> str:
        return self._build_url(self.PATH, {
            'filmId': self.film_id,
            'page': self.page
        })
