#!/usr/bin/env python3

from setuptools import setup, find_packages

"""
Setup script for the geofetch package.

This script uses setuptools to package the geofetch project, specifying its metadata,
dependencies, and entry points for the CLI tool.

Attributes:
    name (str): The name of the package.
    version (str): The version of the package.
    packages (list): A list of all Python import packages that should be included in the distribution package.
    install_requires (list): A list of dependencies required by the package.
    entry_points (dict): A dictionary specifying the entry points for the package, including the CLI command.
    author (str): The author of the package.
    description (str): A short description of the package.
    python_requires (str): The Python version requirement for the package.
"""

setup(
    name='geofetch_cli_util',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests==2.32.3',
    ],
    entry_points={
        'console_scripts': [
            # This makes the geofetch available as CLI command
            'geofetch=src.cli:main',  
        ],
    },
    author="Sai Upadhyay",
    description="A python package to fetch geographical coordinates",
    python_requires=">=3.11.0",
)