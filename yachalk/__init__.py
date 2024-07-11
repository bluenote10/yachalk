import platform
import os
from .chalk_instance import chalk, create_chalk
from .chalk_factory import ChalkFactory
from .types import ColorMode
from ._win import enable_virtual_terminal_processing

VERSION = "0.1.6"

if platform.system() == "Windows" and "DISABLE_VT_PROCESSING" not in os.environ:
    enable_virtual_terminal_processing()

__all__ = [
    "chalk",
    "create_chalk",
    "ChalkFactory",
    "ColorMode",
]
