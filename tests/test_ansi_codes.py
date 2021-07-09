from chalk.ansi_codes import rgb_to_ansi_256


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

    # 69, 173, 92 => 72
    # rgb(201, 101, 240) = 177
    # rgb(20, 40, 60) = 23
