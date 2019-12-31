from setuptools import setup, Extension

module = Extension(
    name='_swiglist',
    sources=['swiglist.cpp', 'swiglist_wrap.cxx'],
)

setup(
    ext_modules=[module],
    py_modules=['swiglist'],
)
