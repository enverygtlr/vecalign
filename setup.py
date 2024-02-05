from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules = cythonize("dp_core.pyx"),
    include_dirs=[np.get_include()]
)