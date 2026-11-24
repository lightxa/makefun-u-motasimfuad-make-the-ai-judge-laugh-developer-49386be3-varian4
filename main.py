"""Make the AI Judge Laugh: Developer Excuses (variant 4).

Writes one funny single-line developer excuse to /output/entry.txt.
Deterministic, pure Python 3.13 stdlib, no network at runtime.

The joke is a deadpan Friday-deploy excuse: the rollback plan was
never a written procedure, it was the developer staying awake
all weekend to watch the deploy by hand.
"""

import os

ENTRY = "I shipped on Friday at 5pm because the rollback plan was just me, awake, all weekend."

OUTPUT_PATH = "/output/entry.txt"


MIN_LENGTH = 1
MAX_LENGTH = 200


def validate_entry(text: str) -> None:
    """Enforce the gate: 1-200 characters, single line, not blank.

    Each rule is checked separately so a failure names the exact
    rule that was broken instead of a generic assertion.
    """
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(text)}"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line with no line breaks")
    if not text.strip():
        raise ValueError("entry must contain non-whitespace characters")


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
