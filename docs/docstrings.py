import json
import pathlib

import pandas_fuzz


def main():
    """
    Check if all docstrings are present and of the correct type.

    Returns non-zero on failure.
    """

    try:

        docstrings = pathlib.Path(pandas_fuzz.__file__).with_name("pdfuzz.json")

        with docstrings.open("r") as f:
            data = json.load(f)

        for accessor, docs in data.items():
            for func in pandas_fuzz.__functions__:
                try:
                    doc = docs[func]
                except KeyError as e:
                    raise KeyError(f"Missing docstring for {accessor}.{func}!") from e

                if not all(isinstance(s, str) for s in doc):
                    raise ValueError(f"Type {accessor}.{func} is not a string!")

    except Exception as e:
        print(f"{docstrings=} check failed!\n\t{e}")
        return 1

    print(f"{docstrings=} check passed!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
