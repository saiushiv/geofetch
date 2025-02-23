from setuptools import setup, find_packages

setup(
    name="geofetch_cli_util",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'requests==2.32.3',
    ],
    entry_points={
        "console_scripts": [
            "geofetch=src.cli:main",  # This makes the CLI available as a command
        ],
    },
)