from enum import Enum


class ReviewType(Enum):
    POSITIVE = 'POSITIVE'
    NEGATIVE = 'NEGATIVE'
    NEUTRAL = 'NEUTRAL'
    UNKNOWN = 'UNKNOWN'
