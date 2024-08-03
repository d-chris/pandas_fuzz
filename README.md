# pandas-fuzz

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pandas_fuzz)](https://pypi.org/project/pandas_fuzz/)
[![PyPI](https://img.shields.io/pypi/v/pandas_fuzz)](https://pypi.org/project/pandas_fuzz/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pandas_fuzz)](https://pypi.org/project/pandas_fuzz/)
[![PyPI - License](https://img.shields.io/pypi/l/pandas_fuzz)](https://raw.githubusercontent.com/d-chris/pandas_fuzz/main/LICENSE)
[![GitHub Workflow Test)](https://img.shields.io/github/actions/workflow/status/d-chris/pandas_fuzz/pytest.yml?logo=github&label=pytest)](https://github.com/d-chris/pandas_fuzz/actions/workflows/pytest.yml)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fd-chris.github.io%2Fpandas_fuzz&up_message=pdoc&logo=github&label=documentation)](https://d-chris.github.io/pandas_fuzz)
[![GitHub tag (with filter)](https://img.shields.io/github/v/tag/d-chris/pandas_fuzz?logo=github&label=github)](https://github.com/d-chris/pandas_fuzz)
[![codecov](https://codecov.io/gh/d-chris/pandas_fuzz/graph/badge.svg?token=XLHILYJB00)](https://codecov.io/gh/d-chris/pandas_fuzz)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)

---

Extension for `pandas` to use `rapidfuzz` for fuzzy matching.

## Requirements

- Python 3.9 or later
- On Windows the [Visual C++ 2019 redistributable](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads) is required

## Installation

```bash
pip install pandas_fuzz
```

## Usage

To register the extension make sure to import `pandas_fuzz` before using it`.

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
- `rapidfuzz.fuzz.partial_ratio_alignment`
- `rapidfuzz.fuzz.token_sort_ratio`
- `rapidfuzz.fuzz.token_set_ratio`
- `rapidfuzz.fuzz.token_ratio`
- `rapidfuzz.fuzz.partial_token_sort_ratio`
- `rapidfuzz.fuzz.partial_token_set_ratio`
- `rapidfuzz.fuzz.partial_token_ratio`
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

[![PyPI - pandas](https://img.shields.io/pypi/v/pandas?logo=pandas&logoColor=white&label=pandas)](https://pypi.org/project/pandas/)
[![PyPI - Version](https://img.shields.io/pypi/v/rapidfuzz?logo=pypi&logoColor=white&label=rapidfuzz)](https://pypi.org/project/rapidfuzz/)

---
