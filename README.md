# mpc_obscodes: Minor Planet Center Observatory Codes File
#### A Python package by the Asteroid Institute, a program of the B612 Foundation

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://img.shields.io/badge/Python-3.7%2B-blue)
[![PyPI version](https://img.shields.io/pypi/v/mpc-obscodes)](https://img.shields.io/pypi/v/mpc-obscodes)
[![PyPi downloads](https://img.shields.io/pypi/dm/mpc-obscodes)](https://img.shields.io/pypi/dm/mpc-obscodes)  
[![Build and Test](https://github.com/B612-Asteroid-Institute/mpc_obscodes/actions/workflows/build_test.yml/badge.svg)](https://github.com/B612-Asteroid-Institute/mpc_obscodes/actions/workflows/build_test.yml)
[![Build, Test, & Publish](https://github.com/B612-Asteroid-Institute/mpc_obscodes/actions/workflows/build_test_publish.yml/badge.svg)](https://github.com/B612-Asteroid-Institute/mpc_obscodes/actions/workflows/build_test_publish.yml)
[![Compare Upstream](https://github.com/B612-Asteroid-Institute/mpc_obscodes/actions/workflows/compare_upstream.yml/badge.svg)](https://github.com/B612-Asteroid-Institute/mpc_obscodes/actions/workflows/compare_upstream.yml)  

This package ships the Minor Planet Center's [file](https://minorplanetcenter.net/Extended_Files/obscodes_extended.json.gz) of observatory codes and their geodetic coordinates.

**This is not an official MPC package**. It is an automatically generated mirror of the file so that it is
installable via `pip`.

Every night at around 2:15 AM UTC, the MPC observatory code file is downloaded and compared (via md5 checksum) to the current version of this package. If the checksums are different, a new package will be published.

## Installation

The latest version of the file can be install via pip:  
`pip install mpc-obscodes`

## Usage
```python
import pandas as pd
from mpc_obscodes import mpc_obscodes

obscodes = pd.read_json(mpc_obscodes, orient="index")
```

## Acknowledgment

This research has made use of data and/or services provided by the International Astronomical Union's Minor Planet Center.

See the Minor Planet Center's [website](https://cgi.minorplanetcenter.net/) for more details.
