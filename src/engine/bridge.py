import ctypes
import os

# Load the shared library (Compile cpp first!)
# lib_path = os.path.join(os.path.dirname(__file__), "search_core.so")
# lib = ctypes.CDLL(lib_path)

def scan_directory(path: str, pattern: str):
    # lib.fast_scan.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
    # return lib.fast_scan(path.encode('utf-8'), pattern.encode('utf-8'))
    pass
