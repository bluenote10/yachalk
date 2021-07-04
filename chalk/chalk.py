import re

from typing import List, NamedTuple, Union


from .ansi_codes import Mod, Color, BgColor, Ansi16Code, wrap_ansi_16


class Code(NamedTuple):
    on: str
    off: str


class Generator:
    def __init__(self, codes: List[Code]):
        self._codes = codes

    def __call__(self, s: str) -> str:
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

    @staticmethod
    def create_from_ansi_16_code(ansi_16_code: Ansi16Code) -> "Generator":
        on, off = ansi_16_code
        return Generator(
            codes=[Code(on=wrap_ansi_16(on), off=wrap_ansi_16(off))],
        )

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


class Chalk:
    @staticmethod
    def style(code: Union[Code, Ansi16Code]) -> Generator:
        g = Generator([])
        g.style(code)
        return g

    # Modifiers

    @property
    def reset(self) -> Generator:
        return Generator.create_from_ansi_16_code(Mod.reset)

    @property
    def bold(self) -> Generator:
        return Generator.create_from_ansi_16_code(Mod.bold)

    @property
    def dim(self) -> Generator:
        return Generator.create_from_ansi_16_code(Mod.dim)

    @property
    def italic(self) -> Generator:
        return Generator.create_from_ansi_16_code(Mod.italic)

    @property
    def underline(self) -> Generator:
        return Generator.create_from_ansi_16_code(Mod.underline)

    @property
    def overline(self) -> Generator:
        return Generator.create_from_ansi_16_code(Mod.overline)

    @property
    def hidden(self) -> Generator:
        return Generator.create_from_ansi_16_code(Mod.hidden)

    @property
    def strikethrough(self) -> Generator:
        return Generator.create_from_ansi_16_code(Mod.strikethrough)

    # Foreground colors

    @property
    def black(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.black)

    @property
    def red(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.red)

    @property
    def green(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.green)

    @property
    def yellow(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.yellow)

    @property
    def blue(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.blue)

    @property
    def magenta(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.magenta)

    @property
    def cyan(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.cyan)

    @property
    def white(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.white)

    @property
    def black_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.black_bright)

    @property
    def red_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.red_bright)

    @property
    def green_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.green_bright)

    @property
    def yellow_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.yellow_bright)

    @property
    def blue_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.blue_bright)

    @property
    def magenta_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.magenta_bright)

    @property
    def cyan_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.cyan_bright)

    @property
    def white_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.white_bright)

    @property
    def gray(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.gray)

    @property
    def grey(self) -> Generator:
        return Generator.create_from_ansi_16_code(Color.grey)

    # Background colors

    @property
    def bg_black(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.black)

    @property
    def bg_red(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.red)

    @property
    def bg_green(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.green)

    @property
    def bg_yellow(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.yellow)

    @property
    def bg_blue(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.blue)

    @property
    def bg_magenta(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.magenta)

    @property
    def bg_cyan(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.cyan)

    @property
    def bg_white(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.white)

    @property
    def bg_black_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.black_bright)

    @property
    def bg_red_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.red_bright)

    @property
    def bg_green_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.green_bright)

    @property
    def bg_yellow_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.yellow_bright)

    @property
    def bg_blue_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.blue_bright)

    @property
    def bg_magenta_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.magenta_bright)

    @property
    def bg_cyan_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.cyan_bright)

    @property
    def bg_white_bright(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.white_bright)

    @property
    def bg_gray(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.gray)

    @property
    def bg_grey(self) -> Generator:
        return Generator.create_from_ansi_16_code(BgColor.grey)


def create_chalk() -> Chalk:
    return Chalk()


chalk = create_chalk()
