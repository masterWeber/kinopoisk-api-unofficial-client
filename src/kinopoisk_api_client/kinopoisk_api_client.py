import apischema

from src.kinopoisk_api_client.client.films_api_client import FilmsApiClient
from src.kinopoisk_api_client.client.http_client import HttpClient
from src.kinopoisk_api_client.client.reviews_api_client import ReviewsApiClient
from src.kinopoisk_api_client.client.staff_api_client import StaffApiClient


class KinopoiskApiClient:
    __base_url: str = 'https://kinopoiskapiunofficial.tech'
    __films: FilmsApiClient

    def __init__(self, token: str) -> None:
        http_client = HttpClient(self.__base_url)
        apischema.settings.camel_case = True
        self.__films = FilmsApiClient(http_client, apischema, token)
        self.__reviews = ReviewsApiClient(http_client, apischema, token)
        self.__staff = StaffApiClient(http_client, apischema, token)

    @property
    def films(self) -> FilmsApiClient:
        return self.__films

    @property
    def reviews(self) -> ReviewsApiClient:
        return self.__reviews

    @property
    def staff(self) -> StaffApiClient:
        return self.__staff
