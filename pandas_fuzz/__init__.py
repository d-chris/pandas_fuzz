import rapidfuzz
import pandas

from .pdfuzz import FuzzSeriesAccessor, FuzzDataFrameAccessor

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

__all__ = pandas.__all__
