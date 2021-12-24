from kinopoisk_unofficial.client.api_client import ApiClient
from kinopoisk_unofficial.request.persons.person_by_name_request import PersonByNameRequest
from kinopoisk_unofficial.response.persons.person_by_name_response import PersonByNameResponse


class PersonsApiClient(ApiClient):
    def send_person_by_name_request(self, request: PersonByNameRequest) -> PersonByNameResponse:
        return self._send_request(request)
