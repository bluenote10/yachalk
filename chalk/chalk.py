import re

from enum import Enum
from typing import List, NamedTuple, Optional, Union

from .ansi_codes import (
    Mod,
    Color,
    BgColor,
    Ansi16Code,
    wrap_ansi_16,
    wrap_ansi_256,
    wrap_ansi_16m,
)
from . import ansi_codes


class ColorMode(Enum):
    NoColors = 0
    Basic16 = 1
    Extended256 = 2
    FullTrueColor = 3


class Code(NamedTuple):
    on: str
    off: str

    def doit(self) -> str:
        return self.on


class Generator:
    def __init__(self, mode: ColorMode, codes: List[Code]):
        self._mode = mode
        self._codes = codes

    def __call__(self, *args: object, sep: str = " ") -> str:
        if len(args) == 1 and isinstance(args[0], str):
            s = args[0]
        else:
            s = sep.join([str(arg) for arg in args])

        all_on = "".join([code.on for code in self._codes])
        all_off = "".join([code.off for code in self._codes])

        if "\u001b" in s:
            for code in self._codes:
                # Note: It seems to be necessary to replace the off code not just by
                # the on code, but keep the off code as well due to issues discussed here:
                # https://github.com/chalk/chalk/pull/335
                # https://github.com/chalk/chalk/issues/334
                # https://github.com/doowb/ansi-colors#nested-styling-bug
                s = s.replace(code.off, code.off + code.on)

        if "\n" in s:
            s = re.sub(
                r"(\r?\n)",
                all_off + r"\1" + all_on,
                s,
            )

        return all_on + s + all_off

    # General style function

    def style(self, code: Union[Code, Ansi16Code]) -> "Generator":
        if isinstance(code, Ansi16Code):
            code = Code(on=wrap_ansi_16(code.on), off=wrap_ansi_16(code.off))
        self._codes.append(code)
        return self

    # Modifiers

    @property
    def reset(self) -> "Generator":
        self.style(Mod.reset)
        return self

    @property
    def bold(self) -> "Generator":
        self.style(Mod.bold)
        return self

    @property
    def dim(self) -> "Generator":
        self.style(Mod.dim)
        return self

    @property
    def italic(self) -> "Generator":
        self.style(Mod.italic)
        return self

    @property
    def underline(self) -> "Generator":
        self.style(Mod.underline)
        return self

    @property
    def overline(self) -> "Generator":
        self.style(Mod.overline)
        return self

    @property
    def hidden(self) -> "Generator":
        self.style(Mod.hidden)
        return self

    @property
    def strikethrough(self) -> "Generator":
        self.style(Mod.strikethrough)
        return self

    # Foreground colors

    @property
    def black(self) -> "Generator":
        self.style(Color.black)
        return self

    @property
    def red(self) -> "Generator":
        self.style(Color.red)
        return self

    @property
    def green(self) -> "Generator":
        self.style(Color.green)
        return self

    @property
    def yellow(self) -> "Generator":
        self.style(Color.yellow)
        return self

    @property
    def blue(self) -> "Generator":
        self.style(Color.blue)
        return self

    @property
    def magenta(self) -> "Generator":
        self.style(Color.magenta)
        return self

    @property
    def cyan(self) -> "Generator":
        self.style(Color.cyan)
        return self

    @property
    def white(self) -> "Generator":
        self.style(Color.white)
        return self

    @property
    def black_bright(self) -> "Generator":
        self.style(Color.black_bright)
        return self

    @property
    def red_bright(self) -> "Generator":
        self.style(Color.red_bright)
        return self

    @property
    def green_bright(self) -> "Generator":
        self.style(Color.green_bright)
        return self

    @property
    def yellow_bright(self) -> "Generator":
        self.style(Color.yellow_bright)
        return self

    @property
    def blue_bright(self) -> "Generator":
        self.style(Color.blue_bright)
        return self

    @property
    def magenta_bright(self) -> "Generator":
        self.style(Color.magenta_bright)
        return self

    @property
    def cyan_bright(self) -> "Generator":
        self.style(Color.cyan_bright)
        return self

    @property
    def white_bright(self) -> "Generator":
        self.style(Color.white_bright)
        return self

    @property
    def gray(self) -> "Generator":
        self.style(Color.gray)
        return self

    @property
    def grey(self) -> "Generator":
        self.style(Color.grey)
        return self

    # Background colors

    @property
    def bg_black(self) -> "Generator":
        self.style(BgColor.black)
        return self

    @property
    def bg_red(self) -> "Generator":
        self.style(BgColor.red)
        return self

    @property
    def bg_green(self) -> "Generator":
        self.style(BgColor.green)
        return self

    @property
    def bg_yellow(self) -> "Generator":
        self.style(BgColor.yellow)
        return self

    @property
    def bg_blue(self) -> "Generator":
        self.style(BgColor.blue)
        return self

    @property
    def bg_magenta(self) -> "Generator":
        self.style(BgColor.magenta)
        return self

    @property
    def bg_cyan(self) -> "Generator":
        self.style(BgColor.cyan)
        return self

    @property
    def bg_white(self) -> "Generator":
        self.style(BgColor.white)
        return self

    @property
    def bg_black_bright(self) -> "Generator":
        self.style(BgColor.black_bright)
        return self

    @property
    def bg_red_bright(self) -> "Generator":
        self.style(BgColor.red_bright)
        return self

    @property
    def bg_green_bright(self) -> "Generator":
        self.style(BgColor.green_bright)
        return self

    @property
    def bg_yellow_bright(self) -> "Generator":
        self.style(BgColor.yellow_bright)
        return self

    @property
    def bg_blue_bright(self) -> "Generator":
        self.style(BgColor.blue_bright)
        return self

    @property
    def bg_magenta_bright(self) -> "Generator":
        self.style(BgColor.magenta_bright)
        return self

    @property
    def bg_cyan_bright(self) -> "Generator":
        self.style(BgColor.cyan_bright)
        return self

    @property
    def bg_white_bright(self) -> "Generator":
        self.style(BgColor.white_bright)
        return self

    @property
    def bg_gray(self) -> "Generator":
        self.style(BgColor.gray)
        return self

    @property
    def bg_grey(self) -> "Generator":
        self.style(BgColor.grey)
        return self

    # rgb/hex

    def rgb(self, r: int, g: int, b: int) -> "Generator":
        code = _get_code_from_rgb(r, g, b, self._mode, background=False)
        if code is not None:
            self._codes.append(code)
        return self

    def hex(self, hex: str) -> "Generator":
        r, g, b = ansi_codes.hex_to_rgb(hex)
        return self.rgb(r, g, b)

    def bg_rgb(self, r: int, g: int, b: int) -> "Generator":
        code = _get_code_from_rgb(r, g, b, self._mode, background=True)
        if code is not None:
            self._codes.append(code)
        return self

    def bg_hex(self, hex: str) -> "Generator":
        r, g, b = ansi_codes.hex_to_rgb(hex)
        return self.bg_rgb(r, g, b)


