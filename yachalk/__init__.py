from .chalk_factory import ChalkFactory
from .chalk_instance import chalk, create_chalk
from .types import ColorMode

VERSION = "0.1.8"

__all__ = [
    "chalk",
    "create_chalk",
    "ChalkFactory",
    "ColorMode",
]
