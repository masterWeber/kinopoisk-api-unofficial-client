from dataclasses import dataclass

from src.kinopoisk_api_client.model.dictonary.film_video_site import FilmVideoSite


@dataclass
class FilmVideo:
    url: str
    name: str
    site: FilmVideoSite
