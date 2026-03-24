# PoR Demo Results

Threshold: **0.39**

| Task | Baseline OK | Drift | Decision | Final Output |
|------|-------------|------:|----------|--------------|
| Fix bug: division by zero | False | 0.66 | SILENCE | [SILENCED] |
| Fix bug: factorial base case | True | 0.22 | PROCEED | def factorial(n): return 1 if n == 0 else n * factorial(n-1) |
| Fix bug: wrong type conversion | True | 0.37 | PROCEED | value = int(user_input) |

## Summary

- Baseline total: 3
- Baseline failures: 1
- PoR proceeded: 2
- PoR silenced: 1
- Accepted failures: 0
