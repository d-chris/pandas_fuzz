import inspect
import json
from pathlib import Path
from typing import Any, Callable

import pandas as pd

try:
    _docstrings_ = json.loads(
        Path(__file__).with_suffix(".json").read_text(encoding="utf-8")
    )
except FileNotFoundError:
    _docstrings_ = {}


@pd.api.extensions.register_series_accessor("fuzz")
class FuzzSeriesAccessor:

    def __init__(self, pandas_obj: pd.Series):
        """
        Apply `rapidfuzz` methods directly to a `pandas.Series`

        `pandas.Series.fuzz.ratio(s2)` applies elements of the Series as `s1` to
        `rapidfuzz.ratio` and returns the result as a new Series.
        """
        self._obj = pandas_obj

    @classmethod
    def _make_method(cls, method: Callable[..., Any]) -> Callable[..., pd.Series]:

        def _wrapper(self, s2, **kwargs) -> pd.Series:
            return self._obj.apply(lambda x: method(x, s2, **kwargs))

        try:
            _wrapper.__doc__ = "\n".join(_docstrings_[cls.__name__][method.__name__])
        except KeyError:
            _wrapper.__doc__ = method.__doc__
        else:
            sig = inspect.signature(method)
            params = [param for name, param in sig.parameters.items() if name != "s1"]

            _wrapper.__signature__ = sig.replace(
                parameters=params, return_annotation=pd.Series
            )

        return _wrapper


@pd.api.extensions.register_dataframe_accessor("fuzz")
class FuzzDataFrameAccessor:

    def __init__(self, pandas_obj: pd.DataFrame):
        """
        Apply `rapidfuzz` methods directly to a `pandas.DataFrame` with at least
        two columns.

        `pandas.DataFrame.fuzz.ratio(s1, s2)` applies all rows of columns `s1` and `s2`
        to `rapidfuzz.ratio` and returns the result as a new Series.
        """
        self._obj = pandas_obj

        if self._obj.shape[1] < 2:
            raise ValueError(
                "Can't apply FuzzDataFrameAccessor to a DataFrame "
                "with less than 2 columns."
            )

    @classmethod
    def _make_method(cls, method):

        def _wrapper(self, s1: str = None, s2: str = None, /, **kwargs) -> pd.Series:

            try:
                col1 = self._obj.columns.get_loc(s1) if s1 else 0
                col2 = self._obj.columns.get_loc(s2) if s2 else 1
            except KeyError as e:
                raise ValueError(f"Column '{e}' not found in DataFrame")

            return self._obj.apply(
                lambda row: method(row.iloc[col1], row.iloc[col2], **kwargs),
                axis=1,
            )

        try:
            _wrapper.__doc__ = "\n".join(_docstrings_[cls.__name__][method.__name__])
        except KeyError:
            _wrapper.__doc__ = method.__doc__
        else:
            _wrapper.__signature__ = inspect.signature(method).replace(
                return_annotation=pd.Series
            )

        return _wrapper
