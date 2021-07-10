"""
Inspired by:
https://github.com/chalk/ansi-styles/blob/main/index.js
"""

import math

from typing import NamedTuple


class Ansi16Code(NamedTuple):
    on: int
    off: int


class Mod:
    reset = Ansi16Code(0, 0)
    bold = Ansi16Code(1, 22)  # 21 isn't widely supported and 22 does the same thing
    dim = Ansi16Code(2, 22)
    italic = Ansi16Code(3, 23)
    underline = Ansi16Code(4, 24)
    overline = Ansi16Code(53, 55)
    hidden = Ansi16Code(8, 28)
    strikethrough = Ansi16Code(9, 29)


COLOR_CLOSE = 39
BG_COLOR_CLOSE = 49


class Color:
    black = Ansi16Code(30, COLOR_CLOSE)
    red = Ansi16Code(31, COLOR_CLOSE)
    green = Ansi16Code(32, COLOR_CLOSE)
    yellow = Ansi16Code(33, COLOR_CLOSE)
    blue = Ansi16Code(34, COLOR_CLOSE)
    magenta = Ansi16Code(35, COLOR_CLOSE)
    cyan = Ansi16Code(36, COLOR_CLOSE)
    white = Ansi16Code(37, COLOR_CLOSE)

    black_bright = Ansi16Code(90, COLOR_CLOSE)
    red_bright = Ansi16Code(91, COLOR_CLOSE)
    green_bright = Ansi16Code(92, COLOR_CLOSE)
    yellow_bright = Ansi16Code(93, COLOR_CLOSE)
    blue_bright = Ansi16Code(94, COLOR_CLOSE)
    magenta_bright = Ansi16Code(95, COLOR_CLOSE)
    cyan_bright = Ansi16Code(96, COLOR_CLOSE)
    white_bright = Ansi16Code(97, COLOR_CLOSE)

    gray = Ansi16Code(90, COLOR_CLOSE)
    grey = Ansi16Code(90, COLOR_CLOSE)


class BgColor:
    black = Ansi16Code(40, BG_COLOR_CLOSE)
    red = Ansi16Code(41, BG_COLOR_CLOSE)
    green = Ansi16Code(42, BG_COLOR_CLOSE)
    yellow = Ansi16Code(43, BG_COLOR_CLOSE)
    blue = Ansi16Code(44, BG_COLOR_CLOSE)
    magenta = Ansi16Code(45, BG_COLOR_CLOSE)
    cyan = Ansi16Code(46, BG_COLOR_CLOSE)
    white = Ansi16Code(47, BG_COLOR_CLOSE)

    black_bright = Ansi16Code(100, BG_COLOR_CLOSE)
    red_bright = Ansi16Code(101, BG_COLOR_CLOSE)
    green_bright = Ansi16Code(102, BG_COLOR_CLOSE)
    yellow_bright = Ansi16Code(103, BG_COLOR_CLOSE)
    blue_bright = Ansi16Code(104, BG_COLOR_CLOSE)
    magenta_bright = Ansi16Code(105, BG_COLOR_CLOSE)
    cyan_bright = Ansi16Code(106, BG_COLOR_CLOSE)
    white_bright = Ansi16Code(107, BG_COLOR_CLOSE)

    gray = Ansi16Code(100, BG_COLOR_CLOSE)
    grey = Ansi16Code(100, BG_COLOR_CLOSE)


_ANSI_BACKGROUND_OFFSET = 10


def wrap_ansi_16(code: int, background: bool = False) -> str:
    offset = _ANSI_BACKGROUND_OFFSET if background else 0
    return f"\x1b[{code + offset}m"


def wrap_ansi_256(code: int, background: bool = False) -> str:
    offset = _ANSI_BACKGROUND_OFFSET if background else 0
    return f"\x1b[{38 + offset};5;{code}m"


def wrap_ansi_16m(r: int, g: int, b: int, background: bool = False) -> str:
    offset = _ANSI_BACKGROUND_OFFSET if background else 0
    return f"\x1b[{38 + offset};2;{r};{g};{b}m"


def rgb_to_ansi_256(r: int, g: int, b: int) -> int:
    if r == g and g == b:
        if r < 8:
            return 16
        if r > 248:
            return 231
        return round(((r - 8) / 247) * 24) + 232

    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


def ansi_256_to_ansi_16(code: int) -> int:
    if code < 8:
        return 30 + code

    if code < 16:
        return 90 + (code - 8)

    if code >= 232:
        r = (((code - 232) * 10) + 8) / 255
        g = r
        b = r
    else:
        code -= 16
        remainder = code % 36

        r = math.floor(code / 36) / 5
        g = math.floor(remainder / 6) / 5
        b = (remainder % 6) / 5

    value = max(r, g, b) * 2

    if value == 0:
        return 30

    result = 30 + ((round(b) << 2) | (round(g) << 1) | round(r))

    if value == 2:
        result += 60

    return result
