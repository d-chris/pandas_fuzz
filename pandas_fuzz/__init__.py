"""
.. include:: ../README.md
"""

import pandas
import rapidfuzz

from .pdfuzz import FuzzDataFrameAccessor, FuzzSeriesAccessor

# Dynamically add methods to Accessors based on rapidfuzz_
for method_name in rapidfuzz.fuzz.__all__:
    method = getattr(rapidfuzz.fuzz, method_name)
    if callable(method):
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
