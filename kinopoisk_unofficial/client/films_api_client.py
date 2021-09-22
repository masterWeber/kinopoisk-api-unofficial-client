from kinopoisk_unofficial.client.api_client import ApiClient
from kinopoisk_unofficial.request.films.box_office_request import BoxOfficeRequest
from kinopoisk_unofficial.request.films.digital_release_request import DigitalReleaseRequest
from kinopoisk_unofficial.request.films.distributions_request import DistributionsRequest
from kinopoisk_unofficial.request.films.facts_request import FactsRequest
from kinopoisk_unofficial.request.films.film_frame_request import FilmFrameRequest
from kinopoisk_unofficial.request.films.film_request import FilmRequest
from kinopoisk_unofficial.request.films.film_search_by_filters_request import FilmSearchByFiltersRequest
from kinopoisk_unofficial.request.films.film_sequels_and_prequels_request import FilmSequelsAndPrequelsRequest
from kinopoisk_unofficial.request.films.film_top_request import FilmTopRequest
from kinopoisk_unofficial.request.films.film_video_request import FilmVideoRequest
from kinopoisk_unofficial.request.films.filters_request import FiltersRequest
from kinopoisk_unofficial.request.films.related_film_request import RelatedFilmRequest
from kinopoisk_unofficial.request.films.search_by_keyword_request import SearchByKeywordRequest
from kinopoisk_unofficial.request.films.seasons_request import SeasonsRequest
from kinopoisk_unofficial.response.films.box_office_response import BoxOfficeResponse
from kinopoisk_unofficial.response.films.digital_release_response import DigitalReleaseResponse
from kinopoisk_unofficial.response.films.distributions_response import DistributionsResponse
from kinopoisk_unofficial.response.films.facts_response import FactsResponse
from kinopoisk_unofficial.response.films.film_frame_response import FilmFrameResponse
from kinopoisk_unofficial.response.films.film_response import FilmResponse
from kinopoisk_unofficial.response.films.film_search_by_filters_response import FilmSearchByFiltersResponse
from kinopoisk_unofficial.response.films.film_sequels_and_prequels_response import FilmSequelsAndPrequelsResponse
from kinopoisk_unofficial.response.films.film_top_response import FilmTopResponse
from kinopoisk_unofficial.response.films.film_video_response import FilmVideoResponse
from kinopoisk_unofficial.response.films.filters_response import FiltersResponse
from kinopoisk_unofficial.response.films.related_film_respons import RelatedFilmResponse
from kinopoisk_unofficial.response.films.search_by_keyword_response import SearchByKeywordResponse
from kinopoisk_unofficial.response.films.seasons_response import SeasonsResponse


class FilmsApiClient(ApiClient):
    def send_search_by_keyword_request(self, request: SearchByKeywordRequest) -> SearchByKeywordResponse:
        return self._send_request(request)

    def send_film_request(self, request: FilmRequest) -> FilmResponse:
        return self._send_request(request)

    def send_seasons_request(self, request: SeasonsRequest) -> SeasonsResponse:
        return self._send_request(request)

    def send_facts_request(self, request: FactsRequest) -> FactsResponse:
        return self._send_request(request)

    def send_distributions_request(self, request: DistributionsRequest) -> DistributionsResponse:
        return self._send_request(request)

    def send_box_office_request(self, request: BoxOfficeRequest) -> BoxOfficeResponse:
        return self._send_request(request)

    def send_film_frame_request(self, request: FilmFrameRequest) -> FilmFrameResponse:
        return self._send_request(request)

    def send_film_video_request(self, request: FilmVideoRequest) -> FilmVideoResponse:
        return self._send_request(request)

    def send_film_sequels_and_prequels_request(
            self,
            request: FilmSequelsAndPrequelsRequest
    ) -> FilmSequelsAndPrequelsResponse:
        return self._send_request(request)

    def send_filters_request(self, request: FiltersRequest) -> FiltersResponse:
        return self._send_request(request)

    def send_film_top_request(self, request: FilmTopRequest) -> FilmTopResponse:
        return self._send_request(request)

    def send_film_search_by_filters_request(self, request: FilmSearchByFiltersRequest) -> FilmSearchByFiltersResponse:
        return self._send_request(request)

    def send_related_film_request(self, request: RelatedFilmRequest) -> RelatedFilmResponse:
        return self._send_request(request)

    def send_digital_release_request(self, request: DigitalReleaseRequest) -> DigitalReleaseResponse:
        return self._send_request(request)
