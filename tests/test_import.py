import importlib
from pathlib import Path
from unittest import mock

import pytest

from docs import check


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_docstrings():
    """
    Test error case if json containing docstring is not found.

    Filter out UserWarning from pandas of overwriting existing accessors due to reload.
    """

    try:
        with mock.patch.object(Path, "read_text", side_effect=FileNotFoundError):

            import pandas_fuzz

            importlib.reload(pandas_fuzz.pdfuzz)

            assert pandas_fuzz.pdfuzz._docstrings_ == {}
    finally:
        importlib.reload(pandas_fuzz.pdfuzz)
        importlib.reload(pandas_fuzz)


def test_docsjson(capsys):
    """
    Test if json containing docstrings has one for each function.

    Catch any print() messages.
    """

    assert check() == 0
    capsys.readouterr()
