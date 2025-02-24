# geofetch: a Python library for fetching geo location data

| Release | Details |
| :-----: | :---: |
| Version | v1.0  |
| Date | 02/22/2025  |


## What is it?

**geofetch** is a lightweight Python package that fetches geolocation coordinates from 
Geocoding API from [Openweather](https://openweathermap.org/api/geocoding-api).

> [!NOTE]
> In version v1.0 the package only supports US locations.

## Table of Contents

- [Main Features](#main-features)
- [Dependencies](#dependencies)
- [PreRequisites](#prerequisites)
- [Assumptions and Limitations](#assumptions-and-limitations)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to run the CLI tool](#how-to-run-the-cli-tool)
- [How to run the tests](#how-to-run-the-tests)
- [How to import this package in other projects](#how-to-import-this-package-in-other-projects)

## Main Features
Here are just a few of the things that geofetch does well:

  - Takes the list of cities and zipcodes as input and returns their respective geographical coordinates (lat, lon).
  - Returns coordinates details of US locations.
  - Automatically handles `city,state` name or a zip code from the input and returns the coordinates using the appropriate API.

The source code is currently hosted on GitHub at:
https://github.com/saiushiv/geofetch

## Dependencies
Lists the dependencies required by the project.
- `pytest`: For running tests.
- `requests`: For making HTTP requests to the API.

## PreRequisites
Lists the prerequisites needed to run the project.
- Python 3.11 or higher.
- `pytest`: For running tests.
- `requests`: For making HTTP requests to the API.

## Assumptions and Limitations
Lists the assumptions and limitations of the project.
- The package currently only supports US locations.
- The input should be either a valid US zip code or a city and state combination in the format `city,state`.

## Project Structure
Provides an overview of the project's directory structure.

geofetch/ ├── src/ │ ├── cli.py │ ├── config/ │ │ └── api_config.py │ ├── handlers/ │ │ └── api_handler.py │ ├── utils/ │ │ ├── logger.py │ │ ├── request_util.py │ │ └── validate_util.py │ └── geofetch.py ├── tests/ │ ├── integration/ │ │ └── test_api_integration.py │ └── unit/ │ └── test_validate_util.py ├── README.md ├── setup.py └──

## Installation
Provides instructions on how to install the package and CLI tool.

In the `geofetch` directory (same one where you found this file after
cloning the git repo), execute:

```sh
pip install .
```

## How to run the CLI tool
Provides instructions on how to run the CLI tool.

In the geofetch directory (same one where you found this file after cloning the git repo), execute:

```sh
geofetch "New York, NY" "90210"
```

## How to run the tests
Provides instructions on how to run the tests.
In the geofetch directory (same one where you found this file after cloning the git repo), execute:

```sh
pytest
```

## How to import this package in other projects

Provides instructions on how to import and use the package in other projects.

You can import the GeoFetch class from the geofetch module in your project:

```py
from geofetch import GeoFetch

geo_fetch = GeoFetch()
results = geo_fetch.fetch_data(["10001", "Madison, WI"])
print(results)
```