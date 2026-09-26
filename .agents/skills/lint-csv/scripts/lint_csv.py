#!/usr/bin/env python3

import argparse
import csv
import sys
from pathlib import Path


def lint_csv(path: Path) -> bool:
    errors: list[str] = []
    row_count = 0
    column_count = 0

    try:
        handle = path.open("r", encoding="utf-8-sig", newline="")
    except (OSError, UnicodeError) as error:
        print(f"{path}: {error}", file=sys.stderr)
        return False

    try:
        with handle:
            reader = csv.reader(handle, strict=True)

            try:
                header = next(reader)
            except StopIteration:
                errors.append("1: file is empty")
                header = []
            except (csv.Error, UnicodeError) as error:
                errors.append(f"{reader.line_num or 1}: {error}")
                header = []

            if header:
                column_count = len(header)
                normalized_header = [name.strip() for name in header]

                if any(not name for name in normalized_header):
                    errors.append("1: header contains an empty column name")

                duplicate_headers = sorted(
                    {name for name in normalized_header if normalized_header.count(name) > 1}
                )
                if duplicate_headers:
                    errors.append(
                        "1: duplicate header name(s): " + ", ".join(duplicate_headers)
                    )

                while True:
                    start_line = reader.line_num + 1
                    try:
                        row = next(reader)
                    except StopIteration:
                        break
                    except (csv.Error, UnicodeError) as error:
                        errors.append(f"{reader.line_num or start_line}: {error}")
                        break

                    row_count += 1
                    if not row or all(not value for value in row):
                        errors.append(f"{start_line}: blank row")
                    elif len(row) != column_count:
                        errors.append(
                            f"{start_line}: expected {column_count} columns, found {len(row)}"
                        )
    except UnicodeError as error:
        errors.append(f"invalid UTF-8: {error}")

    if errors:
        for error in errors:
            print(f"{path}:{error}", file=sys.stderr)
        print(f"{path}: FAILED ({len(errors)} error(s))", file=sys.stderr)
        return False

    print(f"{path}: OK ({row_count} data row(s), {column_count} column(s))")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint CSV syntax and structure.")
    parser.add_argument("files", nargs="+", type=Path, help="CSV files to validate")
    args = parser.parse_args()

    results = [lint_csv(path) for path in args.files]
    return 0 if all(results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
