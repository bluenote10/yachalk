from typing import List, Set

import pytest

from yachalk.types import ColorMode
from yachalk.chalk_factory import ChalkFactory
from yachalk.chalk_builder import ChalkBuilder
from yachalk.ansi import Color, BgColor

from helper import r


@pytest.fixture
def chalk() -> ChalkFactory:
    return ChalkFactory(mode=ColorMode.FullTrueColor)


def test_interface_consistency(chalk: ChalkFactory) -> None:
    def filter_names(names: List[str]) -> Set[str]:
        return set(name for name in names if not name.startswith("__"))

    funcs_factory = filter_names(dir(chalk))
    funcs_generator = filter_names(dir(ChalkBuilder(mode=ColorMode.FullTrueColor, codes=[])))

    funcs_factory -= {
        "set_color_mode",
        "get_color_mode",
        "disable_all_ansi",
        "enable_basic_colors",
        "enable_extended_colors",
        "enable_full_colors",
        "_create_generator_from_ansi_16_code",
    }
    funcs_generator -= {"_codes"}

    print(funcs_factory)
    print(funcs_generator)

    assert funcs_factory == funcs_generator


def test_basics(chalk: ChalkFactory) -> None:
    assert r(chalk.reset("foo")) == r("\x1b[0mfoo\x1b[0m")
    assert r(chalk.bold("foo")) == r("\x1b[1mfoo\x1b[22m")
    assert r(chalk.dim("foo")) == r("\x1b[2mfoo\x1b[22m")
    assert r(chalk.italic("foo")) == r("\x1b[3mfoo\x1b[23m")
    assert r(chalk.underline("foo")) == r("\x1b[4mfoo\x1b[24m")
    assert r(chalk.overline("foo")) == r("\x1b[53mfoo\x1b[55m")
    assert r(chalk.hidden("foo")) == r("\x1b[8mfoo\x1b[28m")
    assert r(chalk.strikethrough("foo")) == r("\x1b[9mfoo\x1b[29m")

    assert r(chalk.black("foo")) == r("\x1b[30mfoo\x1b[39m")
    assert r(chalk.red("foo")) == r("\x1b[31mfoo\x1b[39m")
    assert r(chalk.green("foo")) == r("\x1b[32mfoo\x1b[39m")
    assert r(chalk.yellow("foo")) == r("\x1b[33mfoo\x1b[39m")
    assert r(chalk.blue("foo")) == r("\x1b[34mfoo\x1b[39m")
    assert r(chalk.magenta("foo")) == r("\x1b[35mfoo\x1b[39m")
    assert r(chalk.cyan("foo")) == r("\x1b[36mfoo\x1b[39m")
    assert r(chalk.white("foo")) == r("\x1b[37mfoo\x1b[39m")

    assert r(chalk.black_bright("foo")) == r("\x1b[90mfoo\x1b[39m")
    assert r(chalk.red_bright("foo")) == r("\x1b[91mfoo\x1b[39m")
    assert r(chalk.green_bright("foo")) == r("\x1b[92mfoo\x1b[39m")
    assert r(chalk.yellow_bright("foo")) == r("\x1b[93mfoo\x1b[39m")
    assert r(chalk.blue_bright("foo")) == r("\x1b[94mfoo\x1b[39m")
    assert r(chalk.magenta_bright("foo")) == r("\x1b[95mfoo\x1b[39m")
    assert r(chalk.cyan_bright("foo")) == r("\x1b[96mfoo\x1b[39m")
    assert r(chalk.white_bright("foo")) == r("\x1b[97mfoo\x1b[39m")

    assert r(chalk.gray("foo")) == r("\x1b[90mfoo\x1b[39m")
    assert r(chalk.grey("foo")) == r("\x1b[90mfoo\x1b[39m")

    assert r(chalk.bg_black("foo")) == r("\x1b[40mfoo\x1b[49m")
    assert r(chalk.bg_red("foo")) == r("\x1b[41mfoo\x1b[49m")
    assert r(chalk.bg_green("foo")) == r("\x1b[42mfoo\x1b[49m")
    assert r(chalk.bg_yellow("foo")) == r("\x1b[43mfoo\x1b[49m")
    assert r(chalk.bg_blue("foo")) == r("\x1b[44mfoo\x1b[49m")
    assert r(chalk.bg_magenta("foo")) == r("\x1b[45mfoo\x1b[49m")
    assert r(chalk.bg_cyan("foo")) == r("\x1b[46mfoo\x1b[49m")
    assert r(chalk.bg_white("foo")) == r("\x1b[47mfoo\x1b[49m")

    assert r(chalk.bg_black_bright("foo")) == r("\x1b[100mfoo\x1b[49m")
    assert r(chalk.bg_red_bright("foo")) == r("\x1b[101mfoo\x1b[49m")
    assert r(chalk.bg_green_bright("foo")) == r("\x1b[102mfoo\x1b[49m")
    assert r(chalk.bg_yellow_bright("foo")) == r("\x1b[103mfoo\x1b[49m")
    assert r(chalk.bg_blue_bright("foo")) == r("\x1b[104mfoo\x1b[49m")
    assert r(chalk.bg_magenta_bright("foo")) == r("\x1b[105mfoo\x1b[49m")
    assert r(chalk.bg_cyan_bright("foo")) == r("\x1b[106mfoo\x1b[49m")
    assert r(chalk.bg_white_bright("foo")) == r("\x1b[107mfoo\x1b[49m")

    assert r(chalk.bg_gray("foo")) == r("\x1b[100mfoo\x1b[49m")
    assert r(chalk.bg_grey("foo")) == r("\x1b[100mfoo\x1b[49m")


