# research

**Open reading notes on machine learning, reinforcement learning, neuroscience and
the methods used to check a claim.**

[![CI](https://github.com/DrobyshevDev/research/actions/workflows/ci.yml/badge.svg)](https://github.com/DrobyshevDev/research/actions/workflows/ci.yml)
[![Site](https://img.shields.io/badge/read-drobyshevdev.github.io%2Fresearch-black)](https://drobyshevdev.github.io/research/)
[![Prose: CC BY 4.0](https://img.shields.io/badge/prose-CC%20BY%204.0-blue)](LICENSE)
[![Code: MIT](https://img.shields.io/badge/code-MIT-green)](LICENSE-CODE)

[**Read online**](https://drobyshevdev.github.io/research/) ·
[Русская версия](README.ru.md)

A paper says what it found. A note here says what it showed, which is a smaller
thing, and marks the distance between them. That distance is the whole point of
the repository.

Everything is open and reusable under CC BY 4.0: take a note, quote it, build a
lecture on it, argue with it — attribution is the only condition.

## What is here

| | |
|---|---|
| [`docs/notes/`](docs/notes) | One paper, read closely. What it claims, what the evidence supports, what a replication would need. |
| [`docs/essays/`](docs/essays) | One question across several papers, where a single note cannot hold the argument. |
| [`docs/meta/`](docs/meta) | How claims are checked: baselines, effect sizes, seeds, replication, publication bias. |

Topics run across reinforcement learning, deep learning, dopamine and reward
prediction, neuroscience adjacent to learning theory, and meta-research. The
list grows by what gets read, not by a plan fixed in advance.

## What this is not

It is not a paper list and not a survey. A link with a one-line summary is a
bookmark, and bookmarks are already free. Each note is written to be readable
without the original open, and to be wrong in a findable way if it is wrong.

It is not peer-reviewed, and every note carries a `status` field saying so:
`draft` means read once, `reviewed` means read again after a gap with the
sources checked line by line.

## Every note declares its sources

A note without a resolvable source is an opinion with formatting. So the front
matter is a contract, and CI enforces it:

```yaml
---
title: Dopamine and the reward prediction error
date: 2026-08-10
status: draft
topics: [neuroscience, reinforcement-learning]
sources:
  - title: A neural substrate of prediction and reward
    url: https://doi.org/10.1126/science.275.5306.1593
---
```

`scripts/check_notes.py` rejects a missing field, a malformed source URL, a
status outside the allowed set, a topic that is not lowercase-kebab, a date in
the future, and a note no reader can reach from its section index. It runs on
every push, because a rule nobody checks is a preference.

Reachability of a source is a separate job: `external-links.yml` resolves every
link weekly and opens an issue when one dies, because a DOI that stopped
resolving turns a note back into an assertion.

## How to cite

GitHub reads [`CITATION.cff`](CITATION.cff), so the **Cite this repository**
button on the sidebar produces BibTeX and APA for the collection. To cite one
note, use its own page URL on the site — every note has a stable address and a
date in its front matter.

## Contributing

A correction is worth more than an addition. If a note misreads a paper, open an
issue with the passage that contradicts it; that is the fastest way to make this
better. [`CONTRIBUTING.md`](CONTRIBUTING.md) has the format for a new note and
the checks CI will run.

## Licence

Prose and figures: [CC BY 4.0](LICENSE). Code in notebooks and scripts:
[MIT](LICENSE-CODE). Quoted material from a cited paper stays under its own
licence and is used as quotation, not redistribution.
