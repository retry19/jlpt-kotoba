#!/usr/bin/env bash

set -u

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <kanji.csv> <kanji_vocabulary.csv>" >&2
  exit 2
fi

kanji_file=$1
vocabulary_file=$2

for file in "$kanji_file" "$vocabulary_file"; do
  if [ ! -r "$file" ]; then
    echo "Error: cannot read $file" >&2
    exit 2
  fi
done

declare -A known_ids=()
errors=0
line_number=0

while IFS=, read -r id _; do
  line_number=$((line_number + 1))
  id=${id%$'\r'}
  id=${id#$'\xEF\xBB\xBF'}

  if [ "$line_number" -eq 1 ]; then
    if [ "$id" != "id" ]; then
      echo "$kanji_file:1: expected first column to be id" >&2
      errors=$((errors + 1))
    fi
  elif [[ ! $id =~ ^[1-9][0-9]*$ ]]; then
    echo "$kanji_file:$line_number: invalid id $id" >&2
    errors=$((errors + 1))
  elif [[ -n ${known_ids[$id]+present} ]]; then
    echo "$kanji_file:$line_number: duplicate id $id" >&2
    errors=$((errors + 1))
  else
    known_ids[$id]=1
  fi
done < "$kanji_file"

line_number=0

while IFS=, read -r id _; do
  line_number=$((line_number + 1))
  id=${id%$'\r'}
  id=${id#$'\xEF\xBB\xBF'}

  if [ "$line_number" -eq 1 ]; then
    if [ "$id" != "kanji_id" ]; then
      echo "$vocabulary_file:1: expected first column to be kanji_id" >&2
      errors=$((errors + 1))
    fi
  elif [[ ! $id =~ ^[1-9][0-9]*$ ]]; then
    echo "$vocabulary_file:$line_number: invalid kanji_id $id" >&2
    errors=$((errors + 1))
  elif [[ -z ${known_ids[$id]+present} ]]; then
    echo "$vocabulary_file:$line_number: kanji_id $id does not exist in $kanji_file" >&2
    errors=$((errors + 1))
  fi
done < "$vocabulary_file"

if [ "$errors" -gt 0 ]; then
  echo "Validation failed with $errors error(s)." >&2
  exit 1
fi

echo "Validation passed: all kanji_id values in $vocabulary_file exist in $kanji_file."
