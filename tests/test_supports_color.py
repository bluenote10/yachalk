import os
import sys

from unittest import mock

from yachalk.supports_color import _get_env_force_color, detect_color_support

from yachalk.types import ColorMode


@mock.patch.dict(os.environ, {}, clear=True)
def test_env_force_color__missing() -> None:
    assert _get_env_force_color() is None


@mock.patch.dict(os.environ, {"FORCE_COLOR": "illegal"}, clear=True)
def test_env_force_color__illegal_string() -> None:
    assert _get_env_force_color() is None


@mock.patch.dict(os.environ, {"FORCE_COLOR": ""}, clear=True)
def test_env_force_color__empty_string() -> None:
    assert _get_env_force_color() == ColorMode.Basic16


@mock.patch.dict(os.environ, {"FORCE_COLOR": "true"}, clear=True)
def test_env_force_color__true() -> None:
    assert _get_env_force_color() == ColorMode.Basic16


@mock.patch.dict(os.environ, {"FORCE_COLOR": "TRUE"}, clear=True)
def test_env_force_color__true_not_lower_case() -> None:
    assert _get_env_force_color() == ColorMode.Basic16


@mock.patch.dict(os.environ, {"FORCE_COLOR": "false"}, clear=True)
def test_env_force_color__false() -> None:
    assert _get_env_force_color() == ColorMode.NoColors


@mock.patch.dict(os.environ, {"FORCE_COLOR": "FALSE"}, clear=True)
def test_env_force_color__false_not_lower_case() -> None:
    assert _get_env_force_color() == ColorMode.NoColors


@mock.patch.dict(os.environ, {"FORCE_COLOR": "0"}, clear=True)
def test_env_force_color__0() -> None:
    assert _get_env_force_color() == ColorMode.NoColors


@mock.patch.dict(os.environ, {"FORCE_COLOR": "1"}, clear=True)
def test_env_force_color__1() -> None:
    assert _get_env_force_color() == ColorMode.Basic16


@mock.patch.dict(os.environ, {"FORCE_COLOR": "2"}, clear=True)
def test_env_force_color__2() -> None:
    assert _get_env_force_color() == ColorMode.Extended256


@mock.patch.dict(os.environ, {"FORCE_COLOR": "3"}, clear=True)
def test_env_force_color__3() -> None:
    assert _get_env_force_color() == ColorMode.FullTrueColor


@mock.patch.dict(os.environ, {"FORCE_COLOR": "0"}, clear=True)
def test_detect_color_support__respects_force_color_0() -> None:
    assert detect_color_support() == ColorMode.NoColors


@mock.patch.dict(os.environ, {"FORCE_COLOR": "1"}, clear=True)
def test_detect_color_support__respects_force_color_1() -> None:
    assert detect_color_support() == ColorMode.Basic16


@mock.patch.dict(os.environ, {"FORCE_COLOR": "2"}, clear=True)
def test_detect_color_support__respects_force_color_2() -> None:
    assert detect_color_support() == ColorMode.Extended256


@mock.patch.dict(os.environ, {"FORCE_COLOR": "3"}, clear=True)
def test_detect_color_support__respects_force_color_3() -> None:
    assert detect_color_support() == ColorMode.FullTrueColor


@mock.patch.dict(os.environ, {"COLORTERM": "truecolor"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: False)
def test_detect_color_support__returns_no_color_suppot_for_non_tty() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.NoColors


@mock.patch.dict(os.environ, {"TERM": "dumb"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__dumb_terminal() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.NoColors


@mock.patch.dict(os.environ, {}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
@mock.patch("platform.system", lambda: "Windows")
@mock.patch("platform.version", lambda: "brokenversion")
def test_detect_color_support__windows_broken_version_1() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
@mock.patch("platform.system", lambda: "Windows")
@mock.patch("platform.version", lambda: "broken.but.with-two-dots")
def test_detect_color_support__windows_broken_version_2() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
@mock.patch("platform.system", lambda: "Windows")
@mock.patch("platform.version", lambda: "10.0.10586")
def test_detect_color_support__windows_min_build_for_256_colors() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Extended256


@mock.patch.dict(os.environ, {}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
@mock.patch("platform.system", lambda: "Windows")
@mock.patch("platform.version", lambda: "10.0.14931")
def test_detect_color_support__windows_min_build_for_true_colors() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.FullTrueColor


@mock.patch.dict(os.environ, {"CI": "true"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__ci_env_unknown() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.NoColors


@mock.patch.dict(os.environ, {"CI": "true", "TRAVIS": "true"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__ci_env_known() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {"TEAMCITY_VERSION": "9.0.5 (build 32523)"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__team_city_below_9_1() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.NoColors


@mock.patch.dict(os.environ, {"TEAMCITY_VERSION": "9.1.0 (build 32523)"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__team_city_above_9_1() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {"COLORTERM": "truecolor"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__colorterm_truecolor() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.FullTrueColor


@mock.patch.dict(
    os.environ, {"TERM_PROGRAM": "iTerm.app", "TERM_PROGRAM_VERSION": "2.9.3"}, clear=True
)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__iterm_below_3() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Extended256


@mock.patch.dict(
    os.environ, {"TERM_PROGRAM": "iTerm.app", "TERM_PROGRAM_VERSION": "3.0.10"}, clear=True
)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__iterm_above_3() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.FullTrueColor


@mock.patch.dict(
    os.environ, {"TERM_PROGRAM": "iTerm.app", "TERM_PROGRAM_VERSION": "broken"}, clear=True
)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__iterm_broken_version() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {"TERM_PROGRAM": "iTerm.app"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__iterm_unknown_version() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {"TERM_PROGRAM": "Apple_Terminal"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__apple_terminal() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Extended256


@mock.patch.dict(os.environ, {"TERM_PROGRAM": "unknown"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__unknown_term_program() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {"TERM": "xterm-256color"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__term_256() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Extended256


@mock.patch.dict(os.environ, {"TERM": "xterm"}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__term_basic() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {"COLORTERM": ""}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__colorterm() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.Basic16


@mock.patch.dict(os.environ, {}, clear=True)
@mock.patch("sys.stdout.isatty", lambda: True)
def test_detect_color_support__fall_back_to_no_colors_without_any_indicators() -> None:
    assert detect_color_support(sys.stdout) == ColorMode.NoColors
