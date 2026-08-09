# Contributing

A correction is worth more than an addition. The fastest way to improve this
collection is to point at a note that misreads its source.

## Corrections

Open an issue with the passage from the paper that contradicts the note. Quote
it and give the page or section — a disagreement without a locator takes longer
to check than the note took to write.

If you are already sure, a pull request editing the note is welcome. Change the
`status` to `draft` if the correction is substantive: a `reviewed` note that
turned out to be wrong was not reviewed.

## Adding a note

Copy [`templates/note.md`](templates/note.md) into `docs/notes/` and fill it in.
The file name becomes the URL, so it is lowercase and hyphenated, and it does
not change afterwards — a URL that moves breaks every citation of it.

The front matter is a contract, not metadata:

```yaml
---
title: The claim in one line, as the paper would put it
date: 2026-08-10
status: draft
topics: [reinforcement-learning, neuroscience]
sources:
  - title: Full title of the paper
    url: https://doi.org/10.xxxx/yyyyy
---
```

`sources` takes a DOI wherever one exists, because a DOI outlives the publisher's
URL scheme. An arXiv abstract page is acceptable when there is no DOI; a PDF
link found on someone's course page is not.

Link the note from `docs/notes/index.md`. The section index is the list — notes
are deliberately not repeated in the `nav` in `mkdocs.yml`, so adding one means
editing one file rather than two.

`check_notes.py` fails when a note is not linked from its section index.
`mkdocs build --strict` will not catch that on its own: a page outside the
navigation is an INFO line it prints before building the site anyway.

## Translations

A translation sits beside its original as `name.ru.md`, not in a parallel tree,
because a parallel tree drifts out of date without anyone noticing. It carries
the original's `date`, and CI fails if the two disagree.

An untranslated page falls back to English on the Russian site. That is the
intended behaviour: a missing translation should read as missing, not as an
empty page.

## What CI runs

```bash
pip install -r requirements.txt
python scripts/check_notes.py docs   # the front-matter contract
mkdocs build --strict                # links, navigation, orphan pages
```

Both run on every push and pull request. `external-links.yml` runs lychee weekly
against every source link and opens an issue when one dies, because a DOI that
stopped resolving turns a note into an assertion.

## Scope

Notes on machine learning, reinforcement learning, deep learning, neuroscience
adjacent to learning, and meta-research. A note on something else is welcome if
it is read the same way — claim, evidence, what would change the reading.

Product announcements, benchmark tables without a baseline, and summaries
assembled from abstracts are out of scope.

## Licence

Contributions are published under [CC BY 4.0](LICENSE) for prose and
[MIT](LICENSE-CODE) for code. Open a pull request and you are agreeing to that.
