"""Check that every note keeps the front-matter contract.

A note without a resolvable source is an opinion with formatting. The README
promises that each one declares what it rests on; this script is what makes the
promise checkable rather than aspirational.

It also refuses a note no reader can reach, because `mkdocs build --strict`
does not: a page outside the navigation is an INFO line it prints before
building the site anyway.

Reachability of a URL is deliberately not tested here. That needs the network,
which makes the check flaky and slow, and a dead link is a different failure
from a malformed one - `external-links.yml` runs lychee weekly for that.

Usage:
    python scripts/check_notes.py [docs]

Exits 0 when every note passes, 1 when any note fails, 2 on a usage error.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

# Sections whose Markdown files are notes. Anything outside them - the landing
# page, `how-to-read.md` - is prose about the collection, not a note in it, and
# carries no front matter.
NOTE_DIRS = ("notes", "essays", "meta")

# A section index lists what is in the section. It is navigation, not a note.
EXEMPT_NAMES = {"index.md", "index.ru.md"}

REQUIRED_FIELDS = ("title", "date", "status", "topics", "sources")
ALLOWED_STATUS = ("draft", "reviewed")

# Lowercase kebab, because a topic becomes part of a URL and a tag page. Mixed
# case gives you `Reinforcement-Learning` and `reinforcement-learning` as two
# topics that a reader reasonably expects to be one.
TOPIC_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

FRONT_MATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


class NoteError(Exception):
    """A single contract violation, already phrased for the reader."""


def read_note(path: Path) -> str:
    """Read a note, tolerating a byte-order mark.

    Editors on Windows save UTF-8 with a BOM by default, and PowerShell's
    Set-Content does it too. The mark makes the front-matter block start one
    character late, so the file gets rejected for having no front matter while
    the front matter is sitting right there. utf-8-sig strips the mark when it
    is present and behaves like utf-8 when it is not.
    """
    return path.read_text(encoding="utf-8-sig")


def parse_front_matter(text: str) -> dict:
    match = FRONT_MATTER_RE.match(text)
    if match is None:
        raise NoteError(
            "no front matter. The file must open with a --- block; "
            "copy templates/note.md to start one."
        )

    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        raise NoteError(f"the front matter is not valid YAML: {exc}") from exc

    if not isinstance(data, dict):
        raise NoteError("the front matter must be a mapping of field to value.")

    return data


def check_date(value: object) -> dt.date:
    # PyYAML already turns an unquoted ISO date into a date object. Anything
    # else means it was quoted or written in some other shape, and the writer
    # gets told which one it should have been.
    if isinstance(value, dt.datetime):
        value = value.date()

    if not isinstance(value, dt.date):
        raise NoteError(
            f"`date` must be an unquoted ISO date such as 2026-08-10, got {value!r}."
        )

    # One day of slack, because the runner is on UTC and the writer is not. A
    # note dated on the evening of the 10th in Moscow is still the 9th in UTC,
    # and failing that build teaches nobody anything. The check is here to
    # catch a mistyped year, and 2099 clears any tolerance you like.
    if value > dt.date.today() + dt.timedelta(days=1):
        raise NoteError(f"`date` is in the future: {value.isoformat()}.")

    return value


def check_topics(value: object) -> None:
    if not isinstance(value, list) or not value:
        raise NoteError("`topics` must be a non-empty list.")

    for topic in value:
        if not isinstance(topic, str) or not TOPIC_RE.match(topic):
            raise NoteError(
                f"topic {topic!r} must be lowercase words joined by hyphens, "
                "such as reinforcement-learning."
            )


def check_sources(value: object) -> None:
    if not isinstance(value, list) or not value:
        raise NoteError(
            "`sources` must list at least one source. A note with nothing to "
            "point at belongs in docs/essays/ with the papers it argues from."
        )

    for index, source in enumerate(value, start=1):
        where = f"source {index}"

        if not isinstance(source, dict):
            raise NoteError(f"{where} must be a mapping with `title` and `url`.")

        title = source.get("title")
        if not isinstance(title, str) or not title.strip():
            raise NoteError(f"{where} has no `title`.")

        url = source.get("url")
        if not isinstance(url, str) or not url.strip():
            raise NoteError(f"{where} ({title}) has no `url`.")

        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            raise NoteError(
                f"{where} ({title}) has `url` {url!r}, which is not an http(s) "
                "address. Prefer a DOI: https://doi.org/10.xxxx/yyyy."
            )


def check_note(path: Path, docs_root: Path) -> list[str]:
    """Return the problems found in one note, phrased for whoever wrote it."""
    problems: list[str] = []
    relative = path.relative_to(docs_root).as_posix()

    try:
        text = read_note(path)
    except UnicodeDecodeError as exc:
        return [f"{relative}: not valid UTF-8 ({exc})."]

    try:
        data = parse_front_matter(text)
    except NoteError as exc:
        return [f"{relative}: {exc}"]

    missing = [field for field in REQUIRED_FIELDS if field not in data]
    if missing:
        problems.append(f"{relative}: missing field(s): {', '.join(missing)}.")

    if "title" in data:
        title = data["title"]
        if not isinstance(title, str) or not title.strip():
            problems.append(f"{relative}: `title` must be a non-empty string.")

    if "date" in data:
        try:
            check_date(data["date"])
        except NoteError as exc:
            problems.append(f"{relative}: {exc}")

    if "status" in data and data["status"] not in ALLOWED_STATUS:
        problems.append(
            f"{relative}: `status` is {data['status']!r}, expected one of "
            f"{', '.join(ALLOWED_STATUS)}."
        )

    for field, check in (("topics", check_topics), ("sources", check_sources)):
        if field in data:
            try:
                check(data[field])
            except NoteError as exc:
                problems.append(f"{relative}: {exc}")

    # A Russian note is a translation, not a separate note: it must have an
    # English original beside it, and the pair must not drift apart on the date.
    if path.name.endswith(".ru.md"):
        original = path.with_name(path.name[: -len(".ru.md")] + ".md")
        if not original.exists():
            problems.append(
                f"{relative}: translation with no original at "
                f"{original.relative_to(docs_root).as_posix()}."
            )
        elif "date" in data:
            try:
                original_data = parse_front_matter(read_note(original))
            except NoteError:
                # The original is broken on its own account and already
                # reported. Saying so twice helps nobody.
                original_data = {}
            else:
                if original_data.get("date") != data.get("date"):
                    problems.append(
                        f"{relative}: `date` differs from the English original. "
                        "A translation carries the original's date."
                    )

    return problems


def iter_notes(docs_root: Path):
    for section in NOTE_DIRS:
        directory = docs_root / section
        if not directory.is_dir():
            continue
        for path in sorted(directory.rglob("*.md")):
            if path.name not in EXEMPT_NAMES:
                yield path


def check_orphans(docs_root: Path, notes: list[Path]) -> list[str]:
    """Every note must be reachable from its section index.

    `mkdocs build --strict` does not cover this: a page missing from the
    navigation is an INFO line it prints and then builds anyway. Notes are
    deliberately kept out of `nav` - the section index is the list, so adding a
    note means editing one file rather than two - which leaves this as the only
    thing standing between a published note and a page nobody can reach.
    """
    problems: list[str] = []

    for note in notes:
        section = note.parent
        # A Russian note is linked from the Russian index, and under the name of
        # the English file: mkdocs-static-i18n resolves the suffix at build
        # time, so `note.md` is the correct link there, not `note.ru.md`.
        if note.name.endswith(".ru.md"):
            index = section / "index.ru.md"
            target = note.name[: -len(".ru.md")] + ".md"
        else:
            index = section / "index.md"
            target = note.name

        relative = note.relative_to(docs_root).as_posix()

        if not index.exists():
            problems.append(
                f"{relative}: no {index.relative_to(docs_root).as_posix()} "
                "to be listed in."
            )
            continue

        if target not in read_note(index):
            problems.append(
                f"{relative}: not linked from "
                f"{index.relative_to(docs_root).as_posix()}, "
                "so no reader can reach it."
            )

    return problems


def main(argv: list[str]) -> int:
    if len(argv) > 2:
        print(__doc__, file=sys.stderr)
        return 2

    docs_root = Path(argv[1] if len(argv) == 2 else "docs")
    if not docs_root.is_dir():
        print(f"No such directory: {docs_root}", file=sys.stderr)
        return 2

    notes = list(iter_notes(docs_root))
    problems: list[str] = []
    for path in notes:
        problems.extend(check_note(path, docs_root))
    problems.extend(check_orphans(docs_root, notes))

    if problems:
        print(f"{len(problems)} problem(s) in {len(notes)} note(s):\n")
        for problem in problems:
            print(f"  {problem}")
        print("\nThe front-matter contract is described in CONTRIBUTING.md.")
        return 1

    print(f"{len(notes)} note(s) checked, all keep the front-matter contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
