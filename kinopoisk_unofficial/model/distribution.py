from dataclasses import dataclass
from datetime import datetime

from typing import List, Union

from kinopoisk_unofficial.model.company import Company
from kinopoisk_unofficial.model.country import Country
from kinopoisk_unofficial.model.dictonary.distribution_sub_type import DistributionSubType
from kinopoisk_unofficial.model.dictonary.distribution_type import DistributionType


@dataclass
class Distribution:
    type: DistributionType
    sub_type: Union[DistributionSubType, None]
    date: datetime
    re_release: bool
    country: Union[Country, None]
    companies: List[Company]
