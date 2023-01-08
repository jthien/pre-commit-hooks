from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence


def check_filename_prefix(filename: str, prefixes: list) -> int:
    retv = 1
    file = Path(filename)
    # print("Check " + filename + "(" + file.name + ")")
    for prefix in prefixes:
        # print("Start with " + prefix)
        if file.name.startswith(prefix):
            retv = 0
    # print("Result " + str(retv))
    return retv


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    parser.add_argument(
        "--allowed_prefix",
        dest="allowed_prefix",
        action="append",
        default=[],
    )

    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        retv |= check_filename_prefix(filename, args.allowed_prefix)

    return retv


if __name__ == "__main__":
    raise SystemExit(main())
