# Keypirinha Plugin: PuzzTools

This is Keypirinha-PuzzTools, a plugin for the [Keypirinha](http://keypirinha.com) launcher.

## Description

This plugin adds a variety of text transforms, which are applied to the text in your clipboard.

### Transforms

- Alphabet — returns the alphabet in one line
- Answerize — Returns a canonicalized answer string
- Kebab case — Converts input into kebab-case
- Length — returns the length of the input
- Lowercase — converts input to lowercase
- [Nutrimatic](https://nutrimatic.org/)
  - From ANSWERIZER — converts uppercase answer with ? to a nutrimatic query
  - Add A\* between — add's A\* before, after and between each character
  - Add ? — adds ? after every character
  - From enumeration — converts an enumeration to a nutrimatic query
- Reverse — Reverses the string
- Rotate — Rotates a 2D grid of data 90 degrees clockwise
- Snake case — Converts input into snake_case
- Sort lines
  - Alphabetical — Sorts lines alphabetically
  - By length — Sorts lines by length
  - Reverse — Reverses the order of the lines
- Transpose — Transposes the input, taking characters as columns and lines as rows.
  If a tab is found in the input, it'll use that for columns instead.
- Uppercase — converts input to uppercase

The transform is automatically applied to the contents of your clipboard when selected.

Optionally, you can pass a custom input to the transform by pressing TAB on the item.

## Installation

### Manual

1. Download `puzz_tools.py` from GitHub
1. Place it in:
   - Portable version: `Keypirinha\portable\Profile\Packages\PuzzTools\`
   - Installed version: `%APPDATA%\Keypirinha\Profile\Packages\PuzzTools\`

**NOTE:** You may have to manually restart Keypirinha to see the package activated.

## Changelog

- 1.0: Initial release
- 1.1: Added transpose transform
- 1.2: Allow user to pass custom input to transforms
- 1.3: Added snake_case and kebab-case transforms
- 1.4: Moved to a new file, refactored grid transforms and added rotate