# pandas-fuzz

Extension for `pandas` to use `rapidfuzz` for fuzzy matching.

## Installation

```bash
pip install pandas_fuzz
```

## Usage

To register the extension make sure to import `pandas_fuzz` before using it.

```python
import pandas as pd
import pandas_fuzz
```

Alternatively, you can import `pandas` from `pandas_fuzz` directly.

```python
from pandas_fuzz import pandas as pd
```

## rapidfuzz.fuzz

`pandas_fuzz` integrates the following functions from `rapidfuzz.fuzz` into `pandas`. These functions are available in the `fuzz` namespace for both `pandas.Series` and `pandas.DataFrame`.

- `rapidfuzz.fuzz.ratio`
- `rapidfuzz.fuzz.partial_ratio`
- `rapidfuzz.fuzz.token_sort_ratio`
- `rapidfuzz.fuzz.token_set_ratio`
- `rapidfuzz.fuzz.WRatio`
- `rapidfuzz.fuzz.QRatio`

## pandas.Series

apply `fuzz.ratio` element wise to `pd.Series`.

```python
>>> pd.Series(["this is a test", "this is a test!"]).fuzz.ratio("this is a test!")
0     96.551724
1    100.000000
dtype: float64
```

## pandas.DataFrame

apply `fuzz.ratio` row wise to columns `s1` and `s2`

```python
>>> pd.DataFrame({
    "s1": ["this is a test", "this is a test!"],
    "s2": ["this is a test", "this is a test!"]
}).fuzz.ratio("s1", "s2")
0    100.0
1    100.0
dtype: float64
```

## Dependencies
[![PyPI - pandas](https://img.shields.io/pypi/v/pandas?logo=pandas&logoColor=white&label=pandas)]([https://](https://pypi.org/project/pandas/))
[![PyPI - Version](https://img.shields.io/pypi/v/rapidfuzz?logo=pypi&logoColor=white&label=rapidfuzz)](https://pypi.org/project/rapidfuzz/)
