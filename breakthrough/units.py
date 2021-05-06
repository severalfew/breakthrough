from .constants import COUNTRIES, TEAMS
from enum import IntEnum


class UNIT_SIZES(IntEnum):
    corps = 4
    division = 3
    brigade = 2
    regiment = 1
    battallion = 0
    battery = 0
    company = 0
    administrative = 4


unit_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "object"},
        "location": {"type": "object"},
        "size": {"type": "object"},
        "team": {"type": "object"},
        "type": {"type": "object"},
        "units": {"type": "list"},
    }
}


class Unit:
    def __init__(self, name, size, team, country, children=[], color="grey"):
        self.name = name
        assert size in UNIT_SIZES, f"Unit size must be in: {UNIT_SIZES}"
        self.size = size
        assert team in TEAMS, f"Team must be in: {TEAMS}"
        self.team = team
        assert country in COUNTRIES.values(), f"Country must be in: {COUNTRIES.keys()}"
        self.country = country
        assert len(children) <= self.size
        self.children = children
        self.color=color

    def __str__(self):
        return f"{self.name} - {self.size} - {self.team} - [{self.size + 1}]"
