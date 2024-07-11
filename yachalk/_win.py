"""
Adds ANSI Escape Sequence support for windows `conhost.exe` more commonly known
as `CMD`.

adds windows ANSI Escape Sequence to more newer `conhost.exe` for windows 10
build 16257 and later with the added capabilities.
"""
import sys
import ctypes

STDOUT_HANDLE = -11
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x004

def enable_virtual_terminal_processing() -> None:
    kernel32 = ctypes.WinDLL('kernel32')
    output_handle = kernel32.GetStdHandle(STDOUT_HANDLE)
    console_mode = ctypes.c_ulong(0)
    kernel32.GetConsoleMode(output_handle, ctypes.byref(console_mode))
    console_mode.value |= ENABLE_VIRTUAL_TERMINAL_PROCESSING
    kernel32.SetConsoleMode(output_handle, console_mode)
