# Changelog

Notes are dated in their own front matter, so this file records changes to the
collection — its structure, its rules, its tooling — rather than every text
added.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- The repository: bilingual site, front-matter contract, and the checks that
  enforce it.
- `scripts/check_notes.py` — rejects a note with a missing field, an
  unresolvable source, a status outside `draft`/`reviewed`, a topic that is not
  lowercase-kebab, or a date in the future.
- `CITATION.cff`, so the collection is citable from the GitHub sidebar.
- First note: dopamine neurons and the reward prediction error.
