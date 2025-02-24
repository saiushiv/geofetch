#!/usr/bin/env python3

from setuptools import setup, find_packages

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