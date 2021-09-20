from dataclasses import dataclass, field

from typing import List

from src.kinopoisk_api_client.contract.response import Response
from src.kinopoisk_api_client.model.review import Review


@dataclass(frozen=True)
class ReviewsResponse(Response):
    page: int
    film_id: int
    review_all_count: int
    review_all_positive_ratio: str
    review_positive_count: int
    review_negative_count: int
    review_neutral_count: int
    pages_count: int
    reviews: List[Review] = field(default_factory=list)
