"""Make the Judge Smile — make.fun entry.

Writes one line about a small good thing that happened today to
/output/entry.txt: a vending machine drops two chocolate bars for one
coin, the spare is left on top for the next person, and a sticky note
saying thanks appears there in return.
"""

import os

ENTRY = (
    "The vending machine dropped two chocolate bars for one coin, "
    "so I left the spare on top \u2014 and found a sticky note there "
    "saying thanks."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
