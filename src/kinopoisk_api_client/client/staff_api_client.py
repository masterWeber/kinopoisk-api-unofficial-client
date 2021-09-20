from src.kinopoisk_api_client.client.api_client import ApiClient
from src.kinopoisk_api_client.request.staff.person_request import PersonRequest
from src.kinopoisk_api_client.request.staff.staff_request import StaffRequest
from src.kinopoisk_api_client.response.staff.person_response import PersonResponse
from src.kinopoisk_api_client.response.staff.staff_response import StaffResponse


class StaffApiClient(ApiClient):
    def send_staff_request(self, request: StaffRequest) -> StaffResponse:
        return self._send_request(request)

    def send_person_request(self, request: PersonRequest) -> PersonResponse:
        return self._send_request(request)
