---
name: validate-kanji-vocabulary-ids
description: Validate kanji_id values in JLPT kanji_vocabulary.csv files against the corresponding kanji.csv. Use when checking kanji vocabulary data, reviewing new kanji CSV entries, or preparing these datasets for commit.
---

# Validate Kanji Vocabulary IDs

Run the bundled validator from the repository root for each requested JLPT level:

```bash
bash .agents/skills/validate-kanji-vocabulary-ids/scripts/validate-kanji-vocabulary-ids.sh N5/kanji.csv N5/kanji_vocabulary.csv
```

On Windows, if `bash` is not on `PATH`, invoke the same script with Git Bash at
`C:\Program Files\Git\bin\bash.exe`.

If no level is specified, validate every `N*/kanji_vocabulary.csv` that has a
corresponding `kanji.csv`. Do not edit either CSV during validation. Report the
file and line diagnostics emitted by the script and treat any nonzero exit code
as a failed validation.
