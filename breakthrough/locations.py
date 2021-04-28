from .constants import COLORS, COUNTRIES, TEAMS
from enum import Enum
import json
import os
import pyglet


class CITY_SIZES(Enum):
    village = 1
    town = 2
    city = 3
    lager = 4
    metropolis = 5


class Location:
    def __init__(self, city, country, team, city_size, x, y, **kwargs):
        self.name = city
        self.country = getattr(COUNTRIES, country)
        self.team = getattr(TEAMS, team)
        self.value = getattr(CITY_SIZES, city_size)
        self.x = x
        self.y = y
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.sprite = self.create_sprite()

    def create_sprite(self):
        sprite = pyglet.shapes.Circle(
            getattr(self, "display_x", self.x),
            getattr(self, "display_y", self.x),
            radius=5 * self.value.value,
            color=getattr(COLORS, self.team.name).value
        )
        sprite.opacity = 200
        return sprite


location_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "locations")
locations = []
for loc_file in os.listdir(location_path):
    if not loc_file.endswith(".json"):
        continue
    with open(os.path.join(location_path, loc_file), "r") as fp:
        locations.append(Location(**json.load(fp)))