def test_basics_chained() -> None:
    def gen() -> ChalkBuilder:
        return ChalkBuilder(ColorMode.FullTrueColor, [])

    assert r(gen().reset("foo")) == r("\x1b[0mfoo\x1b[0m")
    assert r(gen().bold("foo")) == r("\x1b[1mfoo\x1b[22m")
    assert r(gen().dim("foo")) == r("\x1b[2mfoo\x1b[22m")
    assert r(gen().italic("foo")) == r("\x1b[3mfoo\x1b[23m")
    assert r(gen().underline("foo")) == r("\x1b[4mfoo\x1b[24m")
    assert r(gen().overline("foo")) == r("\x1b[53mfoo\x1b[55m")
    assert r(gen().hidden("foo")) == r("\x1b[8mfoo\x1b[28m")
    assert r(gen().strikethrough("foo")) == r("\x1b[9mfoo\x1b[29m")

    assert r(gen().black("foo")) == r("\x1b[30mfoo\x1b[39m")
    assert r(gen().red("foo")) == r("\x1b[31mfoo\x1b[39m")
    assert r(gen().green("foo")) == r("\x1b[32mfoo\x1b[39m")
    assert r(gen().yellow("foo")) == r("\x1b[33mfoo\x1b[39m")
    assert r(gen().blue("foo")) == r("\x1b[34mfoo\x1b[39m")
    assert r(gen().magenta("foo")) == r("\x1b[35mfoo\x1b[39m")
    assert r(gen().cyan("foo")) == r("\x1b[36mfoo\x1b[39m")
    assert r(gen().white("foo")) == r("\x1b[37mfoo\x1b[39m")

    assert r(gen().black_bright("foo")) == r("\x1b[90mfoo\x1b[39m")
    assert r(gen().red_bright("foo")) == r("\x1b[91mfoo\x1b[39m")
    assert r(gen().green_bright("foo")) == r("\x1b[92mfoo\x1b[39m")
    assert r(gen().yellow_bright("foo")) == r("\x1b[93mfoo\x1b[39m")
    assert r(gen().blue_bright("foo")) == r("\x1b[94mfoo\x1b[39m")
    assert r(gen().magenta_bright("foo")) == r("\x1b[95mfoo\x1b[39m")
    assert r(gen().cyan_bright("foo")) == r("\x1b[96mfoo\x1b[39m")
    assert r(gen().white_bright("foo")) == r("\x1b[97mfoo\x1b[39m")

    assert r(gen().gray("foo")) == r("\x1b[90mfoo\x1b[39m")
    assert r(gen().grey("foo")) == r("\x1b[90mfoo\x1b[39m")

    assert r(gen().bg_black("foo")) == r("\x1b[40mfoo\x1b[49m")
    assert r(gen().bg_red("foo")) == r("\x1b[41mfoo\x1b[49m")
    assert r(gen().bg_green("foo")) == r("\x1b[42mfoo\x1b[49m")
    assert r(gen().bg_yellow("foo")) == r("\x1b[43mfoo\x1b[49m")
    assert r(gen().bg_blue("foo")) == r("\x1b[44mfoo\x1b[49m")
    assert r(gen().bg_magenta("foo")) == r("\x1b[45mfoo\x1b[49m")
    assert r(gen().bg_cyan("foo")) == r("\x1b[46mfoo\x1b[49m")
    assert r(gen().bg_white("foo")) == r("\x1b[47mfoo\x1b[49m")

    assert r(gen().bg_black_bright("foo")) == r("\x1b[100mfoo\x1b[49m")
    assert r(gen().bg_red_bright("foo")) == r("\x1b[101mfoo\x1b[49m")
    assert r(gen().bg_green_bright("foo")) == r("\x1b[102mfoo\x1b[49m")
    assert r(gen().bg_yellow_bright("foo")) == r("\x1b[103mfoo\x1b[49m")
    assert r(gen().bg_blue_bright("foo")) == r("\x1b[104mfoo\x1b[49m")
    assert r(gen().bg_magenta_bright("foo")) == r("\x1b[105mfoo\x1b[49m")
    assert r(gen().bg_cyan_bright("foo")) == r("\x1b[106mfoo\x1b[49m")
    assert r(gen().bg_white_bright("foo")) == r("\x1b[107mfoo\x1b[49m")

    assert r(gen().bg_gray("foo")) == r("\x1b[100mfoo\x1b[49m")
    assert r(gen().bg_grey("foo")) == r("\x1b[100mfoo\x1b[49m")


