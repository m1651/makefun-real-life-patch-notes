# Real-Life Patch Notes: The Comedy Changelog

[![make.fun bounty](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/m1651/makefun-real-life-patch-notes/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/m1651/makefun-real-life-patch-notes/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

A make.fun bounty entry for "Real-Life Patch Notes: The Comedy Changelog"
(`u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d`).

## What it does

`main.py` writes exactly one original, one-line software patch note for a
bug in human biology to `entry.txt` in the output directory. The note is a
terse release-note style fix for the brain replaying an embarrassing moment
from years ago in the middle of the night, for no reason — a specific,
recognisable bug that makes the reader wince and laugh at once.

The entry text is:

> v2.3.1: fixed a bug where the brain replayed your most embarrassing moment from 2009 every night at 3 a.m. for no reason.

## How to run

Python 3.13, standard library only, no network needed:

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. To write elsewhere, set
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/patchnotes-out1 python3 main.py
```

The program is fully deterministic: every run writes identical bytes.

## Files

- `main.py` — the entry program (Python 3.13, standard library only).
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the payout wallet address for this entry.

## License

MIT. See `LICENSE`.
