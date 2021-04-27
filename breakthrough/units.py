from enum import Enum
from .constants import COUNTRIES, TEAMS


class UNIT_SIZES(Enum):
    division = 3
    brigade = 2
    regiment = 1
    battallion = 0
    battery = 0
    company = 0


class Unit:
    def __init__(self, name, size, team, country, children=[]):
        self.name = name
        assert size in UNIT_SIZES, f"Unit size must be in: {UNIT_SIZES}"
        self.size = size
        assert team in TEAMS, f"Team must be in: {TEAMS}"
        self.team = team
        assert country in COUNTRIES, f"Country must be in: {COUNTRIES}"
        assert len(children) <= self.size
        self.children = children

    def __str__(self):
        return f"{self.name} - {self.size} - {self.team} - [{self.size + 1}]"
