from enum import Enum
from typing import NamedTuple


class ColorMode(Enum):
    AllOff = 0
    Basic16 = 1
    Extended256 = 2
    FullTrueColor = 3


class Code(NamedTuple):
    on: str
    off: str
