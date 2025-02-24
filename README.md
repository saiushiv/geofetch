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
- [Prerequisites](#prerequisites)
- [Assumptions and Limitations](#assumptions-and-limitations)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [How to run the CLI tool](#how-to-run-the-cli-tool)
- [Tool usage examples](#tool-usage-examples)
- [How to run the tests](#how-to-run-the-tests)
- [How to import this package in other projects](#how-to-import-this-package-in-other-projects)
- [To uninstall the CLI tool](#to-uninstall-the-cli-tool)

## Main Features
Here are just a few of the things that geofetch does well:

  - Takes the list of cities and zipcodes as input and returns their respective geographical coordinates (lat, lon).
  - Returns coordinates details of US locations.
  - Automatically handles `city,state` name or a zip code from the input and returns the coordinates using the appropriate API.

The source code is currently hosted on GitHub at:
https://github.com/saiushiv/geofetch

## Dependencies

- `pytest`: For running tests.
- `requests`: For making HTTP requests to the API.

## Prerequisites

- `Python` v3.11.0 or higher.
- `pytest`: For running tests.
- `requests`: For making HTTP requests to the API.
- **API Key**: You must set the `GEOFETCH_API_KEY` environment variable with your API key from OpenWeather(or from the Take-Home assessment test document) in your local machine/environment.
  API key can be set as :
```sh
$>  export GEOFETCH_API_KEY=<YOUR API KEY HERE>
```

## Assumptions and Limitations

- The package currently only supports US locations.
- The input should be either a valid US zip code or a city and state combination(without spaces) in the format `city,state`.

## Project Structure

```
geofetch/ 
├── src/ 
│ ├── cli.py                        # CLI entry point for the geofetch CLI tool
│ ├── config/ 
│ │ └── api_config.py               # Configuration for the Geo API
│ ├── handlers/ 
│ │ └── api_handler.py              # Handler for interacting with the Geo API
│ ├── utils/ 
│ │ ├── logger.py                   # Logging configuration
│ │ ├── request_util.py             # Utility for making API requests
│ │ └── validate_util.py            # Utility for validating input
│ └── geofetch.py                   # Core functionality for fetching geo data
├── tests/ 
│ ├── integration/ 
│ │ └── test_api_integration.py     # Integration tests for the API
│ 
├── README.md                       # Project documentation
├── setup.py                        # Setup script for installing the package
└── requirements.txt                # List of devlopment dependencies
```

## Installation
If you don't have `pytest` installed on your machine then run this command to install the dependency:

```sh
$>  pip install -r requirements.txt
```

Rest other dependencies such as `requests` package will be installed during the setup of the CLI tool using the step shown below.

To install the `geofetch` package as a CLI command tool, in the `geofetch` directory (same one where you found this file after
cloning the git repo), execute:

```sh
$>  pip install .
```

## How to run the CLI tool

In the geofetch directory (same one where you found this file after cloning the git repo), execute:

```sh
$>   geofetch "New York, NY" "90210"
```

## Tool usage examples

1. with zip code

```sh
$>   geofetch "90210"
```

```
Response:

2025-02-23 21:40:48,538 - INFO - Response for '90210': {'zip': '90210', 'name': 'Beverly Hills', 'lat': 34.0901, 'lon': -118.4065, 'country': 'US'}
```

2. with city,state code

```sh
$>   geofetch Madison,WI
```

```
Response:

2025-02-23 21:48:24,377 - INFO - Response for 'Madison,WI': [{'name': 'Madison', 'local_names': {'zh': '麦迪逊', 'ta': 'மேடிசன்', 'sr': 'Медисон', 'pl': 'Madison', 'ru': 'Мадисон', 'en': 'Madison', 'uk': 'Медісон'}, 'lat': 43.074761, 'lon': -89.3837613, 'country': 'US', 'state': 'Wisconsin'}]
```

3. with multiple locations of either city/state or zip location type at once.

```sh
$>   geofetch Madison,WI 12345 Chicago,IL 10001
```

```
Response:

2025-02-23 21:50:35,864 - INFO - Response for 'Madison,WI': [{'name': 'Madison', 'local_names': {'ta': 'மேடிசன்', 'sr': 'Медисон', 'pl': 'Madison', 'ru': 'Мадисон', 'en': 'Madison', 'uk': 'Медісон', 'zh': '麦迪逊'}, 'lat': 43.074761, 'lon': -89.3837613, 'country': 'US', 'state': 'Wisconsin'}]

2025-02-23 21:50:35,865 - INFO - Response for '12345': {'zip': '12345', 'name': 'Schenectady', 'lat': 42.8142, 'lon': -73.9396, 'country': 'US'}

2025-02-23 21:50:35,866 - INFO - Response for 'Chicago,IL': [{'name': 'Chicago', 'local_names': {'ca': 'Chicago', 'hr': 'Chicago', 'el': 'Σικάγο', 'kw': 'Chicago', 'ky': 'Чикаго', 'mk': 'Чикаго', 'nl': 'Chicago', 'is': 'Chicago', 'oc': 'Chicago', 'mg': 'Chicago', 'br': 'Chicago', 'bm': 'Chicago', 'ht': 'Chikago', 'zu': 'Chicago', 'se': 'Chicago', 'ce': 'Чикаго', 'eu': 'Chicago', 'fa': 'شیکاگو', 'sw': 'Chicago', 'fo': 'Chicago', 'kk': 'Чикаго', 'ku': 'Chicago', 'no': 'Chicago', 'bh': 'शिकागो', 'gv': 'Chicago', 'an': 'Chicago', 'th': 'ชิคาโก', 'zh': '芝加哥', 'kl': 'Chicago', 'hi': 'शिकागो', 'ig': 'Chicago', 'cs': 'Chicago', 'sh': 'Chicago', 'sq': 'Çikago', 'es': 'Chicago', 'ug': 'Chikago', 'pa': 'ਸ਼ਿਕਾਗੋ', 'be': 'Чыкага', 'sg': 'Chicago', 'mn': 'Чикаго', 'pt': 'Chicago', 'mr': 'शिकागो', 'st': 'Chicago', 'la': 'Sicagum', 'mi': 'Chicago', 'eo': 'Ĉikago', 'kn': 'ಶಿಕಾಗೊ', 'fy': 'Chicago', 'vo': 'Chicago', 'af': 'Chicago', 'bn': 'শিকাগো', 'gl': 'Chicago', 'io': 'Chicago', 'ha': 'Chicago', 'ml': 'ഷിക്കാഗോ', 'ru': 'Чикаго', 'qu': 'Chicago', 'bg': 'Чикаго', 'yi': 'שיקאגא', 'bi': 'Chicago', 'so': 'Chicago', 'am': 'ሺካጎ', 'sk': 'Chicago', 'bs': 'Chicago', 'de': 'Chicago', 'ga': 'Chicago', 'sl': 'Chicago', 'id': 'Chicago', 'ka': 'ჩიკაგო', 'my': 'ရှီကာဂိုမြို့', 'ta': 'சிகாகோ', 'nn': 'Chicago', 'fr': 'Chicago', 'tk': 'Chicago', 'en': 'Chicago', 'lt': 'Čikaga', 'iu': 'ᓰᖄᑯ', 'ki': 'Chicago', 'te': 'చికాగో', 'tt': 'Çikago', 'fj': 'Chicago', 'tl': 'Chicago', 'et': 'Chicago', 'ms': 'Chicago', 'ar': 'شيكاغو', 'sn': 'Chicago', 'co': 'Chicago', 'pl': 'Chicago', 'fi': 'Chicago', 'it': 'Chicago', 'rn': 'Chicago', 'ak': 'Chicago', 'nv': 'Shikááʼgóó', 'uz': 'Chicago', 'gd': 'Chicago', 'li': 'Chicago', 'sc': 'Chicago', 'ne': 'शिकागो', 'ps': 'شیکاګو', 'ro': 'Chicago', 'cy': 'Chicago', 'ur': 'شکاگو، الینوائے', 'hu': 'Chicago', 'ko': '시카고', 'az': 'Çikaqo', 'hy': 'Չիկագո', 'ie': 'Chicago', 'xh': 'E-Chicago', 'na': 'Chicago', 'sv': 'Chicago', 'vi': 'Chicago', 'os': 'Чикаго', 'yo': 'Ṣìkágò', 'he': 'שיקגו', 'rm': 'Chicago', 'sr': 'Чикаго', 'wa': 'Tchicago', 'tw': 'Kyekago', 'lb': 'Chicago', 'ia': 'Chicago', 'tr': 'Şikago', 'jv': 'Chicago', 'uk': 'Чикаго', 'da': 'Chicago', 'tg': 'Чикаго', 'lv': 'Čikāga', 'ja': 'シカゴ', 'gn': 'Chikago'}, 'lat': 41.8755616, 'lon': -87.6244212, 'country': 'US', 'state': 'Illinois'}]

2025-02-23 21:50:35,866 - INFO - Response for '10001': {'zip': '10001', 'name': 'New York', 'lat': 40.7484, 'lon': -73.9967, 'country': 'US'}
```


## How to run the tests

In the geofetch directory (same one where you found this file after cloning the git repo), execute:

```sh
$>   pytest
```

## How to import this package in other projects

You can import the GeoFetch class from the geofetch module in your project. 
Like create a a new file in the geofetch directory (same one where you found this file after cloning the git repo), execute:

```py
from src.geofetch import GeoFetch

geo_fetch = GeoFetch()
results = geo_fetch.fetch_data(["10001", "Madison, WI"])
print(results)
```

## To uninstall the CLI tool

In the geofetch directory (same one where you found this file after cloning the git repo), execute:

```sh
$>   pip uninstall geofetch_cli_util
```