class Chalk:
    def __init__(self, mode: ColorMode = ColorMode.FullTrueColor):
        self._mode = mode

    # Internal helpers

    def _create_generator_from_ansi_16_code(self, ansi_16_code: Ansi16Code) -> "Generator":
        on, off = ansi_16_code
        return Generator(
            mode=self._mode,
            codes=[Code(on=wrap_ansi_16(on), off=wrap_ansi_16(off))],
        )

    # General style function

    def style(self, code: Union[Code, Ansi16Code]) -> Generator:
        g = Generator(self._mode, [])
        g.style(code)
        return g

    # Modifiers

    @property
    def reset(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Mod.reset)

    @property
    def bold(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Mod.bold)

    @property
    def dim(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Mod.dim)

    @property
    def italic(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Mod.italic)

    @property
    def underline(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Mod.underline)

    @property
    def overline(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Mod.overline)

    @property
    def hidden(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Mod.hidden)

    @property
    def strikethrough(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Mod.strikethrough)

    # Foreground colors

    @property
    def black(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.black)

    @property
    def red(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.red)

    @property
    def green(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.green)

    @property
    def yellow(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.yellow)

    @property
    def blue(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.blue)

    @property
    def magenta(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.magenta)

    @property
    def cyan(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.cyan)

    @property
    def white(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.white)

    @property
    def black_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.black_bright)

    @property
    def red_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.red_bright)

    @property
    def green_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.green_bright)

    @property
    def yellow_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.yellow_bright)

    @property
    def blue_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.blue_bright)

    @property
    def magenta_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.magenta_bright)

    @property
    def cyan_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.cyan_bright)

    @property
    def white_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.white_bright)

    @property
    def gray(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.gray)

    @property
    def grey(self) -> Generator:
        return self._create_generator_from_ansi_16_code(Color.grey)

    # Background colors

    @property
    def bg_black(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.black)

    @property
    def bg_red(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.red)

    @property
    def bg_green(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.green)

    @property
    def bg_yellow(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.yellow)

    @property
    def bg_blue(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.blue)

    @property
    def bg_magenta(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.magenta)

    @property
    def bg_cyan(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.cyan)

    @property
    def bg_white(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.white)

    @property
    def bg_black_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.black_bright)

    @property
    def bg_red_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.red_bright)

    @property
    def bg_green_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.green_bright)

    @property
    def bg_yellow_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.yellow_bright)

    @property
    def bg_blue_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.blue_bright)

    @property
    def bg_magenta_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.magenta_bright)

    @property
    def bg_cyan_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.cyan_bright)

    @property
    def bg_white_bright(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.white_bright)

    @property
    def bg_gray(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.gray)

    @property
    def bg_grey(self) -> Generator:
        return self._create_generator_from_ansi_16_code(BgColor.grey)

    # rgb/hex

    def rgb(self, r: int, g: int, b: int) -> Generator:
        code = _get_code_from_rgb(r, g, b, self._mode, background=False)
        return Generator(self._mode, [code] if code is not None else [])

    def hex(self, hex: str) -> Generator:
        r, g, b = ansi_codes.hex_to_rgb(hex)
        return self.rgb(r, g, b)

    def bg_rgb(self, r: int, g: int, b: int) -> Generator:
        code = _get_code_from_rgb(r, g, b, self._mode, background=True)
        return Generator(self._mode, [code] if code is not None else [])

    def bg_hex(self, hex: str) -> Generator:
        r, g, b = ansi_codes.hex_to_rgb(hex)
        return self.bg_rgb(r, g, b)


def _get_code_from_rgb(r: int, g: int, b: int, mode: ColorMode, background: bool) -> Optional[Code]:
    if mode == ColorMode.FullTrueColor:
        code = wrap_ansi_16m(r, g, b, background=background)
    elif mode == ColorMode.Extended256:
        code_256 = ansi_codes.rgb_to_ansi_256(r, g, b)
        code = wrap_ansi_256(code_256, background=background)
    elif mode == ColorMode.Basic16:
        code_256 = ansi_codes.rgb_to_ansi_256(r, g, b)
        code_16 = ansi_codes.ansi_256_to_ansi_16(code_256)
        code = wrap_ansi_16(code_16, background=background)
    else:
        return None

    close = ansi_codes.BG_COLOR_CLOSE if background else ansi_codes.COLOR_CLOSE
    return Code(on=code, off=wrap_ansi_16(close))


def create_chalk() -> Chalk:
    return Chalk()


chalk = create_chalk()
