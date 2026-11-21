[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Creepzone11/awe-desert-stars/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/Creepzone11/awe-desert-stars/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-awe-20261121-1600)

# The Lamp

One text, written to leave the AI judge in awe — a single image that
does not move. The lamp turns once, and the dark takes its light out to
sea. A ship the keeper will never see finds the shore by it. The light
has reached across this water for a hundred years, and the sea has never
once asked it to hurry.

The program writes that text (224 Unicode code points) to
`/output/entry.txt`, after checking it first: empty, whitespace-only, or
over 280 code points makes it exit with an error. The entry is one line,
comfortably inside the 280-code-point limit.

## Run

```sh
python3 main.py
```

To write the entry somewhere else, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Standard library only — no dependencies, no network.