def test_rgb_hex() -> None:
    chalk = ChalkFactory(mode=ColorMode.FullTrueColor)
    assert r(chalk.rgb(20, 40, 60)("foo")) == r("\x1b[38;2;20;40;60mfoo\x1b[39m")
    assert r(chalk.hex("14283c")("foo")) == r("\x1b[38;2;20;40;60mfoo\x1b[39m")
    assert r(chalk.bg_rgb(20, 40, 60)("foo")) == r("\x1b[48;2;20;40;60mfoo\x1b[49m")
    assert r(chalk.bg_hex("14283c")("foo")) == r("\x1b[48;2;20;40;60mfoo\x1b[49m")

    chalk = ChalkFactory(mode=ColorMode.Extended256)
    assert r(chalk.rgb(20, 40, 60)("foo")) == r("\x1b[38;5;23mfoo\x1b[39m")
    assert r(chalk.hex("14283c")("foo")) == r("\x1b[38;5;23mfoo\x1b[39m")
    assert r(chalk.bg_rgb(20, 40, 60)("foo")) == r("\x1b[48;5;23mfoo\x1b[49m")
    assert r(chalk.bg_hex("14283c")("foo")) == r("\x1b[48;5;23mfoo\x1b[49m")

    chalk = ChalkFactory(mode=ColorMode.Basic16)
    assert r(chalk.rgb(20, 40, 60)("foo")) == r("\x1b[30mfoo\x1b[39m")
    assert r(chalk.hex("14283c")("foo")) == r("\x1b[30mfoo\x1b[39m")
    assert r(chalk.bg_rgb(20, 40, 60)("foo")) == r("\x1b[40mfoo\x1b[49m")
    assert r(chalk.bg_hex("14283c")("foo")) == r("\x1b[40mfoo\x1b[49m")

    chalk = ChalkFactory(mode=ColorMode.AllOff)
    assert r(chalk.rgb(20, 40, 60)("foo")) == r("foo")
    assert r(chalk.hex("14283c")("foo")) == r("foo")
    assert r(chalk.bg_rgb(20, 40, 60)("foo")) == r("foo")
    assert r(chalk.bg_hex("14283c")("foo")) == r("foo")


