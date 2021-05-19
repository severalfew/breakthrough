from .constants import COUNTRIES, TEAMS
from enum import IntEnum


class UNIT_SIZES(IntEnum):
    corps = 50
    division = 4
    brigade = 3
    regiment = 2
    battallion = 1
    battery = 1
    company = 1
    administrative = 100


class UNIT_TYPES(IntEnum):
    administrative = 0
    artillery = 1
    infantry = 2
    armor = 3
    support = 4
    airborne = 5
    air_defense = 6
    fighter = 7
    bomber = 8


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
    def __init__(self, name, size, team, country, children=[], color="grey", type=UNIT_TYPES.administrative):
        self.name = name
        assert size in UNIT_SIZES, f"Unit size must be in: {UNIT_SIZES}"
        self.size = size
        assert team in TEAMS, f"Team must be in: {TEAMS}"
        self.team = team
        assert country in COUNTRIES.values(), f"Country must be in: {COUNTRIES.keys()}"
        self.country = country
        assert len(children) <= self.size.value, f"{len(children)} {self.size.value}"
        self.children = children
        self.color = color
        self.type = type

    def __str__(self):
        return self.name
