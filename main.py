#!/usr/bin/env python3
"""Office Joke Open: write one line of office comedy to /output/entry.txt.

The joke is a single line, under 200 characters, about office life.
"""

import os

JOKE = (
    "I hit reply-all to ask everyone to stop hitting reply-all, "
    "and now HR wants a meeting about my tone."
)


def main() -> None:
    # The gate refuses anything over 200 characters, so fail loudly here
    # instead of shipping an entry the judge never sees.
    assert 1 <= len(JOKE) <= 200, f"joke is {len(JOKE)} characters"
    assert JOKE.strip() == JOKE and "\n" not in JOKE, "joke must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
