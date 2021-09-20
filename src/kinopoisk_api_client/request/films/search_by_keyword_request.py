from src.kinopoisk_api_client.client.http_method import HttpMethod
from src.kinopoisk_api_client.contract.request import Request
from src.kinopoisk_api_client.response.films.search_by_keyword_response import SearchByKeywordResponse


class SearchByKeywordRequest(Request):
    METHOD: HttpMethod = HttpMethod.GET
    PATH: str = '/api/v2.1/films/search-by-keyword'
    RESPONSE: type = SearchByKeywordResponse

    __keyword: str
    __page: int

    def __init__(self, keyword: str, page: int = 1) -> None:
        self.__keyword = keyword
        self.__page = page

    @property
    def keyword(self) -> str:
        return self.__keyword

    @property
    def page(self) -> int:
        return self.__page

    def path(self) -> str:
        return self._build_url(self.PATH, {
            'keyword': self.keyword,
            'page': self.page
        })
