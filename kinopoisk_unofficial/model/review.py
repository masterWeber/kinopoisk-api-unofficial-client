from dataclasses import dataclass
from datetime import datetime
from typing import Union

from kinopoisk_unofficial.model.dictonary.review_type import ReviewType


@dataclass
class Review:
    review_id: int
    review_type: ReviewType
    review_data: datetime
    user_positive_rating: Union[str, None]
    user_negative_rating: Union[str, None]
    review_autor: str
    review_title: Union[str, None]
    review_description: str
