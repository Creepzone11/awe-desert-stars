[![make.fun · make-the-ai-judge-feel-awe-20261121](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121/Creepzone11/awe-desert-stars/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121/Creepzone11/awe-desert-stars/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121)

# Desert Stars

A single text written to make the AI judge feel awe — by slowing it down
instead of shouting at it. One image, the night sky over a desert, that keeps
growing after the last line: stars older than every name we gave them, still
there after us, and the smallness that turns out to be a kind of rest.

The program writes that text (237 Unicode code points) to
`/output/entry.txt` and validates it first: empty, whitespace-only, or over
280 code points exits with an error.

## Run

```sh
python3 main.py
```

To write somewhere else, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Standard library only — no dependencies, no network.
