# Git hooks for Rebel Documentation

Hooks are `bash` scripts that are run when calling `git commit`.
Hooks help Rebel Documentation contributors comply with the Rebel Documentation requirements.

## Installation

Ensure that
[`codespell`](https://github.com/codespell-project/codespell)
is installed and available in the system `path`.
Copy all the files from this folder into your `.git/hooks` folder.
Confirm that all the scripts are executable.

## Hook Details

## `pre-commit`

`pre-commit` is the hook called by Git when calling `git commit`.
The `pre-commit` hook checks the documentation spelling.
