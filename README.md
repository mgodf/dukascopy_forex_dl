[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<p align="center">
  <a href="https://github.com/mgodf/dukascopy_forex_dl">
  </a>

  <h3 align="center">(Unofficial) Dukascopy Forex Downloader</h3>

  <p align="center">
    Unofficial Forex Data Downloader for Dukascopy API!
    <br />
    <a href="https://github.com/mgodf/dukascopy_forex_dl"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/mgodf/dukascopy_forex_dl">View Demo</a>
    ·
    <a href="https://github.com/mgodf/dukascopy_forex_dl">Report Bug</a>
    ·
    <a href="https://github.com/mgodf/dukascopy_forex_dl">Request Feature</a>
  </p>

## Getting Started
Files:
- main.py
- bi5-csv.py

### Prerequisites

- Python 3
- Do a 'pip install' for any packages that you might be missing

### Installation

Just download and run!

## Usage

### main.py
Downloads a range of .bi5 files from Dukascopy

#### Step 1.) Configure
To configure, open main.py and set the `ctx` variables at the top of the file as follows:
- **cache_loc**: Location where files will be downloaded
- **session_sym**: Symbol to download (e.g. 'EURUSD')
- **session_start_date**: Date to begin downloading from (e.g. fo**r** January 1st 2019: "2019-01-01")
- **session_start_hour**: Hour to begin downloading (0-23)
- **session_duration_hrs**: Number of hours worth of data to download (e.g. for 1 week: 24*7)

#### Step 2.) Run
```py
python .\main.py
```

### bi5-csv.py
Converts (.bi5) files to (.csv) format. --in_file can be a single file or a while directory 
```py
python .\bi5-csv.py [-h] --in_file IN_FILE [--out_file OUT_FILE]
```
*hint:* After running `main.py`, set `--in_file` to the same directory as the `cache_loc` variable from above.

e.g.)

If `main.py` was configured as:
```py
ctx['cache_loc'] = r'C:/Users/<user_name>/FXCACHE/'
```
 you would run:
```sh
python .\bi5-csv.py --in_file 'C:/Users/<user_name>/FXCACHE/'
```


[contributors-shield]: https://img.shields.io/github/contributors/mgodf/dukascopy_forex_dl.svg?style=flat-square
[contributors-url]: https://github.com/mgodf/dukascopy_forex_dl/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/mgodf/dukascopy_forex_dl.svg?style=flat-square
[forks-url]: https://github.com/mgodf/dukascopy_forex_dl/network/members
[stars-shield]: https://img.shields.io/github/stars/mgodf/dukascopy_forex_dl.svg?style=flat-square
[stars-url]: https://github.com/mgodf/dukascopy_forex_dl/stargazers
[issues-shield]: https://img.shields.io/github/issues/mgodf/dukascopy_forex_dl.svg?style=flat-square
[issues-url]: https://github.com/mgodf/dukascopy_forex_dl/issues
[license-shield]: https://img.shields.io/github/license/mgodf/dukascopy_forex_dl.svg?style=flat-square
[license-url]: https://github.com/mgodf/dukascopy_forex_dl/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/michaeljaygodfrey/