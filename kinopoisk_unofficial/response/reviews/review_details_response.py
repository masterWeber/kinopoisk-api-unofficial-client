from dataclasses import dataclass
from datetime import datetime

from kinopoisk_unofficial.contract.response import Response
from kinopoisk_unofficial.model.dictonary.review_type import ReviewType


@dataclass(frozen=True)
class ReviewDetailsResponse(Response):
    review_id: int
    review_type: ReviewType
    review_data: datetime
    user_positive_rating: int
    user_negative_rating: int
    review_autor: str
    review_title: str
    review_description: float
