from typing import Union

from .types import ColorMode, Code
from .ansi import (
    Mod,
    Color,
    BgColor,
    Ansi16Code,
    wrap_ansi_16,
)
from .utils import get_code_from_rgb, hex_to_rgb
from .chalk_builder import ChalkBuilder


class ChalkFactory:
    def __init__(self, mode: ColorMode = ColorMode.FullTrueColor):
        self._mode = mode

    # Internal helpers

    def _create_generator_from_ansi_16_code(self, ansi_16_code: Ansi16Code) -> "ChalkBuilder":
        if self._mode != ColorMode.AllOff:
            on, off = ansi_16_code
            codes = [Code(on=wrap_ansi_16(on), off=wrap_ansi_16(off))]
        else:
            codes = []
        return ChalkBuilder(
            mode=self._mode,
            codes=codes,
        )

    # Color mode control

    def get_color_mode(self) -> ColorMode:
        return self._mode

    def set_color_mode(self, mode: ColorMode) -> None:
        self._mode = mode

    def disable_all_ansi(self) -> None:
        self.set_color_mode(ColorMode.AllOff)

    def enable_basic_colors(self) -> None:
        self.set_color_mode(ColorMode.Basic16)

    def enable_extended_colors(self) -> None:
        self.set_color_mode(ColorMode.Extended256)

    def enable_full_colors(self) -> None:
        self.set_color_mode(ColorMode.FullTrueColor)

    # General style function

    def style(self, code: Union[Code, Ansi16Code]) -> ChalkBuilder:
        g = ChalkBuilder(self._mode, [])
        g.style(code)
        return g

    # Modifiers

    @property
    def reset(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Mod.reset)

    @property
    def bold(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Mod.bold)

    @property
    def dim(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Mod.dim)

    @property
    def italic(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Mod.italic)

    @property
    def underline(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Mod.underline)

    @property
    def overline(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Mod.overline)

    @property
    def hidden(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Mod.hidden)

    @property
    def strikethrough(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Mod.strikethrough)

    # Foreground colors

    @property
    def black(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.black)

    @property
    def red(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.red)

    @property
    def green(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.green)

    @property
    def yellow(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.yellow)

    @property
    def blue(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.blue)

    @property
    def magenta(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.magenta)

    @property
    def cyan(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.cyan)

    @property
    def white(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.white)

    @property
    def black_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.black_bright)

    @property
    def red_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.red_bright)

    @property
    def green_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.green_bright)

    @property
    def yellow_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.yellow_bright)

    @property
    def blue_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.blue_bright)

    @property
    def magenta_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.magenta_bright)

    @property
    def cyan_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.cyan_bright)

    @property
    def white_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.white_bright)

    @property
    def gray(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.gray)

    @property
    def grey(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(Color.grey)

    # Background colors

    @property
    def bg_black(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.black)

    @property
    def bg_red(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.red)

    @property
    def bg_green(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.green)

    @property
    def bg_yellow(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.yellow)

    @property
    def bg_blue(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.blue)

    @property
    def bg_magenta(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.magenta)

    @property
    def bg_cyan(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.cyan)

    @property
    def bg_white(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.white)

    @property
    def bg_black_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.black_bright)

    @property
    def bg_red_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.red_bright)

    @property
    def bg_green_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.green_bright)

    @property
    def bg_yellow_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.yellow_bright)

    @property
    def bg_blue_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.blue_bright)

    @property
    def bg_magenta_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.magenta_bright)

    @property
    def bg_cyan_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.cyan_bright)

    @property
    def bg_white_bright(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.white_bright)

    @property
    def bg_gray(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.gray)

    @property
    def bg_grey(self) -> ChalkBuilder:
        return self._create_generator_from_ansi_16_code(BgColor.grey)

    # rgb/hex

    def rgb(self, r: int, g: int, b: int) -> ChalkBuilder:
        code = get_code_from_rgb(r, g, b, self._mode, background=False)
        return ChalkBuilder(self._mode, [code] if code is not None else [])

    def hex(self, hex: str) -> ChalkBuilder:
        r, g, b = hex_to_rgb(hex)
        return self.rgb(r, g, b)

    def bg_rgb(self, r: int, g: int, b: int) -> ChalkBuilder:
        code = get_code_from_rgb(r, g, b, self._mode, background=True)
        return ChalkBuilder(self._mode, [code] if code is not None else [])

    def bg_hex(self, hex: str) -> ChalkBuilder:
        r, g, b = hex_to_rgb(hex)
        return self.bg_rgb(r, g, b)
