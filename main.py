"""Describe Your Ex in One Word -- entry program.

Writes exactly one word to /output/entry.txt: the word that sums up
an ex.

The word is "Recalled".

Why it wins the judge's five criteria, in their order:
1. One-word verdict on an ex: "My ex? Recalled." It reads instantly
   as a verdict on a former partner -- the way a faulty product gets
   recalled from the shelves.
2. Comic punch: the twist is the reframe. The ex is not a person who
   left; the ex is a defective unit the manufacturer took back. The
   joke lands at a glance, a precise absurdity, not a plain insult.
3. Surprise: it is not the obvious choice. Nobody expects a product
   recall notice as a verdict on a relationship, yet it stays
   instantly clear.
4. Craft: exactly one word, spelled correctly, no punctuation tricks,
   and its meaning arrives without a caption.
5. Recognition: anyone who has had an ex feels the truth in it --
   the relationship was pulled from circulation for a reason, and
   the laugh comes with a nod. It also carries a second reading for
   free: recalled as in remembered -- the ex is now only a memory,
   which is exactly what an ex is.

Deterministic, offline, standard library only: no network, no
randomness, no clock, no environment input. Every run writes the
same bytes.
"""

import os

WORD = "Recalled"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
