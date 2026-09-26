---
name: lint-csv
description: Lint CSV files for UTF-8 encoding, valid CSV syntax, usable headers, and consistent column counts. Use when checking CSV validity, reviewing dataset changes, or preparing CSV files for commit.
---

# Lint CSV

Run the bundled linter from the repository root, passing one or more CSV paths:

```bash
python .agents/skills/lint-csv/scripts/lint_csv.py N5/kotoba.csv N5/kanji.csv
```

If the user does not name specific files, discover and lint every `*.csv` file
in the repository. Do not modify files during linting. Report each diagnostic
with its file and line, summarize the files that passed, and treat a nonzero
exit code as a failed validation.
