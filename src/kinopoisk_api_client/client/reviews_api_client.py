from src.kinopoisk_api_client.client.api_client import ApiClient
from src.kinopoisk_api_client.request.reviews.review_details_request import ReviewDetailsRequest
from src.kinopoisk_api_client.request.reviews.reviews_request import ReviewsRequest
from src.kinopoisk_api_client.response.reviews.review_details_response import ReviewDetailsResponse
from src.kinopoisk_api_client.response.reviews.reviews_response import ReviewsResponse


class ReviewsApiClient(ApiClient):
    def send_reviews_request(self, request: ReviewsRequest) -> ReviewsResponse:
        return self._send_request(request)

    def send_review_details_request(self, request: ReviewDetailsRequest) -> ReviewDetailsResponse:
        return self._send_request(request)
