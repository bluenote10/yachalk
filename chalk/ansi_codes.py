class Colors:
    black = (30, 39)
    red = (31, 39)
    green = (32, 39)
    yellow = (33, 39)
    blue = (34, 39)
    magenta = (35, 39)
    cyan = (36, 39)
    white = (37, 39)


class BgColors:
    bg_black = (40, 49)
    bg_red = (41, 49)
    bg_green = (42, 49)
    bg_yellow = (43, 49)
    bg_blue = (44, 49)
    bg_magenta = (45, 49)
    bg_cyan = (46, 49)
    bg_white = (47, 49)


def wrap_ansi_16(code, offset=0):
    return f"\u001b[{code + offset}m"
