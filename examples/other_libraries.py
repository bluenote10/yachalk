# type: ignore


def termcolor():
    from termcolor import colored

    print(colored(f"termcolor {colored('termcolor', 'blue')} termcolor", "red"))


def ansicolors():
    from colors import color

    print(color(f"ansicolors {color('ansicolors', 'blue')} ansicolors", "red"))


def blessings():
    from blessings import Terminal

    t = Terminal()

    print(t.bold_red_on_bright_green("It hurts my eyes!"))

    print(t.red(f"blessings {t.blue('blessings')} blessings"))


def rich():
    from rich import print

    print("[bold magenta]rich [green]ri\nch[/green] rich[/bold magenta]")


def style():
    import style

    print(style.red("style", style.blue("style") + " style"))


def simple_chalk():
    from simple_chalk import chalk

    # both of these are the same
    print(chalk.green("success"))
    # print(green("success"))

    print(chalk.italic.red("foo"))


# termcolor()
# ansicolors()
# blessings()
# rich()
style()
