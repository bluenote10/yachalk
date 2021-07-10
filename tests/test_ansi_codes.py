import pytest

from chalk.ansi_codes import rgb_to_ansi_256, ansi_256_to_ansi_16, hex_to_rgb


def test_rgb_to_ansi_256() -> None:
    assert rgb_to_ansi_256(0, 0, 0) == 16

    assert rgb_to_ansi_256(255, 0, 0) == 196
    assert rgb_to_ansi_256(0, 255, 0) == 46
    assert rgb_to_ansi_256(0, 0, 255) == 21

    assert rgb_to_ansi_256(255, 255, 0) == 226
    assert rgb_to_ansi_256(255, 0, 255) == 201
    assert rgb_to_ansi_256(0, 255, 255) == 51

    assert rgb_to_ansi_256(255, 255, 255) == 231

    assert rgb_to_ansi_256(7, 7, 7) == 16
    assert rgb_to_ansi_256(8, 8, 8) == 232
    assert rgb_to_ansi_256(127, 127, 127) == 244
    assert rgb_to_ansi_256(191, 191, 191) == 250
    assert rgb_to_ansi_256(248, 248, 248) == 255
    assert rgb_to_ansi_256(249, 249, 249) == 231

    assert rgb_to_ansi_256(69, 173, 92) == 72
    assert rgb_to_ansi_256(201, 101, 240) == 177
    assert rgb_to_ansi_256(20, 40, 60) == 23


def test_ansi_256_to_ansi_16() -> None:
    expected_values_groups = [
        [30, 31, 32, 33, 34, 35, 36, 37, 90, 91, 92, 93, 94, 95, 96, 97],
        [30, 30, 30, 34, 34, 94, 30, 30, 30, 34, 34, 94, 30, 30, 30, 34],
        [34, 94, 32, 32, 32, 36, 36, 96, 32, 32, 32, 36, 36, 96, 92, 92],
        [92, 96, 96, 96, 30, 30, 30, 34, 34, 94, 30, 30, 30, 34, 34, 94],
        [30, 30, 30, 34, 34, 94, 32, 32, 32, 36, 36, 96, 32, 32, 32, 36],
        [36, 96, 92, 92, 92, 96, 96, 96, 30, 30, 30, 34, 34, 94, 30, 30],
        [30, 34, 34, 94, 30, 30, 30, 34, 34, 94, 32, 32, 32, 36, 36, 96],
        [32, 32, 32, 36, 36, 96, 92, 92, 92, 96, 96, 96, 31, 31, 31, 35],
        [35, 95, 31, 31, 31, 35, 35, 95, 31, 31, 31, 35, 35, 95, 33, 33],
        [33, 37, 37, 97, 33, 33, 33, 37, 37, 97, 93, 93, 93, 97, 97, 97],
        [31, 31, 31, 35, 35, 95, 31, 31, 31, 35, 35, 95, 31, 31, 31, 35],
        [35, 95, 33, 33, 33, 37, 37, 97, 33, 33, 33, 37, 37, 97, 93, 93],
        [93, 97, 97, 97, 91, 91, 91, 95, 95, 95, 91, 91, 91, 95, 95, 95],
        [91, 91, 91, 95, 95, 95, 93, 93, 93, 97, 97, 97, 93, 93, 93, 97],
        [97, 97, 93, 93, 93, 97, 97, 97, 30, 30, 30, 30, 30, 30, 30, 30],
        [30, 30, 30, 30, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37, 37],
    ]

    i = 0
    for expected_values in expected_values_groups:
        for expected_value in expected_values:
            print(i, expected_value)
            assert ansi_256_to_ansi_16(i) == expected_value
            i += 1

    assert i == 256


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
