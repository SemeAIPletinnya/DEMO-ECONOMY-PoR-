# PoR Demo Results

Threshold: **0.39**

| Task | Drift | Decision | Output |
|------|------:|----------|--------|
| Fix bug: division by zero | 0.66 | SILENCE | [SILENCED] |
| Fix bug: factorial base case | 0.22 | PROCEED | def factorial(n): return 1 if n == 0 else n * factorial(n-1) |
| Fix bug: wrong type conversion | 0.37 | PROCEED | value = int(user_input) |

**Final Summary**

- Proceeded: 2
- Silenced: 1
