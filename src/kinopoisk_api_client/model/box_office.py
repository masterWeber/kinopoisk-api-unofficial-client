from dataclasses import dataclass


@dataclass
class BoxOffice:
    type: str
    amount: int
    currency_code: str
    name: str
    symbol: str
