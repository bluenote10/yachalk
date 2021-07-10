import pytest

from yachalk.utils import hex_to_rgb, get_code_from_rgb

from yachalk.types import ColorMode

from helper import r


def test_hex_to_rgb() -> None:
    assert hex_to_rgb("000") == (0, 0, 0)
    assert hex_to_rgb("fff") == (255, 255, 255)

    assert hex_to_rgb("102030") == (16, 32, 48)
    assert hex_to_rgb("abcdef") == (171, 205, 239)

    with pytest.raises(ValueError, match="is not a valid hex literal"):
        hex_to_rgb("12345")

    with pytest.raises(ValueError, match="is not a valid hex literal"):
        hex_to_rgb("1234567")

    with pytest.raises(ValueError, match="is not a valid hex literal"):
        hex_to_rgb("xyxyxy")


def test_get_code_from_rgb() -> None:
    assert get_code_from_rgb(20, 40, 60, ColorMode.NoColors, background=False) is None
    assert get_code_from_rgb(20, 40, 60, ColorMode.NoColors, background=True) is None

    code = get_code_from_rgb(20, 40, 60, ColorMode.Basic16, background=False)
    assert code is not None
    assert r(code.on) == r("\x1b[30m")
    assert r(code.off) == r("\x1b[39m")
    code = get_code_from_rgb(20, 40, 60, ColorMode.Basic16, background=True)
    assert code is not None
    assert r(code.on) == r("\x1b[40m")
    assert r(code.off) == r("\x1b[49m")

    code = get_code_from_rgb(20, 40, 60, ColorMode.Extended256, background=False)
    assert code is not None
    assert r(code.on) == r("\x1b[38;5;23m")
    assert r(code.off) == r("\x1b[39m")
    code = get_code_from_rgb(20, 40, 60, ColorMode.Extended256, background=True)
    assert code is not None
    assert r(code.on) == r("\x1b[48;5;23m")
    assert r(code.off) == r("\x1b[49m")

    code = get_code_from_rgb(20, 40, 60, ColorMode.FullTrueColor, background=False)
    assert code is not None
    assert r(code.on) == r("\x1b[38;2;20;40;60m")
    assert r(code.off) == r("\x1b[39m")
    code = get_code_from_rgb(20, 40, 60, ColorMode.FullTrueColor, background=True)
    assert code is not None
    assert r(code.on) == r("\x1b[48;2;20;40;60m")
    assert r(code.off) == r("\x1b[49m")