def test_rgb_hex_chained() -> None:
    def gen3() -> ChalkBuilder:
        return ChalkBuilder(ColorMode.FullTrueColor, [])

    assert r(gen3().rgb(20, 40, 60)("foo")) == r("\x1b[38;2;20;40;60mfoo\x1b[39m")
    assert r(gen3().hex("14283c")("foo")) == r("\x1b[38;2;20;40;60mfoo\x1b[39m")
    assert r(gen3().bg_rgb(20, 40, 60)("foo")) == r("\x1b[48;2;20;40;60mfoo\x1b[49m")
    assert r(gen3().bg_hex("14283c")("foo")) == r("\x1b[48;2;20;40;60mfoo\x1b[49m")

    def gen2() -> ChalkBuilder:
        return ChalkBuilder(ColorMode.Extended256, [])

    assert r(gen2().rgb(20, 40, 60)("foo")) == r("\x1b[38;5;23mfoo\x1b[39m")
    assert r(gen2().hex("14283c")("foo")) == r("\x1b[38;5;23mfoo\x1b[39m")
    assert r(gen2().bg_rgb(20, 40, 60)("foo")) == r("\x1b[48;5;23mfoo\x1b[49m")
    assert r(gen2().bg_hex("14283c")("foo")) == r("\x1b[48;5;23mfoo\x1b[49m")

    def gen1() -> ChalkBuilder:
        return ChalkBuilder(ColorMode.Basic16, [])

    assert r(gen1().rgb(20, 40, 60)("foo")) == r("\x1b[30mfoo\x1b[39m")
    assert r(gen1().hex("14283c")("foo")) == r("\x1b[30mfoo\x1b[39m")
    assert r(gen1().bg_rgb(20, 40, 60)("foo")) == r("\x1b[40mfoo\x1b[49m")
    assert r(gen1().bg_hex("14283c")("foo")) == r("\x1b[40mfoo\x1b[49m")

    def gen0() -> ChalkBuilder:
        return ChalkBuilder(ColorMode.AllOff, [])

    assert r(gen0().rgb(20, 40, 60)("foo")) == r("foo")
    assert r(gen0().hex("14283c")("foo")) == r("foo")
    assert r(gen0().bg_rgb(20, 40, 60)("foo")) == r("foo")
    assert r(gen0().bg_hex("14283c")("foo")) == r("foo")


def test_disabled_mode() -> None:
    chalk = ChalkFactory(mode=ColorMode.AllOff)
    assert r(chalk.black("foo")) == r("foo")
    assert r(chalk.style(Color.black)("foo")) == r("foo")

    def gen() -> ChalkBuilder:
        return ChalkBuilder(ColorMode.AllOff, [])

    assert r(gen().black("foo")) == r("foo")
    assert r(gen().style(Color.black)("foo")) == r("foo")


def test_manual_styling(chalk: ChalkFactory) -> None:
    assert chalk.style(Color.black)("foo") == "\x1b[30mfoo\x1b[39m"
    assert (
        chalk.style(Color.black).style(BgColor.white)("foo")
        == "\x1b[30m\x1b[47mfoo\x1b[39m\x1b[49m"
    )

    def gen() -> ChalkBuilder:
        return ChalkBuilder(ColorMode.FullTrueColor, [])

    assert gen().style(Color.black)("foo") == "\x1b[30mfoo\x1b[39m"
    assert (
        gen().style(Color.black).style(BgColor.white)("foo")
        == "\x1b[30m\x1b[47mfoo\x1b[39m\x1b[49m"
    )


