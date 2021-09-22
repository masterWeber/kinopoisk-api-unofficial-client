from dataclasses import dataclass

from kinopoisk_unofficial.model.dictonary.film_video_site import FilmVideoSite


@dataclass
class FilmVideo:
    url: str
    name: str
    site: FilmVideoSite
