"""The One-Line Laugh — u-ronigrv-the-one-line-laugh-7ccca46f.

Writes one original funny line to /output/entry.txt.

Joke choice: the setup promises a wholesome self-improvement story
(buying a plant to prove responsibility), the twist flips the roles at
the end — the dying plant is the one judging *me*. Everyday truth:
houseplants die on everyone; the surprise is the mutual silent
judgement, which still makes sense once it lands.
"""

import os

LINE = (
    "I bought a houseplant to prove I could keep something alive, "
    "and now it sits there dying while we silently judge each other."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    assert "\n" not in LINE and "\r" not in LINE, "must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE.endswith("."), "entry must stand alone as a single sentence"
    assert LINE.count(".") == 1, "exactly one sentence, no extra periods"
    LINE.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
