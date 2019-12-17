# -*- coding:utf-8 -*-

r"""
Setup script for C API.
"""

from setuptools import setup, Extension

module = Extension(
    'hello',
    sources=['hello.c']
)

setup(ext_modules=[module])
