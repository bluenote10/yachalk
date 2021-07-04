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


class Color:
    black = Ansi16Code(30, 39)
    red = Ansi16Code(31, 39)
    green = Ansi16Code(32, 39)
    yellow = Ansi16Code(33, 39)
    blue = Ansi16Code(34, 39)
    magenta = Ansi16Code(35, 39)
    cyan = Ansi16Code(36, 39)
    white = Ansi16Code(37, 39)

    black_bright = Ansi16Code(90, 39)
    red_bright = Ansi16Code(91, 39)
    green_bright = Ansi16Code(92, 39)
    yellow_bright = Ansi16Code(93, 39)
    blue_bright = Ansi16Code(94, 39)
    magenta_bright = Ansi16Code(95, 39)
    cyan_bright = Ansi16Code(96, 39)
    white_bright = Ansi16Code(97, 39)

    gray = Ansi16Code(90, 39)
    grey = Ansi16Code(90, 39)


class BgColor:
    black = Ansi16Code(40, 49)
    red = Ansi16Code(41, 49)
    green = Ansi16Code(42, 49)
    yellow = Ansi16Code(43, 49)
    blue = Ansi16Code(44, 49)
    magenta = Ansi16Code(45, 49)
    cyan = Ansi16Code(46, 49)
    white = Ansi16Code(47, 49)

    black_bright = Ansi16Code(100, 49)
    red_bright = Ansi16Code(101, 49)
    green_bright = Ansi16Code(102, 49)
    yellow_bright = Ansi16Code(103, 49)
    blue_bright = Ansi16Code(104, 49)
    magenta_bright = Ansi16Code(105, 49)
    cyan_bright = Ansi16Code(106, 49)
    white_bright = Ansi16Code(107, 49)

    gray = Ansi16Code(100, 49)
    grey = Ansi16Code(100, 49)


def wrap_ansi_16(code: int, offset: int = 0) -> str:
    return f"\x1b[{code + offset}m"
