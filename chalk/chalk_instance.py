import sys

from .chalk_factory import ChalkFactory
from .supports_color import detect_color_support


def create_chalk() -> ChalkFactory:
    mode = detect_color_support(sys.stdout)
    return ChalkFactory(mode)


chalk = create_chalk()
