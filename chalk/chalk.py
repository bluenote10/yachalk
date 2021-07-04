from typing import List, NamedTuple, Union


from .ansi_codes import Color, BgColor, Ansi16Code, wrap_ansi_16


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


class Chalk:
    @staticmethod
    def style(code: Union[Code, Ansi16Code]) -> Generator:
        g = Generator([])
        g.style(code)
        return g

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


def create_chalk() -> Chalk:
    return Chalk()


chalk = create_chalk()
