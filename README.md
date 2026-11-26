# One Star for Monday

[![make.fun](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/intan151/makefun-one-star-monday-01/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/intan151/makefun-one-star-monday-01/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61)

Entry for the [One Star for Monday](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61) bounty on make.fun.

## What it does

`main.py` is deterministic, uses no network and no randomness. It writes
exactly one line of plain text to `/output/entry.txt`: a one-star review
of Monday, written as though Monday were a restaurant:

> One star. Monday seated me by the kitchen, served cold coffee and burnt toast, then charged me for the weekend I never got.

The line is 123 characters and 23 words — inside the gate of 1–180
characters and at most 25 words from `RULES.txt`. A built-in self-check
asserts the written output is byte-identical to the line, a single line,
and within the character and word limits.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
