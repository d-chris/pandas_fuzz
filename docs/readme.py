import pandas_fuzz


def main():
    """
    Render the README.md file using the README.md.jinja2 template.

    Requires following PyPi packages:
    - 'jinja2'
    - 'pathlibutil'

    Returns non-zero on failure.
    """

    try:
        from jinja2 import Environment
        from pathlibutil import Path

        with Path(__file__).parent as cwd:

            template = cwd / "README.md.jinja2"
            readme = (cwd / "../README.md").resolve()

            with template.open("r") as file:
                template = Environment(
                    keep_trailing_newline=True,
                ).from_string(file.read())

            with readme.open("w") as file:
                file.write(
                    template.render(
                        methods=pandas_fuzz.__functions__,
                    )
                )

    except Exception as e:
        print(f"{readme=} creation failed!\n\t{e}")
        return 1

    print(f"{readme=} created successfully!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
