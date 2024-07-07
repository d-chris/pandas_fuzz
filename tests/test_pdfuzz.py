from pandas_fuzz import pandas as pd
import pytest


def test_fuzz(accessor):
    assert hasattr(accessor, "fuzz")


def test_methods(accessor, rapidfuzz):
    assert hasattr(accessor.fuzz, rapidfuzz)


def test_callable(accessor, rapidfuzz):
    assert callable(getattr(accessor.fuzz, rapidfuzz))


def test_series_accessor(fuzzy):
    func, s1, s2, result = fuzzy

    d = pd.Series([s1])

    method = getattr(d.fuzz, func)
    res = method(s2)

    assert type(res) == pd.Series
    pd.testing.assert_series_equal(
        res,
        pd.Series([result]),
        check_exact=False,
    )


def test_dataframe_accessor(fuzzy):
    func, s1, s2, result = fuzzy

    d = pd.DataFrame({"s1": [s1, s2], "s2": [s1, s2]})

    method = getattr(d.fuzz, func)
    res = method()

    assert type(res) == pd.Series
    pd.testing.assert_series_equal(
        res,
        pd.Series([100.0, 100.0]),
        check_exact=False,
    )


def test_dataframe_shape():
    with pytest.raises(ValueError):
        pd.DataFrame().fuzz.ratio()


def test_dataframe_columns():
    s1 = "r1"
    s2 = "r2"

    with pytest.raises(ValueError):
        pd.DataFrame({"s1": [s1, s2], "s2": [s1, s2]}).fuzz.ratio("s1", "S2")
