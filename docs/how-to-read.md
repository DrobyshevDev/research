# How to read this

Every note opens with a block of fields. They are not decoration: CI rejects a
note that gets them wrong, so they mean what they say.

## The fields

`title`
:   The claim in one line, phrased as the paper would phrase it — not as the
    note concludes.

`date`
:   When the note was written. It is not updated on a typo fix. A note from two
    years ago that has not been revisited is telling you something.

`status`
:   `draft` — read once. `reviewed` — read again after a gap, with every source
    checked line by line. There is no third value, because a scale invites a
    middle that means nothing.

`topics`
:   Lowercase, hyphenated. Used for grouping, not for keywords.

`sources`
:   What the note rests on, each with a resolvable link — a DOI where one
    exists. A note with no source does not build.

## The sections

A note runs in the same order every time: what the paper claims, what its
evidence shows, what would change the reading. The middle section is the one
worth your attention, because that is where a claim and its support are allowed
to come apart.

The last section is a commitment. A note that cannot say what would falsify it
is describing a belief, and belongs in [Essays](essays/index.md) instead, where
that is the point.

## What to distrust here

The notes are written by one reader, unreviewed, often outside their author's
field. Neuroscience notes in particular are read from the outside: the summary
of a method may be right in outline and wrong in the detail that matters to
someone who runs it.

So read them the way they are written — as a first pass with its sources in the
open, checkable against the originals. If a note misreads a paper,
[the issue tracker](https://github.com/DrobyshevDev/research/issues/new/choose)
is the right place, and a correction beats a new note.

## Reuse

CC BY 4.0. Quote it, teach from it, translate it, disagree with it in print —
name the source and you are done. Individual notes are citable by their page
URL; the collection has a [`CITATION.cff`](https://github.com/DrobyshevDev/research/blob/main/CITATION.cff)
and a **Cite this repository** button on GitHub.
