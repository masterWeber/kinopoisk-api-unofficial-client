from src.kinopoisk_api_client.client.api_client import ApiClient
from src.kinopoisk_api_client.request.search_by_keyword_request import SearchByKeywordRequest
from src.kinopoisk_api_client.response.search_by_keyword_response import SearchByKeywordResponse


class FilmsApiClient(ApiClient):
    def send_search_by_keyword_request(self, request: SearchByKeywordRequest) -> SearchByKeywordResponse:
        return self._send_request(request)
