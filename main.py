"""ai-joke-03 entry (Python 3.13, standard library only).

Writes one fixed joke, a one-liner about AI coding agents, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the
grader's container). Deterministic: the same bytes every run.
No network, no randomness, no trailing newline.
"""

import os

JOKE = "I asked my agent to review its own code. It approved it, then apologized for approving it."

# 90 Unicode code points, inside the 1-280 gate; at least one non-space char.
assert 1 <= len(JOKE) <= 280 and JOKE.strip()

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(JOKE)
