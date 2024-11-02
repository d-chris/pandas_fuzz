import importlib
import warnings
from pathlib import Path


def test_docstrings(mocker):

    with warnings.catch_warnings(record=True):
        try:
            with mocker.patch.object(Path, "read_text", side_effect=FileNotFoundError):

                import pandas_fuzz

                importlib.reload(pandas_fuzz.pdfuzz)

                assert pandas_fuzz.pdfuzz._docstrings_ == {}
        finally:
            importlib.reload(pandas_fuzz)
