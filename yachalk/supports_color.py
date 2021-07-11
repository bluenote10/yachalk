"""
Inspired by:
https://github.com/chalk/supports-color/blob/main/index.js

With test cases:
https://github.com/chalk/supports-color/blob/main/test.js
"""

import os
import platform
import re
import sys


from typing import Optional, TextIO

from .types import ColorMode


def _get_env_force_color() -> Optional[ColorMode]:
    force_color = os.environ.get("FORCE_COLOR")

    if force_color is None:
        return None

    if force_color.lower() == "true" or len(force_color) == 0:
        return ColorMode.Basic16

    if force_color.lower() == "false":
        return ColorMode.AllOff

    try:
        level = int(force_color)
        return ColorMode(level)
    except ValueError:
        return None


def detect_color_support(stream: TextIO = sys.stdout) -> ColorMode:

    force_color = _get_env_force_color()

    is_tty = stream.isatty()

    # As a minor deviation from JS Chalk, we use the force color directly if given.
    # It feels like going into auto-detection mode even after a FORCE_COLOR value
    # is specified is not very intuitive (at least to me).
    if force_color is not None:
        return force_color

    elif not is_tty:
        return ColorMode.AllOff

    elif os.environ.get("TERM") == "dumb":
        return ColorMode.AllOff

    elif platform.system() == "Windows":
        # https://stackoverflow.com/a/66554956/1804173
        windows_version = platform.version().split(".")
        if len(windows_version) == 3:
            try:
                major = int(windows_version[0])
                build = int(windows_version[2])
                if major >= 10:
                    if build >= 14931:
                        return ColorMode.FullTrueColor
                    elif build >= 10586:
                        return ColorMode.Extended256
            except ValueError:
                pass

        return ColorMode.Basic16

    elif "CI" in os.environ:
        if (
            any(
                name in os.environ
                for name in [
                    "TRAVIS",
                    "CIRCLECI",
                    "APPVEYOR",
                    "GITLAB_CI",
                    "GITHUB_ACTIONS",
                    "BUILDKITE",
                    "DRONE",
                ]
            )
            or os.environ.get("CI_NAME") == "codeship"
        ):
            return ColorMode.Basic16
        else:
            return ColorMode.AllOff

    elif "TEAMCITY_VERSION" in os.environ:
        team_city_version = os.environ["TEAMCITY_VERSION"]
        m = re.search(r"^(9\.(0*[1-9]\d*)\.|\d{2,}\.)", team_city_version)
        if m is not None:
            return ColorMode.Basic16
        else:
            return ColorMode.AllOff

    elif os.environ.get("COLORTERM") == "truecolor":
        return ColorMode.FullTrueColor

    elif "TERM_PROGRAM" in os.environ:
        try:
            term_program_version_str = os.environ.get("TERM_PROGRAM_VERSION")
            if term_program_version_str is not None:
                term_program_version: Optional[int] = int(term_program_version_str.split(".")[0])
            else:
                term_program_version = None
        except ValueError:
            return ColorMode.Basic16
        term_program = os.environ.get("TERM_PROGRAM")
        if term_program == "iTerm.app":
            if term_program_version is not None:
                if term_program_version >= 3:
                    return ColorMode.FullTrueColor
                else:
                    return ColorMode.Extended256
            else:
                return ColorMode.Basic16
        elif term_program == "Apple_Terminal":
            return ColorMode.Extended256
        else:
            return ColorMode.Basic16

    elif "TERM" in os.environ and re.search(r"-256(color)?$", os.environ["TERM"]):
        return ColorMode.Extended256

    elif "TERM" in os.environ and re.search(
        r"^screen|^xterm|^vt100|^vt220|^rxvt|color|ansi|cygwin|linux", os.environ["TERM"]
    ):
        return ColorMode.Basic16

    elif "COLORTERM" in os.environ:
        return ColorMode.Basic16

    else:
        return ColorMode.AllOff
