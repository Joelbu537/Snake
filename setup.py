from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("snake.py", language_level="3"),
)
