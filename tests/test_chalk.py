from chalk import chalk


def test_basic_colors() -> None:
    assert f"x {chalk.black('foo')} y" == "x \x1b[30mfoo\x1b[39m y"
    assert f"x {chalk.red('foo')} y" == "x \x1b[31mfoo\x1b[39m y"
    assert f"x {chalk.green('foo')} y" == "x \x1b[32mfoo\x1b[39m y"
    assert f"x {chalk.yellow('foo')} y" == "x \x1b[33mfoo\x1b[39m y"
    assert f"x {chalk.blue('foo')} y" == "x \x1b[34mfoo\x1b[39m y"
    assert f"x {chalk.magenta('foo')} y" == "x \x1b[35mfoo\x1b[39m y"
    assert f"x {chalk.cyan('foo')} y" == "x \x1b[36mfoo\x1b[39m y"
    assert f"x {chalk.white('foo')} y" == "x \x1b[37mfoo\x1b[39m y"


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
