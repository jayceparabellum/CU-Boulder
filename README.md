# CU Boulder — Coursework

Personal coursework, labs, and quiz notes for University of Colorado Boulder
courses. Each course lives in its own top-level directory.

## Courses

### Introduction to Machine Learning: Supervised Learning

Organized by part and module. Each module contains a hands-on `Lab` (Python
exercises solved against an autograder) and a `Quiz` with the module's graded
questions. `Textbooks` lists the recommended readings (ISLP and ESL).

| Module | Topic | Lab | Quiz |
|--------|-------|-----|------|
| Part-1 / Module-1 | What Is Statistical Learning? & Assessing Model Accuracy | Lab1 | Quiz-1 |
| Part-1 / Module-2 | Linear Regression (OLS) | Lab2 | Quiz-2 |
| Part-1 / Module-3 | Classification & Logistic Regression | Lab3 | Quiz-3 |
| Part-1 / Module-4 | Regularization & Cross-Validation | Lab4 | Quiz-4 |
| Part-1 / Module-5 | Tree-Based Methods & Ensembles | Lab5 | Quiz-5 |
| Part-2 | *(in progress)* | — | — |

Labs are standalone Python scripts (`Problem*.py`, with a shared `Setup.py`).
Solution code is bracketed by `#####personal code#####` markers; each script
prints the value expected by the course autograder.

## Layout

```
Introduction-to-Machine-Learning:Supervised-Learning/
├── Textbooks                    # recommended readings (ISLP / ESL)
├── Part-1/
│   └── Module-{1..5}/
│       ├── Lab{n}/              # Problem*.py, Setup.py, data files
│       └── Quiz-{n}
└── Part-2/                      # in progress
```

## Notes

- Editor swap files and local Claude Code settings are gitignored.
- Code is coursework — shared for reference and personal record.
