from dataclasses import dataclass


@dataclass(frozen=True)
class ScreenConstants:
    WIDTH: int = 800
    HEIGHT: int = 500
    TITLE: str = "Hack n Slash"
