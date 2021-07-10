from typing import List, Set

from chalk import chalk
from chalk.chalk import Generator, ColorMode
from chalk.ansi_codes import Color, BgColor


def r(s: str) -> str:
    """
    Pytest string handling is quite inappropriate for the task.
    """
    print(s.__repr__())
    return s.__repr__()


def test_interface_consistency() -> None:
    def filter_names(names: List[str]) -> Set[str]:
        return set(name for name in names if not name.startswith("__"))

    funcs_factory = filter_names(dir(chalk))
    funcs_generator = filter_names(dir(Generator(mode=ColorMode.FullTrueColor, codes=[])))

    funcs_factory -= {"_create_generator_from_ansi_16_code"}
    funcs_generator -= {"_codes"}

    print(funcs_factory)
    print(funcs_generator)

    assert funcs_factory == funcs_generator


def test_basics() -> None:
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
    def gen() -> Generator:
        return Generator(ColorMode.FullTrueColor, [])

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


def test_manual_styling() -> None:
    assert chalk.style(Color.black)("foo") == "\x1b[30mfoo\x1b[39m"
    assert (
        chalk.style(Color.black).style(BgColor.white)("foo")
        == "\x1b[30m\x1b[47mfoo\x1b[39m\x1b[49m"
    )


def test_type_support() -> None:
    class Custom:
        def __str__(self) -> str:
            return "custom"

    assert r(chalk.black(42)) == r("\x1b[30m42\x1b[39m")
    assert r(chalk.black(1.0)) == r("\x1b[30m1.0\x1b[39m")
    assert r(chalk.black(True)) == r("\x1b[30mTrue\x1b[39m")
    assert r(chalk.black(Custom())) == r("\x1b[30mcustom\x1b[39m")


def test_vararg_support() -> None:
    assert r(chalk.black("a", "b", "c")) == r("\x1b[30ma b c\x1b[39m")
    assert r(chalk.black("a", "b", "c", sep="")) == r("\x1b[30mabc\x1b[39m")
    assert r(chalk.black(1, 2, 3)) == r("\x1b[30m1 2 3\x1b[39m")
    assert r(chalk.black(1, 2, 3, sep=", ")) == r("\x1b[30m1, 2, 3\x1b[39m")


# -----------------------------------------------------------------------------
# Test cases from Chalk
# -----------------------------------------------------------------------------


def test_support_nesting_styles_of_same_type() -> None:
    assert r(chalk.red(" a " + chalk.yellow(" b " + chalk.green(" c ") + " b ") + " a ")) == r(
        "\x1b[31m a \x1b[33m b \x1b[32m c \x1b[39m\x1b[31m\x1b[33m b \x1b[39m\x1b[31m a \x1b[39m"
    )


def test_line_breaks_should_close_and_open_colors() -> None:
    assert r(chalk.grey("hello\nworld")) == r(
        "\u001B[90mhello\u001B[39m\n\u001B[90mworld\u001B[39m"
    )


def test_line_breaks_should_close_and_open_colors_with_crlf() -> None:
    assert r(chalk.grey("hello\r\nworld")) == r(
        "\u001B[90mhello\u001B[39m\r\n\u001B[90mworld\u001B[39m"
    )


def test_line_breaks_should_close_and_open_colors_multiple_occurrences() -> None:
    assert r(chalk.grey(" a \r\n b \n c \r\n d ")) == r(
        "\u001B[90m a \u001B[39m\r\n\u001B[90m b \u001B[39m\n\u001B[90m c \u001B[39m\r\n\u001B[90m d \u001B[39m"  # noqa
    )
