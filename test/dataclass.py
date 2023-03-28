from dataclasses import dataclass


@dataclass
class Site:
    Name: str
    Backend: str
    Frontend: str
    Popularity: int
