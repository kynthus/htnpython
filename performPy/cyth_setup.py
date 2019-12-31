from setuptools import setup, Extension
from Cython.Build import cythonize

module = Extension(
    name='cythonlist',
    sources=['cyth_main.pyx'],
    library_dirs=['/usr/local/lib'],
    libraries=['boost_python36'],
)

setup(ext_modules=cythonize([module]))
