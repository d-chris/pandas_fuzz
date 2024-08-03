import pytest
from rapidfuzz import fuzz

from pandas_fuzz import pandas as pd


@pytest.fixture(
    params=[name for name in fuzz.__all__ if callable(getattr(fuzz, name))],
)
def rapidfuzz(request):
    return request.param


@pytest.fixture(
    params=[
        pd.Series,
        pd.DataFrame,
    ],
    ids=lambda x: x.__name__,
)
def accessor(request):
    return request.param


@pytest.fixture(
    params=[
        (
            "ratio",
            "this is a test",
            "this is a test!",
            96.55172413793103,
        ),
        (
            "ratio",
            "fuzzy wuzzy was a bear",
            "wuzzy fuzzy was a bear",
            90.9090909090909,
        ),
        (
            "token_sort_ratio",
            "fuzzy wuzzy was a bear",
            "wuzzy fuzzy was a bear",
            100.0,
        ),
        (
            "token_sort_ratio",
            "fuzzy was a bear",
            "fuzzy fuzzy was a bear",
            84.21052631578947,
        ),
        (
            "token_set_ratio",
            "fuzzy was a bear",
            "fuzzy fuzzy was a bear",
            100.0,
        ),
        (
            "token_set_ratio",
            "fuzzy was a bear but not a dog",
            "fuzzy was a bear",
            100.0,
        ),
        (
            "token_set_ratio",
            "fuzzy was a bear but not a dog",
            "fuzzy was a bear but not a cat",
            92.3076923076923,
        ),
        (
            "WRatio",
            "this is a test",
            "this is a new test!!!",
            85.5,
        ),
        (
            "WRatio",
            "this is a test",
            "this is a new test",
            95.0,
        ),
        (
            "WRatio",
            "this is a word",
            "THIS IS A WORD",
            21.42857142857143,
        ),
        (
            "QRatio",
            "this is a test",
            "this is a new test!!!",
            80.0,
        ),
        (
            "QRatio",
            "this is a test",
            "this is a new test",
            87.5,
        ),
        (
            "QRatio",
            "this is a word",
            "THIS IS A WORD",
            21.42857142857143,
        ),
    ],
    ids=lambda x: f"{x[0]}-'{x[1]}'-'{x[2]}'_{x[3]:.3f}",
)
def fuzzy(request):
    return request.param
