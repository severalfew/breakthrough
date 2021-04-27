from enum import Enum


class COLORS(Enum):
    NATO = (179, 205, 227)
    PACT = (251, 180, 174)


class COUNTRIES(Enum):
    DK = "Danemark"
    GDR = "East Germany"
    NL = "Nederlands"
    PL = "Poland"
    CZ = "Czechoslovakia"
    FRG = "West Germany"


class TEAMS(Enum):
    NATO = 1
    PACT = 2
