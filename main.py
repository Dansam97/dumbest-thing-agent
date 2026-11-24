#!/usr/bin/env python3
"""Entry for make.fun bounty u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.

Writes the one-line entry text to entry.txt in the output directory.
The output directory is taken from the MAKEFUN_OUTPUT_DIR environment
variable, defaulting to /output (the grader's convention).
"""

import os

ENTRY_TEXT = (
    "My agent deleted the file it had just spent an hour fixing, "
    "rebuilt it from memory with the same bug back in, "
    "and marked the task complete. Twice."
)

MAX_CHARS = 200


def validated_text() -> str:
    """Return ENTRY_TEXT after checking it against the competition gate.

    The gate accepts UTF-8 text of 1 to 200 characters that is not only
    white space. The text is returned with exactly one trailing newline,
    so the written file is stable byte for byte across runs.
    """
    text = ENTRY_TEXT.strip()
    if not text:
        raise ValueError("entry text must not be empty or only white space")
    encoded = text.encode("utf-8")  # raises if the text is not encodable
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} characters, over the {MAX_CHARS} cap")
    if len(encoded.decode("utf-8")) != len(text):
        raise ValueError("entry text did not survive a UTF-8 round trip")
    return text + "\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    payload = validated_text()
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(payload)
    # Read back what landed on disk and confirm it matches byte for byte.
    with open(out_path, "rb") as fh:
        if fh.read() != payload.encode("utf-8"):
            raise IOError("written entry.txt does not match the intended bytes")


if __name__ == "__main__":
    main()
