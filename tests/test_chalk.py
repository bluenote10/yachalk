from typing import List, Set

from chalk import chalk
from chalk.chalk import Generator
from chalk.ansi_codes import Color, BgColor


def test_basic_colors() -> None:
    assert f"x {chalk.black('foo')} y" == "x \x1b[30mfoo\x1b[39m y"
    assert f"x {chalk.red('foo')} y" == "x \x1b[31mfoo\x1b[39m y"
    assert f"x {chalk.green('foo')} y" == "x \x1b[32mfoo\x1b[39m y"
    assert f"x {chalk.yellow('foo')} y" == "x \x1b[33mfoo\x1b[39m y"
    assert f"x {chalk.blue('foo')} y" == "x \x1b[34mfoo\x1b[39m y"
    assert f"x {chalk.magenta('foo')} y" == "x \x1b[35mfoo\x1b[39m y"
    assert f"x {chalk.cyan('foo')} y" == "x \x1b[36mfoo\x1b[39m y"
    assert f"x {chalk.white('foo')} y" == "x \x1b[37mfoo\x1b[39m y"


def test_manual_styling() -> None:
    assert chalk.style(Color.black)("foo") == "\x1b[30mfoo\x1b[39m"
    assert (
        chalk.style(Color.black).style(BgColor.white)("foo")
        == "\x1b[30m\x1b[47mfoo\x1b[39m\x1b[49m"
    )


def r(s: str) -> str:
    """
    Pytest string handling is quite inappropriate for the task.
    """
    print(s.__repr__())
    return s.__repr__()


def test_support_nesting_styles_of_same_type() -> None:
    assert r(
        chalk.red(" a " + chalk.yellow(" b " + chalk.green(" c ") + " b ") + " a ")
    ) == r(
        "\x1b[31m a \x1b[33m b \x1b[32m c \x1b[39m\x1b[31m\x1b[33m b \x1b[39m\x1b[31m a \x1b[39m"
    )


def test_interface_consistency() -> None:
    def filter_names(names: List[str]) -> Set[str]:
        return set(name for name in names if not name.startswith("__"))

    funcs_factory = filter_names(dir(chalk))
    funcs_generator = filter_names(dir(Generator([])))

    funcs_generator = funcs_generator - {"create_from_ansi_16_code", "_codes"}

    print(funcs_factory)
    print(funcs_generator)

    assert funcs_factory == funcs_generator
