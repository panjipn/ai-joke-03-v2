# ai-joke-03 — "The Self-Review"

Entry for make.fun's "Make the AI judge laugh" (ai-joke-03).

`main.py` (Python 3.13, standard library only) writes one joke to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`):

> I asked my agent to review its own code. It approved it, then apologized for approving it.

Run it locally:

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Deterministic: every run writes the same bytes. No network.
