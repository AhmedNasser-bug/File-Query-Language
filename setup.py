import os
# FORCE the path inside Python so it can't miss it
os.environ["PATH"] = r"C:\msys64\mingw64\bin;" + os.environ["PATH"]
import sys
from setuptools import setup, Extension

# --- CONFIGURATION FOR MINGW (GCC) ---
# We force GCC flags because you are using MinGW64
extra_compile_args = ["-std=c++17", "-O3"]
extra_link_args = []

# If you are strictly on Windows with MinGW, -fPIC is usually not needed/ignored,
# but it doesn't hurt to leave it out or include it.
# We will stick to the basics.

module = Extension(
    name="src.engine.search_core",
    sources=["src/engine/search_core.cpp"],
    include_dirs=["src/engine"],
    language="c++",
    extra_compile_args=extra_compile_args,
    extra_link_args=extra_link_args,
)

setup(
    name="fql_core",
    version="0.1",
    description="FQL Engine",
    ext_modules=[module],
)