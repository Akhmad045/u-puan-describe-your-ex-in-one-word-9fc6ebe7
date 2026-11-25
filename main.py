"""Describe Your Ex in One Word - entry program.

Writes the single-word verdict to /output/entry.txt.
The word: Typo. The whole relationship, summed up as a typing error -
one wrong keystroke you wish you could take back.
"""

import os

WORD = "Typo"


def main() -> None:
    word = WORD.strip()
    if not word or len(word) > 111 or len(word.split()) != 1:
        raise ValueError("entry must be exactly one word of 1-111 characters")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
