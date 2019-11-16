# -*- coding:utf-8 -*-

r"""
Setup script for PyPI.
"""

from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(
    filename=path.join(here, 'README.md'),
    encoding='utf-8',
) as desc:
    long_description = desc.read()

setup(
    name='htnhello',
    version='1.0.0',
    description='Hello World for PyPI.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kynthus/htnpython',
    author='Kynthus Aueoau',
    license='MIT',
    install_requires=['kafka'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'htnhello = htnhello.greet:hello',
        ],
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
