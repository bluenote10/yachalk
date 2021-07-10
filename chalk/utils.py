import re

from typing import Optional, Tuple

from .types import ColorMode, Code
from . import ansi


def hex_to_rgb(hex: str) -> Tuple[int, int, int]:

    if len(hex) == 3:
        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]

    hex = hex.lower()
    m = re.match(r"^([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$", hex)

    if m is None:
        raise ValueError(f"'{hex}' is not a valid hex literal")

    return int(m.group(1), 16), int(m.group(2), 16), int(m.group(3), 16)


def get_code_from_rgb(r: int, g: int, b: int, mode: ColorMode, background: bool) -> Optional[Code]:
    if mode == ColorMode.FullTrueColor:
        code = ansi.wrap_ansi_16m(r, g, b, background=background)
    elif mode == ColorMode.Extended256:
        code_256 = ansi.rgb_to_ansi_256(r, g, b)
        code = ansi.wrap_ansi_256(code_256, background=background)
    elif mode == ColorMode.Basic16:
        code_256 = ansi.rgb_to_ansi_256(r, g, b)
        code_16 = ansi.ansi_256_to_ansi_16(code_256)
        code = ansi.wrap_ansi_16(code_16, background=background)
    else:
        return None

    close = ansi.BG_COLOR_CLOSE if background else ansi.COLOR_CLOSE
    return Code(on=code, off=ansi.wrap_ansi_16(close))
