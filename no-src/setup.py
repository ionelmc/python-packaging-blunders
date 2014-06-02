# -*- encoding: utf8 -*-
import glob
import io
import re
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ).read()

setup(
    name="nameless",
    version="0.1.0",
    license="BSD",
    description="An example package. Replace this with a proper project description. Generated with https://github.com/ionelmc/cookiecutter-pylibrary",
    long_description=read("README.rst"),
    author="Ionel Cristian Mărieș",
    author_email="contact@ionelmc.ro",
    url="https://github.com/ionelmc/python-nameless",
    packages=['package'],
    py_modules=['module'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Utilities",
    ],
    keywords=[
    ],
    install_requires=[
    ],
    extras_require={
    },
    entry_points={
        "console_scripts": [
            "test-module = module:main",
            "test-package = package:main",
        ]
    }

)