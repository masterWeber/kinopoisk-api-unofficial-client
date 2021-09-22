from kinopoisk_unofficial.client.http_method import HttpMethod
from kinopoisk_unofficial.contract.request import Request
from kinopoisk_unofficial.response.reviews.review_details_response import ReviewDetailsResponse


class ReviewDetailsRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v1/reviews/details'
    RESPONSE: type = ReviewDetailsResponse

    __review_id: int

    def __init__(self, review_id: int) -> None:
        self.__review_id = review_id

    @property
    def review_id(self) -> int:
        return self.__review_id

    def path(self) -> str:
        return self._build_url(self.PATH, {
            'filmId': self.review_id,
        })
