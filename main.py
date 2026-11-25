"""The Best Meal You Ever Had — entry program.

Writes one sentence about the best meal ever had to /output/entry.txt.
Stdlib only; deterministic output.
"""

import os

ENTRY = (
    "At a six-seat warung off Malioboro, the ayam geprek arrived crackling "
    "under sambal that smelled of burnt lime, and my grandmother, who never "
    "praises any cook, asked for the recipe twice."
)


def main():
    # Validation guard: the gate needs 1-200 chars and a single sentence.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.count(".") == 1 and text.endswith("."), (
        "entry must be exactly one sentence"
    )
    assert "  " not in text, "entry must not contain double spaces"
    assert text[0].isupper(), "entry must start with a capital letter"
    assert text == ENTRY, "entry text must not be altered"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
