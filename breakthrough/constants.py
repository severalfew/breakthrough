from .utility import resource_path
from enum import Enum, IntEnum
from PIL import Image
import os


class COLORS(Enum):
    NATO = (179, 205, 227)
    PACT = (251, 180, 174)


class country:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.icon = Image.open(os.path.join(resource_path, "flags", f"{code}.png"))


COUNTRIES = {
    "DK": country("DK", "Danmark"),
    "US": country("US", "United States"),
    "UK": country("UK", "United Kingdom"),
    "NL": country("NL", "Nederland"),
    "PL": country("PL", "Poland"),
    "DE": country("DE", "Deutschland"),
    "DDR": country("DDR", "Ost Deutchland"),
    "BE": country("BE", "Belgium"),
    "CZ": country("CZ", "Czechoslovakia"),
    "USSR": country("USSR", "Soviet Union"),
}


class TEAMS(IntEnum):
    NATO = 1
    PACT = 2
