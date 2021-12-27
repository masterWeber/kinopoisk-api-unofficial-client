from dataclasses import dataclass
from typing import Optional


@dataclass
class Image:
    imageUrl: Optional[str]
    previewUrl: Optional[str]
