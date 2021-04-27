from .constants import COLORS, COUNTRIES, TEAMS
from enum import Enum
import pandas as pd
import pyglet
import os


class CITY_SIZES(Enum):
    village = 1
    town = 2
    city = 3
    metropolis = 5


class Location:
    def __init__(self, name, country, team, city_size, x, y):
        self.name = name
        assert country in COUNTRIES, f"Country must be one of {COUNTRIES}"
        self.country = country
        assert team in TEAMS, f"Team must be one of {TEAMS}"
        self.team = team
        assert city_size in CITY_SIZES, f"Value must be one of {CITY_SIZES}"
        self.value = city_size
        self.x = x
        self.y = y
        self.sprite = self.create_sprite()

    def create_sprite(self):
        return pyglet.shapes.Circle(self.x, self.y, radius=5 * self.value, color=COLORS[self.team])


df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "locations.csv"))
locations = [Location(**row) for i, row in df.iterrows()]
