import pandas as pd
from functools import wraps


@pd.api.extensions.register_series_accessor("fuzz")
class FuzzSeriesAccessor:
    """
    Apply `rapidfuzz` methods directly to a `pandas.Series`

    `pandas.Series.fuzz.ratio(s2)` applies elements of the Series as `s1` to
    `rapidfuzz.ratio` and returns the result as a new Series.
    """

    def __init__(self, pandas_obj: pd.Series):
        self._obj = pandas_obj

    @staticmethod
    def _make_method(method):
        @wraps(method)
        def _method(self, s2, **kwargs) -> pd.Series:
            return self._obj.apply(lambda x: method(x, s2, **kwargs))

        return _method


@pd.api.extensions.register_dataframe_accessor("fuzz")
class FuzzDataFrameAccessor:
    """
    Apply `rapidfuzz` methods directly to a `pandas.DataFrame` with at least two columns.

    `pandas.DataFrame.fuzz.ratio(s1, s2)` applies all rows of columns `s1` and `s2` to
    `rapidfuzz.ratio` and returns the result as a new Series.
    """

    def __init__(self, pandas_obj: pd.DataFrame):
        self._obj = pandas_obj

        if self._obj.shape[1] < 2:
            raise ValueError(
                "Cannot apply FuzzDataFrameAccessor to a DataFrame with less than 2 columns"
            )

    @staticmethod
    def _make_method(method):
        @wraps(method)
        def _method(self, s1: str = None, s2: str = None, /, **kwargs) -> pd.Series:

            try:
                col1 = self._obj.columns.get_loc(s1) if s1 else 0
                col2 = self._obj.columns.get_loc(s2) if s2 else 1
            except KeyError as e:
                raise ValueError(f"Column '{e}' not found in DataFrame")

            return self._obj.apply(
                lambda row: method(row.iloc[col1], row.iloc[col2], **kwargs),
                axis=1,
            )

        return _method
