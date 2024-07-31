import subprocess
from pathlib import Path


def main():
    outdir = Path("docs/public")
    outdir.mkdir(exist_ok=True, parents=True)

    try:
        subprocess.run(
            [
                "pdoc",
                "-o",
                outdir,
                "--no-show-source",
                "-t",
                "docs\\dark-mode",
                "pandas_fuzz",
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
