<div align="center">
    <h1>Kinopoisk API Unofficial client</h1>
    <p>Python-модуль для взаимодействия с неофициальным <a href="https://kinopoiskapiunofficial.tech/">API КиноПоиска</a></p>
    <img align="center" src="https://img.shields.io/github/repo-size/masterWeber/kinopoisk-api-unofficial-client" alt="GitHub repo size">
    <img align="center" src="https://img.shields.io/pypi/dm/kinopoisk-api-unofficial-client" alt="PyPI - Downloads">
    <img align="center" src="https://img.shields.io/github/stars/masterWeber/kinopoisk-api-unofficial-client" alt="GitHub Repo stars">
    <img align="center" src="https://img.shields.io/github/watchers/masterWeber/kinopoisk-api-unofficial-client" alt="GitHub watchers">
    <img align="center" src="https://img.shields.io/github/last-commit/masterWeber/kinopoisk-api-unofficial-client" alt="GitHub last commit">
    <img align="center" src="https://img.shields.io/github/languages/top/masterWeber/kinopoisk-api-unofficial-client" alt="GitHub top language">
    <img align="center" src="https://img.shields.io/website?down_message=Down&label=Kinopoisk%20Api%20Unofficial&up_message=Up&url=https%3A%2F%2Fkinopoiskapiunofficial.tech%2F" alt="API Uptime">
</div>

### Установка

```
$ pip install kinopoisk-api-unofficial-client
```

### Получение токена KinopoiskAPI

Для получения токена необходима регистрация на сайте
<a href="https://kinopoiskapiunofficial.tech/signup">kinopoiskapiunofficial.tech</a>. После регистрации перейдите в
настройки своего <a href="https://kinopoiskapiunofficial.tech/user">профиля</a> и сохраните токен.
<div align="center">
    <img src="https://i.imgur.com/uRY1rRF.png" alt="Регистрация">
</div>

## films

Набор методов для работы с данными о фильмах

### Получить данные о фильме по kinopoisk id

Возвращает базовые данные о фильме. Поле last_sync показывает дату последнего обновления данных.

* `Эндпоинт`: /api/v2.2/films/{id}
* `Метод`: send_film_request(request: FilmRequest) -> FilmResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_request import FilmRequest

api_client = KinopoiskApiClient("<your_token>")
request = FilmRequest(507)
response = api_client.films.send_film_request(request)
```

### Получить данные о сезонах для сериала по kinopoisk film id

Возвращает данные о сезонах для сериала.

* `Эндпоинт`: /api/v2.2/films/{id}/seasons
* `Метод`: send_seasons_request(request: SeasonsRequest) -> SeasonsResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.seasons_request import SeasonsRequest

api_client = KinopoiskApiClient("<your_token>")
request = SeasonsRequest(685246)
response = api_client.films.send_seasons_request(request)
```

### Получить данные о фактах и ошибках в фильме по kinopoisk film id

Возвращает список фактов и ошибок в фильме.

* `Эндпоинт`: /api/v2.2/films/{id}/facts
* `Метод`: send_facts_request(request: FactsRequest) -> FactsResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.facts_request import FactsRequest

api_client = KinopoiskApiClient("<your_token>")
request = FactsRequest(685246)
response = api_client.films.send_facts_request(request)
```

### Получить данные о прокате фильма по kinopoisk film id

Возвращает данные о прокате в разных странах.

* `Эндпоинт`: /api/v2.2/films/{id}/distributions
* `Метод`: send_distributions_request(request: DistributionsRequest) -> DistributionsResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.distributions_request import DistributionsRequest

api_client = KinopoiskApiClient("<your_token>")
request = DistributionsRequest(507)
response = api_client.films.send_distributions_request(request)
```

### Получить данные о бюджете и сборах фильма по kinopoisk film id

Возвращает данные о бюджете и сборах.

* `Эндпоинт`: /api/v2.2/films/{id}/box_office
* `Метод`: send_box_office_request(request: BoxOfficeRequest) -> BoxOfficeResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.box_office_request import BoxOfficeRequest

api_client = KinopoiskApiClient("<your_token>")
request = BoxOfficeRequest(507)
response = api_client.films.send_box_office_request(request)
```

### Получить кадры из фильма по kinopoisk film id

Возвращает кадры из фильма.

* `Эндпоинт`: /api/v2.1/films/{id}/frames
* `Метод`: send_film_frame_request(request: FilmFrameRequest) -> FilmFrameResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_frame_request import FilmFrameRequest

api_client = KinopoiskApiClient("<your_token>")
request = FilmFrameRequest(507)
response = api_client.films.send_film_frame_request(request)
```

### Получить трейлеры,тизеры,видео для фильма по kinopoisk film id

Возвращает трейлеры,тизеры,видео для фильма по kinopoisk film id.

* `Эндпоинт`: /api/v2.2/films/{id}/videos
* `Метод`: send_film_video_request(request: FilmVideoRequest) -> FilmVideoResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_video_request import FilmVideoRequest

api_client = KinopoiskApiClient("<your_token>")
request = FilmVideoRequest(507)
response = api_client.films.send_film_video_request(request)
```

### Получить сиквелы и приквелы для фильма по kinopoisk film id

Возвращает информацию о сиквелах и приквелах для фильма по kinopoisk film id.

* `Эндпоинт`: /api/v2.1/films/{id}/sequels_and_prequels
* `Метод`: send_film_sequels_and_prequels_request(request: FilmSequelsAndPrequelsRequest) ->
  FilmSequelsAndPrequelsResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_sequels_and_prequels_request import FilmSequelsAndPrequelsRequest

api_client = KinopoiskApiClient("<your_token>")
request = FilmSequelsAndPrequelsRequest(507)
response = api_client.films.send_film_sequels_and_prequels_request(request)
```

