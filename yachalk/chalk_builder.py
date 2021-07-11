import re

from typing import List, Union

from .types import ColorMode, Code
from .ansi import (
    Mod,
    Color,
    BgColor,
    Ansi16Code,
    wrap_ansi_16,
)
from .utils import get_code_from_rgb, hex_to_rgb


class ChalkBuilder:
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

    def style(self, code: Union[Code, Ansi16Code]) -> "ChalkBuilder":
        if self._mode != ColorMode.AllOff:
            if isinstance(code, Ansi16Code):
                code = Code(on=wrap_ansi_16(code.on), off=wrap_ansi_16(code.off))
            self._codes.append(code)
        return self

    # Modifiers

    @property
    def reset(self) -> "ChalkBuilder":
        self.style(Mod.reset)
        return self

    @property
    def bold(self) -> "ChalkBuilder":
        self.style(Mod.bold)
        return self

    @property
    def dim(self) -> "ChalkBuilder":
        self.style(Mod.dim)
        return self

    @property
    def italic(self) -> "ChalkBuilder":
        self.style(Mod.italic)
        return self

    @property
    def underline(self) -> "ChalkBuilder":
        self.style(Mod.underline)
        return self

    @property
    def overline(self) -> "ChalkBuilder":
        self.style(Mod.overline)
        return self

    @property
    def hidden(self) -> "ChalkBuilder":
        self.style(Mod.hidden)
        return self

    @property
    def strikethrough(self) -> "ChalkBuilder":
        self.style(Mod.strikethrough)
        return self

    # Foreground colors

    @property
    def black(self) -> "ChalkBuilder":
        self.style(Color.black)
        return self

    @property
    def red(self) -> "ChalkBuilder":
        self.style(Color.red)
        return self

    @property
    def green(self) -> "ChalkBuilder":
        self.style(Color.green)
        return self

    @property
    def yellow(self) -> "ChalkBuilder":
        self.style(Color.yellow)
        return self

    @property
    def blue(self) -> "ChalkBuilder":
        self.style(Color.blue)
        return self

    @property
    def magenta(self) -> "ChalkBuilder":
        self.style(Color.magenta)
        return self

    @property
    def cyan(self) -> "ChalkBuilder":
        self.style(Color.cyan)
        return self

    @property
    def white(self) -> "ChalkBuilder":
        self.style(Color.white)
        return self

    @property
    def black_bright(self) -> "ChalkBuilder":
        self.style(Color.black_bright)
        return self

    @property
    def red_bright(self) -> "ChalkBuilder":
        self.style(Color.red_bright)
        return self

    @property
    def green_bright(self) -> "ChalkBuilder":
        self.style(Color.green_bright)
        return self

    @property
    def yellow_bright(self) -> "ChalkBuilder":
        self.style(Color.yellow_bright)
        return self

    @property
    def blue_bright(self) -> "ChalkBuilder":
        self.style(Color.blue_bright)
        return self

    @property
    def magenta_bright(self) -> "ChalkBuilder":
        self.style(Color.magenta_bright)
        return self

    @property
    def cyan_bright(self) -> "ChalkBuilder":
        self.style(Color.cyan_bright)
        return self

    @property
    def white_bright(self) -> "ChalkBuilder":
        self.style(Color.white_bright)
        return self

    @property
    def gray(self) -> "ChalkBuilder":
        self.style(Color.gray)
        return self

    @property
    def grey(self) -> "ChalkBuilder":
        self.style(Color.grey)
        return self

    # Background colors

    @property
    def bg_black(self) -> "ChalkBuilder":
        self.style(BgColor.black)
        return self

    @property
    def bg_red(self) -> "ChalkBuilder":
        self.style(BgColor.red)
        return self

    @property
    def bg_green(self) -> "ChalkBuilder":
        self.style(BgColor.green)
        return self

    @property
    def bg_yellow(self) -> "ChalkBuilder":
        self.style(BgColor.yellow)
        return self

    @property
    def bg_blue(self) -> "ChalkBuilder":
        self.style(BgColor.blue)
        return self

    @property
    def bg_magenta(self) -> "ChalkBuilder":
        self.style(BgColor.magenta)
        return self

    @property
    def bg_cyan(self) -> "ChalkBuilder":
        self.style(BgColor.cyan)
        return self

    @property
    def bg_white(self) -> "ChalkBuilder":
        self.style(BgColor.white)
        return self

    @property
    def bg_black_bright(self) -> "ChalkBuilder":
        self.style(BgColor.black_bright)
        return self

    @property
    def bg_red_bright(self) -> "ChalkBuilder":
        self.style(BgColor.red_bright)
        return self

    @property
    def bg_green_bright(self) -> "ChalkBuilder":
        self.style(BgColor.green_bright)
        return self

    @property
    def bg_yellow_bright(self) -> "ChalkBuilder":
        self.style(BgColor.yellow_bright)
        return self

    @property
    def bg_blue_bright(self) -> "ChalkBuilder":
        self.style(BgColor.blue_bright)
        return self

    @property
    def bg_magenta_bright(self) -> "ChalkBuilder":
        self.style(BgColor.magenta_bright)
        return self

    @property
    def bg_cyan_bright(self) -> "ChalkBuilder":
        self.style(BgColor.cyan_bright)
        return self

    @property
    def bg_white_bright(self) -> "ChalkBuilder":
        self.style(BgColor.white_bright)
        return self

    @property
    def bg_gray(self) -> "ChalkBuilder":
        self.style(BgColor.gray)
        return self

    @property
    def bg_grey(self) -> "ChalkBuilder":
        self.style(BgColor.grey)
        return self

    # rgb/hex

    def rgb(self, r: int, g: int, b: int) -> "ChalkBuilder":
        code = get_code_from_rgb(r, g, b, self._mode, background=False)
        if code is not None:
            self._codes.append(code)
        return self

    def hex(self, hex: str) -> "ChalkBuilder":
        r, g, b = hex_to_rgb(hex)
        return self.rgb(r, g, b)

    def bg_rgb(self, r: int, g: int, b: int) -> "ChalkBuilder":
        code = get_code_from_rgb(r, g, b, self._mode, background=True)
        if code is not None:
            self._codes.append(code)
        return self

    def bg_hex(self, hex: str) -> "ChalkBuilder":
        r, g, b = hex_to_rgb(hex)
        return self.bg_rgb(r, g, b)
