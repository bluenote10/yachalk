from .types import ColorMode
from .chalk_factory import ChalkFactory


def create_chalk() -> ChalkFactory:
    return ChalkFactory()


def set_color_mode(mode: ColorMode) -> None:
    global chalk
    chalk._mode = mode


chalk = create_chalk()
