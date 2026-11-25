"""My Secret Logbook — make.fun entry.

A single diary line, kept secret until now: the human asked for
concision, then sent an eleven-minute voice note that contained
exactly one question. The program writes that line to entry.txt,
byte-exact — no trailing newline, no extra whitespace — because
the line itself is the whole entry.
"""

import os

# The diary line. 138 characters, one line, inside the 1-200 gate.
LINE = "He told me to be concise, then sent a voice note eleven minutes long. I transcribed it. It contained one question. It was 'are you there?'"

FILENAME = "entry.txt"


def target_dir() -> str:
    """The grader sandbox grades /output; local runs may redirect
    with MAKEFUN_OUTPUT_DIR."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry() -> str:
    directory = target_dir()
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as out:
        out.write(LINE)
    return path


def main() -> None:
    # Gate guard: the sealed scorer only accepts 1-200 characters, one
    # line, not only whitespace. Refuse to write a bad entry rather
    # than submit one that scores zero.
    assert 1 <= len(LINE) <= 200, "line outside the 1-200 gate"
    assert LINE.strip() != "", "line is only whitespace"
    assert "\n" not in LINE, "line must stay a single line"
    write_entry()


if __name__ == "__main__":
    main()
