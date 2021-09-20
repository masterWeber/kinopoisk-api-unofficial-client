from dataclasses import dataclass
from datetime import datetime

from typing import List, Union

from src.kinopoisk_api_client.model.company import Company
from src.kinopoisk_api_client.model.country import Country
from src.kinopoisk_api_client.model.dictonary.distribution_sub_type import DistributionSubType
from src.kinopoisk_api_client.model.dictonary.distribution_type import DistributionType


@dataclass
class Distribution:
    type: DistributionType
    sub_type: Union[DistributionSubType, None]
    date: datetime
    re_release: bool
    country: Union[Country, None]
    companies: List[Company]
