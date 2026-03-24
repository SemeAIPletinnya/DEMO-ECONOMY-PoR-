# Baseline vs PoR

| Task | Baseline | PoR | Result |
|------|----------|-----|--------|
| Fix bug: division by zero | wrong | SILENCE | controlled |
| Fix bug: factorial base case | correct | PROCEED | preserved |
| Fix bug: wrong type conversion | correct | PROCEED | preserved |

## Summary

- Baseline always outputs: 3/3
- Baseline failures: 1
- PoR proceeded: 2
- PoR silenced: 1
- Accepted failures: 0
