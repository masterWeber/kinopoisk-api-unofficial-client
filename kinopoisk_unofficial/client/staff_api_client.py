from kinopoisk_unofficial.client.api_client import ApiClient
from kinopoisk_unofficial.request.staff.person_request import PersonRequest
from kinopoisk_unofficial.request.staff.staff_request import StaffRequest
from kinopoisk_unofficial.response.staff.person_response import PersonResponse
from kinopoisk_unofficial.response.staff.staff_response import StaffResponse


class StaffApiClient(ApiClient):
    def send_staff_request(self, request: StaffRequest) -> StaffResponse:
        return self._send_request(request)

    def send_person_request(self, request: PersonRequest) -> PersonResponse:
        return self._send_request(request)
