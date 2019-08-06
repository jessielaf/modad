# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

try:
    from m2r import parse_from_file

    long_description = parse_from_file("README.md")
except ImportError as e:
    long_description = ""

here = path.abspath(path.dirname(__file__))

setup(
    name="modad",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # http://packaging.python.org/en/latest/tutorial.html#version
    version="0.1",
    description="Modad: The monolith ass- and dissembler",
    long_description=long_description,
    # The project's main homepage.
    url="https://github.com/jessielaf/modad",
    # Author details
    author="Jessie Liauw A Fong",
    author_email="jessielaff@live.nl",
    # Choose your license
    license="MIT",
    # See https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: System :: Installation/Setup",
        "Topic :: Utilities",
    ],
    scripts=["modad/cli.py"],
    entry_points={"console_scripts": ["modad = modad.cli:main"]},
    # What does your project relate to?
    keywords="",
    packages=find_packages(),
    install_requires=[
        "pyyaml==5.1",
        "gitpython==2.1",
        "dataclasses==0.6.0",
        "click==7.0",
    ],
    # extras_require={"docs": required_build},
    include_package_data=True,
)
