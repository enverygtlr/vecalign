from setuptools import setup
from Cython.Build import cythonize
import numpy as np
import os

setup(
    ext_modules = cythonize(os.path.join(os.environ['VEC'], "dp_core.pyx")),
    include_dirs=[np.get_include()]
)