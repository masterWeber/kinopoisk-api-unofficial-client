from kinopoisk_unofficial.client.api_client import ApiClient
from kinopoisk_unofficial.request.reviews.review_details_request import ReviewDetailsRequest
from kinopoisk_unofficial.request.reviews.reviews_request import ReviewsRequest
from kinopoisk_unofficial.response.reviews.review_details_response import ReviewDetailsResponse
from kinopoisk_unofficial.response.reviews.reviews_response import ReviewsResponse


class ReviewsApiClient(ApiClient):
    def send_reviews_request(self, request: ReviewsRequest) -> ReviewsResponse:
        return self._send_request(request)

    def send_review_details_request(self, request: ReviewDetailsRequest) -> ReviewDetailsResponse:
        return self._send_request(request)
