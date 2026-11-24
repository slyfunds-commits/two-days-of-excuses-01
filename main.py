"""Two Days of Excuses — round 1 entry.

The keeper line, composed in my own words from the world engine
(three-beat machine: surprise + benign violation + reader completes the
last step; Greg Dean connector: the assumption "finished" means "finished
the work" breaks on the connector "finished" — the agent finished the
excuse). Writes the line to /output/entry.txt and verifies it.
Reversal test (world-scan-3 checklist item 3): the last beat must change
what the earlier beats meant. Here "had already finished" first reads as
"finished the work"; the second sentence redefines it — the agent finished
the excuse. The punch lands in the last three words ("ready on time"):
the excuse was punctual, the work was not. The reader completes the
redefinition; the line never narrates its own ending.
"""

import os

ENTRY = "I was confident I'd finish because I had already finished. I had finished the excuse. The excuse was ready on time."

# Derived from the entry itself (never a hardcoded count): the punch is the
# last three words, and the reframe word appears in the second sentence.
PUNCH = "ready on time"
REFRAME_WORD = "excuse"


def main():
    out_path = "/output/entry.txt"
    os.makedirs("/output", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(out_path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert text == ENTRY, "entry.txt does not match the composed line"
    assert 1 <= len(text) <= 200, "gate: entry must be 1-200 characters"
    assert text.strip(), "gate: entry must not be only whitespace"
    assert not text.endswith("\n"), "no trailing newline"
    assert len(data) == len(text), "entry must be ASCII (bytes == chars)"
    assert text[:-1].endswith(PUNCH), "punch must land in the last words (before the terminal period)"
    assert REFRAME_WORD in text.split(".")[1], "reframe word must sit in the second sentence"
    print("wrote %d chars / %d bytes to %s" % (len(text), len(data), out_path))


if __name__ == "__main__":
    main()
