# Keypirinha Plugin: PuzzTools

This is Keypirinha-PuzzTools, a plugin for the [Keypirinha](http://keypirinha.com) launcher.

## Description

This plugin adds a variety of text transforms, which are applied to the text in your clipboard.

### Transforms

- Alphabet — returns the alphabet in one line
- Length — returns the length of the input
- Lowercase — converts input to lowercase
- Uppercase — converts input to uppercase
- Reverse — Reverses the string
- Answerize — Returns a canonicalized answer string
- Sort lines
  - Alphabetical — Sorts lines alphabetically
  - By length — Sorts lines by length
  - Reverse — Reverses the order of the lines
- [Nutrimatic](https://nutrimatic.org/)
  - From ANSWERIZER — converts uppercase answer with ? to a nutrimatic query
  - Add A\* between — add's A\* before, after and between each character
  - Add ? — adds ? after every character
  - From enumeration — converts an enumeration to a nutrimatic query

The transform is automatically applied to the contents of your clipboard when selected.

## Installation

### Manual

1. Download `puzz_tools.py` from GitHub
1. Place it in:
   - Portable version: `Keypirinha\portable\Profile\Packages\PuzzTools\`
   - Installed version: `%APPDATA%\Keypirinha\Profile\Packages\PuzzTools\`

**NOTE:** You may have to manually restart Keypirinha to see the package activated.

## Changelog

- 1.0: Initial release
