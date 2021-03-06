#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-gmx',
    version='0.1.0',
    author='Ian Kenney',
    author_email='dfsdf',
    maintainer='Ian Kenney',
    maintainer_email='dfsdf',
    license='MIT',
    url='https://github.com/asfd/pytest-gmx',
    description='A simple plugin to use with Pytest',
    long_description=read('README.rst'),
    install_requires=['pytest>=3.0.0'],
    py_modules=['pytest_gmx'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'gmx = pytest_gmx',
        ],
    },
)
