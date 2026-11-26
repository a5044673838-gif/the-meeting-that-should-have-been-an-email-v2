"""Write the entry line for make.fun's "The Meeting That Should Have Been
an Email" bounty (replacement entry, v2).

Stdlib only, no network.
"""

import os

LINE = "After 47 minutes, nine people agreed the meeting should have been an email \u2014 then stayed twenty more minutes arguing over who would send it."


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    assert LINE.strip(), "entry must not be only whitespace"
    assert LINE.endswith("."), "entry must end with a full stop"
    text = LINE.strip()
    assert text == LINE, "entry must have no leading or trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
