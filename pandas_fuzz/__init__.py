"""
.. include:: ../README.md
"""

import pandas
import rapidfuzz

from pandas_fuzz.pdfuzz import FuzzDataFrameAccessor, FuzzSeriesAccessor

__functions__ = [
    func for func in rapidfuzz.fuzz.__all__ if callable(getattr(rapidfuzz.fuzz, func))
]

# Dynamically add methods to Accessors based on rapidfuzz_
for method_name in __functions__:
    method = getattr(rapidfuzz.fuzz, method_name)

    setattr(
        FuzzSeriesAccessor,
        method_name,
        FuzzSeriesAccessor._make_method(method),
    )
    setattr(
        FuzzDataFrameAccessor,
        method_name,
        FuzzDataFrameAccessor._make_method(method),
    )


__all__ = [
    "pandas",
    "rapidfuzz",
    "FuzzDataFrameAccessor",
    "FuzzSeriesAccessor",
]
