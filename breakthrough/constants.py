from enum import Enum


class COLORS(Enum):
    NATO = (179, 205, 227)
    PACT = (251, 180, 174)


class COUNTRIES(Enum):
    DK = "Danemark"
    DDR = "Ost Deutschland"
    NL = "Nederland"
    PL = "Poland"
    CZ = "Československo"
    DE = "West Deutschland"


class TEAMS(Enum):
    NATO = 1
    PACT = 2