### Получить список фильмов по ключевым словам

* `Эндпоинт`: /api/v2.1/films/search-by-keyword
* `Метод`: send_search_by_keyword_request(request: SearchByKeywordRequest) -> SearchByKeywordResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.search_by_keyword_request import SearchByKeywordRequest

api_client = KinopoiskApiClient("<your_token>")
request = SearchByKeywordRequest("Рик и Морти")
response = api_client.films.send_search_by_keyword_request(request)
```

### Получить id стран и жанров для использования в FilmSearchByFiltersRequest

Возвращает список id стран и жанров, которые могут быть использованы в поиске по фильтру.

* `Эндпоинт`: /api/v2.1/films/filters
* `Метод`: send_filters_request(request: FiltersRequest) -> FiltersResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.filters_request import FiltersRequest

api_client = KinopoiskApiClient("<your_token>")
request = FiltersRequest()
response = api_client.films.send_filters_request(request)
```

### Получить список фильмов по различным фильтрам

Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов. Используй `FiltersRequest`
чтобы получить id стран и жанров.

* `Эндпоинт`: /api/v2.1/films/search-by-filters
* `Метод`: send_film_search_by_filters_request(request: FilmSearchByFiltersRequest) -> FilmSearchByFiltersResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_search_by_filters_request import FilmSearchByFiltersRequest

api_client = KinopoiskApiClient("<your_token>")

request = FilmSearchByFiltersRequest()
request.year_from = 2020
request.rating_from = 5

response = api_client.films.send_film_search_by_filters_request(request)
```

### Получить список фильмов из различных топов или коллекций

Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
Например https://www.kinopoisk.ru/top/lists/58/.

* `Эндпоинт`: /api/v2.2/films/top
* `Метод`: send_film_top_request(request: FilmTopRequest) -> FilmTopResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.film_top_request import FilmTopRequest
from kinopoisk_unofficial.model.dictonary.top_type import TopType

api_client = KinopoiskApiClient("<your_token>")
request = FilmTopRequest(TopType.TOP_250_BEST_FILMS)
response = api_client.films.send_film_top_request(request)
```

### Получить список похожих фильмов по kinopoisk film id

Возвращает список похожих фильмов по kinopoisk film id

* `Эндпоинт`: /api/v2.2/films/{id}/similars
* `Метод`: send_related_film_request(request: RelatedFilmRequest) -> RelatedFilmResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.related_film_request import RelatedFilmRequest

api_client = KinopoiskApiClient("<your_token>")
request = RelatedFilmRequest(507)
response = api_client.films.send_related_film_request(request)
```

### Получить список цифровых релизов

Возвращает список цифровых релизов. Например https://www.kinopoisk.ru/comingsoon/digital/

* `Эндпоинт`: /api/v2.1/films/releases
* `Метод`: send_digital_release_request(request: DigitalReleaseRequest) -> DigitalReleaseResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.films.digital_release_request import DigitalReleaseRequest
from kinopoisk_unofficial.model.dictonary.month import Month

api_client = KinopoiskApiClient("<your_token>")
request = DigitalReleaseRequest(2021, Month.SEPTEMBER)
response = api_client.films.send_digital_release_request(request)
```

## reviews

Набор методов для работы с ревью о фильмах

### Получить рецензии зрителей

Возвращает список рецензий с пагинацией. Каждая страница содержит не более чем 20 рецензий. Поле description содержит не
полный текст рецензии. Полный текст может быть получен из `ReviewDetailsRequest`

* `Эндпоинт`: /api/v1/reviews
* `Метод`: send_reviews_request(request: ReviewsRequest) -> ReviewsResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.reviews.reviews_request import ReviewsRequest

api_client = KinopoiskApiClient("<your_token>")
request = ReviewsRequest(507)
response = api_client.reviews.send_reviews_request(request)
```

### Получить полную рецензию по kinopoisk review id

Возвращает полную информацию о рецензии.

* `Эндпоинт`: /api/v1/reviews/details
* `Метод`: send_review_details_request(request: ReviewDetailsRequest) -> ReviewDetailsResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.reviews.review_details_request import ReviewDetailsRequest

api_client = KinopoiskApiClient("<your_token>")
request = ReviewDetailsRequest(3000574)
response = api_client.reviews.send_review_details_request(request)
```

## staff

Набор методов для работы с данными об актерах, режиссерах и т.д.

### Получить данные об актерах, режисерах и т.д. по kinopoisk film id

Возвращает данные об актерах, режисерах и т.д. по kinopoisk film id

* `Эндпоинт`: /api/v1/staff
* `Метод`: send_staff_request(request: StaffRequest) -> StaffResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.staff.staff_request import StaffRequest

api_client = KinopoiskApiClient("<your_token>")
request = StaffRequest(507)
response = api_client.staff.send_staff_request(request)
```

### Получить данные о конкретном человеке по kinopoisk person id

Возвращает данные о конкретном человеке по kinopoisk person id

* `Эндпоинт`: /api/v1/staff/{id}
* `Метод`: send_person_request(request: PersonRequest) -> PersonResponse

```python
from kinopoisk_unofficial.kinopoisk_api_client import KinopoiskApiClient
from kinopoisk_unofficial.request.staff.person_request import PersonRequest

api_client = KinopoiskApiClient("<your_token>")
request = PersonRequest(27977)
response = api_client.staff.send_person_request(request)
```