import subprocess


def main():
    try:
        subprocess.run(
            [
                "pdoc",
                "-o",
                "docs\\public",
                "--no-show-source",
                "-t",
                "docs\\dark-mode",
                "pandas_fuzz",
                "pandas",
            ],
            encoding="utf-8",
            check=True,
        )
    except Exception as e:
        print(str(e))
        return 1

    return 0


if __name__ == "__main__":
    SystemExit(main())
