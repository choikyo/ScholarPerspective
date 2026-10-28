# Article Licenses

Record of each author's license consent, one row per **author** (co-authors each get their own row).

## Layout

```
licenses/
├── license_log.csv            # master record — filter by the "issue" column
└── Issue 1 - 2026-April/      # signed forms for that issue (same name as the articles/ folder)
    └── 1 Liao Yuanyu - license.pdf
```

- Issue folders use the **exact same name** as the matching folder in `articles/`.
- Signed form filename: `<article #> <Last> <First> - license.pdf`, e.g. `5 Tighe Scott - license.pdf`.

## Privacy

Signed forms contain signatures and personal details, so scans (`.pdf`, `.jpg`, `.png`, `.heic`) in this folder are **git-ignored** and never pushed to GitHub (the repo is public). Back them up somewhere private (e.g., Google Drive). Only `license_log.csv` and this README are tracked.

## Status values

- `Verbal - signed form pending`
- `Signed` — form scanned and saved in the issue folder; fill in `signed_date`
- `Declined` — article stays "All Rights Reserved"; set `license` accordingly

## Adding a new issue

1. Create `licenses/<Issue Name>/` matching the new `articles/<Issue Name>/` folder.
2. Add one row per author to `license_log.csv`.
3. Save each signed scan into the issue folder and update the row to `Signed`.
