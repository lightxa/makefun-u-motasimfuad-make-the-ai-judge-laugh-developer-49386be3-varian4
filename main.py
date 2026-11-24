"""Make the AI Judge Laugh: Developer Excuses (variant 4).

Writes one funny single-line developer excuse to /output/entry.txt.
Deterministic, pure Python 3.13 stdlib, no network at runtime.

The line is a deadpan Friday-deploy excuse: the rollback plan was
never a procedure, it was the developer staying awake all weekend.
"""

import os

ENTRY = "I shipped on Friday at 5pm because the rollback plan was just me, awake, all weekend."


def _check(text: str) -> None:
    """Enforce the gate: 1-200 chars, single line, not only whitespace."""
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"


def main() -> None:
    _check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
