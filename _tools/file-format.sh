#!/usr/bin/env bash

set -uo pipefail
IFS=$'\n\t'

# Loops through all text files tracked by Git.
git grep -zIl '' |
while IFS= read -rd '' file; do
    # Ensure that file is UTF-8 formatted.
    recode UTF-8 "$file" 2> /dev/null
    # Ensure that file has LF line endings.
    dos2unix "$file" 2> /dev/null
    # Ensure that file does not contain a BOM.
    sed -i '1s/^\xEF\xBB\xBF//' "$file"
    # Ensure that file ends with newline character.
    tail -c1 < "$file" | read -r _ || echo >> "$file";
done

# If a diff has been created, notify the user and exit with an error.
if [[ $(git diff) ]]; then
    echo "Files in this commit do not comply with the file formatting rules."
    echo "The following differences were found between the code and the formatting rules:"
    echo
    git diff --color
    echo
    echo "Please fix your commit(s)"
    echo "::error::Files in this commit do not comply with the file formatting rules." && exit 1
fi

echo "Files in this commit comply with the file formatting rules."
