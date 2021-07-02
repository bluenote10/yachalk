from .ansi_codes import Colors, BgColors, wrap_ansi_16


class Generator:
    def __init__(self, on, off):
        self.on = on
        self.off = off

    def __call__(self, s: str) -> str:
        all_on = "".join(self.on)
        all_off = "".join(self.off)
        return all_on + s + all_off

    @staticmethod
    def create_from_color(color):
        on, off = color
        return Generator([wrap_ansi_16(on)], [wrap_ansi_16(off)])

    @property
    def bg_black(self) -> "Generator":
        on, off = BgColors.bg_black
        self.on.append(wrap_ansi_16(on))
        self.off.append(wrap_ansi_16(off))
        return self

    @property
    def bg_red(self) -> "Generator":
        on, off = BgColors.bg_red
        self.on.append(wrap_ansi_16(on))
        self.off.append(wrap_ansi_16(off))
        return self

    @property
    def bg_green(self) -> "Generator":
        on, off = BgColors.bg_green
        self.on.append(wrap_ansi_16(on))
        self.off.append(wrap_ansi_16(off))
        return self

    @property
    def bg_yellow(self) -> "Generator":
        on, off = BgColors.bg_yellow
        self.on.append(wrap_ansi_16(on))
        self.off.append(wrap_ansi_16(off))
        return self

    @property
    def bg_blue(self) -> "Generator":
        on, off = BgColors.bg_blue
        self.on.append(wrap_ansi_16(on))
        self.off.append(wrap_ansi_16(off))
        return self

    @property
    def bg_magenta(self) -> "Generator":
        on, off = BgColors.bg_magenta
        self.on.append(wrap_ansi_16(on))
        self.off.append(wrap_ansi_16(off))
        return self

    @property
    def bg_cyan(self) -> "Generator":
        on, off = BgColors.bg_cyan
        self.on.append(wrap_ansi_16(on))
        self.off.append(wrap_ansi_16(off))
        return self

    @property
    def bg_white(self) -> "Generator":
        on, off = BgColors.bg_white
        self.on.append(wrap_ansi_16(on))
        self.off.append(wrap_ansi_16(off))
        return self


class Chalk:
    @property
    def black(self) -> Generator:
        return Generator.create_from_color(Colors.black)

    @property
    def red(self) -> Generator:
        return Generator.create_from_color(Colors.red)

    @property
    def green(self) -> Generator:
        return Generator.create_from_color(Colors.green)

    @property
    def yellow(self) -> Generator:
        return Generator.create_from_color(Colors.yellow)

    @property
    def blue(self) -> Generator:
        return Generator.create_from_color(Colors.blue)

    @property
    def magenta(self) -> Generator:
        return Generator.create_from_color(Colors.magenta)

    @property
    def cyan(self) -> Generator:
        return Generator.create_from_color(Colors.cyan)

    @property
    def white(self) -> Generator:
        return Generator.create_from_color(Colors.white)


def create_chalk():
    return Chalk()


chalk = create_chalk()