def test_type_support(chalk: ChalkFactory) -> None:
    class Custom:
        def __str__(self) -> str:
            return "custom"

    assert r(chalk.black(42)) == r("\x1b[30m42\x1b[39m")
    assert r(chalk.black(1.0)) == r("\x1b[30m1.0\x1b[39m")
    assert r(chalk.black(True)) == r("\x1b[30mTrue\x1b[39m")
    assert r(chalk.black(Custom())) == r("\x1b[30mcustom\x1b[39m")


def test_vararg_support(chalk: ChalkFactory) -> None:
    assert r(chalk.black("a", "b", "c")) == r("\x1b[30ma b c\x1b[39m")
    assert r(chalk.black("a", "b", "c", sep="")) == r("\x1b[30mabc\x1b[39m")
    assert r(chalk.black(1, 2, 3)) == r("\x1b[30m1 2 3\x1b[39m")
    assert r(chalk.black(1, 2, 3, sep=", ")) == r("\x1b[30m1, 2, 3\x1b[39m")


def test_instance_is_configurable(chalk: ChalkFactory) -> None:
    assert chalk.get_color_mode() == ColorMode.FullTrueColor
    chalk.set_color_mode(ColorMode.AllOff)
    assert chalk.get_color_mode() == ColorMode.AllOff

    chalk.enable_full_colors()
    assert chalk.get_color_mode() == ColorMode.FullTrueColor

    chalk.enable_extended_colors()
    assert chalk.get_color_mode() == ColorMode.Extended256

    chalk.enable_basic_colors()
    assert chalk.get_color_mode() == ColorMode.Basic16

    chalk.disable_all_ansi()
    assert chalk.get_color_mode() == ColorMode.AllOff


def test_nested_reset(chalk: ChalkFactory) -> None:
    s = chalk.bold.blue(f"before {chalk.reset('reset')} after")
    assert r(s) == r(
        "\x1b[1m\x1b[34mbefore \x1b[22m\x1b[39m\x1b[0mreset\x1b[0m\x1b[1m\x1b[34m after\x1b[22m\x1b[39m"  # noqa
    )
    s = chalk.red(
        "outer "
        + chalk.bold.blue(f"before {chalk.reset('reset')} after")
        + " outer "
        + chalk.reset("reset")
        + " outer"
    )
    assert r(s) == r(
        "\x1b[31mouter \x1b[1m\x1b[34mbefore \x1b[22m\x1b[39m\x1b[31m\x1b[39m\x1b[0mreset\x1b[0m\x1b[31m\x1b[1m\x1b[34m after\x1b[22m\x1b[39m\x1b[31m outer \x1b[39m\x1b[0mreset\x1b[0m\x1b[31m outer\x1b[39m"  # noqa
    )


# -----------------------------------------------------------------------------
# Test cases from Chalk
# -----------------------------------------------------------------------------


def test_support_nesting_styles_of_same_type(chalk: ChalkFactory) -> None:
    assert r(chalk.red(" a " + chalk.yellow(" b " + chalk.green(" c ") + " b ") + " a ")) == r(
        "\x1b[31m a \x1b[33m b \x1b[32m c \x1b[39m\x1b[31m\x1b[33m b \x1b[39m\x1b[31m a \x1b[39m"
    )


def test_line_breaks_should_close_and_open_colors(chalk: ChalkFactory) -> None:
    assert r(chalk.grey("hello\nworld")) == r(
        "\u001b[90mhello\u001b[39m\n\u001b[90mworld\u001b[39m"
    )


def test_line_breaks_should_close_and_open_colors_with_crlf(chalk: ChalkFactory) -> None:
    assert r(chalk.grey("hello\r\nworld")) == r(
        "\u001b[90mhello\u001b[39m\r\n\u001b[90mworld\u001b[39m"
    )


def test_line_breaks_should_close_and_open_colors_multiple_occurrences(chalk: ChalkFactory) -> None:
    assert r(chalk.grey(" a \r\n b \n c \r\n d ")) == r(
        "\u001b[90m a \u001b[39m\r\n\u001b[90m b \u001b[39m\n\u001b[90m c \u001b[39m\r\n\u001b[90m d \u001b[39m"  # noqa
    )
