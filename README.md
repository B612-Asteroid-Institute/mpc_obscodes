# Minor Planet Center Observatory Codes

This package ships the Minor Planet Center's [file](https://minorplanetcenter.net/Extended_Files/obscodes_extended.json.gz) of observatory codes and their geodetic coordinates.

This is not an official MPC package. It is an automatically generated mirror of the file so that it is 
installable via `pip`.

Every night at 1 AM UTC, the MPC observatory code file is downloaded and compared (via md5 checksum) to the current version of this package. If the checksums are different, a new package will be published. 

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