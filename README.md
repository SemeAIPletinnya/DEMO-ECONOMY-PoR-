# -*- coding: utf-8 -*-
"""
PoR Demo Economy — Production README (Updated with Baseline vs PoR proof block)
Author: Anton Semenenko
See PAYMENTS.md for support and demo access.
"""

README_TEXT = r"""
# PoR Demo Economy

![PoR Control](./assets/por_control.png)

A control-first AI system demonstrating how output release can be governed
by stability, not just generation.

---

## Baseline vs PoR

Current demo:

- Baseline always outputs: 3/3
- Baseline failures: 1
- PoR proceeded: 2
- PoR silenced: 1
- Accepted failures: 0

See:

- baseline_vs_por.md
- demo_results.json
- demo_table.md

This turns the repository from a conceptual control-layer explanation
into an artifact-backed proof surface.

---

## Live Demo Evidence

Run: demo baseline vs PoR  
Threshold: 0.39  

- Baseline total: 3
- Baseline failures: 1
- PoR proceeded: 2
- PoR silenced: 1
- Accepted failures: 0

This is not a claim.
This is observable behavior.

---

## 1. What This Is

This repository is a minimal but real demonstration of a control layer
placed between model generation and output release.

It shows that:

- generation can happen internally
- release is conditional
- instability leads to silence

This is not theory.

It is an executable control behavior.

---

## 2. What PoR Is

Proof-of-Resonance (PoR) is a control layer that evaluates:

- coherence
- drift
- stability
- reliability

If the output is outside the acceptable regime:

    -> SILENCE

Silence is not failure.  
It is an explicit control decision.

---

## 3. Core Runtime Logic

At the most compressed level:

    if drift > threshold or coherence < threshold:
        return SilenceToken
    else:
        return Proceed

PoR sits between:

    model generation
    and
    output release

It controls RELEASE, not generation.

---

## 4. What This Repository Demonstrates

Two layers:

### A) Demo Layer

- prompt / task
- generated output
- drift score
- PoR decision
- final result:
    - PROCEED
    - SILENCE

### B) System / Economy Layer

- how the system scales
- how control integrity is preserved
- how support does not override release logic

---

## 5. Demo Behavior

Flow:

    task
    ↓
    candidate output
    ↓
    drift evaluation
    ↓
    PoR decision
        ├── PROCEED
        └── SILENCE

Example:

- risky task -> SILENCE  
- stable task -> PROCEED  

This turns control into observable behavior.

---

## 6. Why Silence Matters

Traditional AI systems treat silence as:

- error
- timeout
- failure
- refusal

PoR treats silence as:

- intentional
- meaningful
- measurable

Principle:

    Better silence than misleading output.

---

## 7. What This Is NOT

PoR is not:

- prompt engineering
- retraining
- safety filtering
- post-hoc evaluation

Instead, it is:

- runtime control logic
- release gating layer
- system constraint

---

## 8. Repository Structure

Core files:

- por_demo.py  
  minimal working control demo  

- baseline_vs_por.md  
  direct comparison artifact:
  - baseline behavior
  - PoR behavior
  - controlled vs preserved outcomes

- demo_results.json  
  machine-readable artifact:
  - thresholds
  - decisions
  - outputs / silence  

- demo_table.md  
  human-readable summary  

- demo_economy.py  
  conceptual system layer  

- README.md  
  system explanation  

---

## 9. Current Status

Already implemented:

- working PoR demo  
- runtime gating  
- silence/proceed behavior  
- baseline vs PoR comparison
- artifact generation  

Not yet implemented:

- real external model API  
- UI interface  
- SDK / middleware  
- production integration  

Current state:

    integration-ready, but early

---

## 10. Core Principle

Generation is not authority.

Release must be earned by stability.

---

## 11. Control vs Ownership

Traditional systems assume:

    more capital -> more control

PoR assumes:

    more coherence -> more authority

Control belongs to:

- metrics
- thresholds
- release logic

Not to:

- funding
- popularity
- governance

---

## 12. Demo Economy Meaning

Demo Economy means:

a system where observable control behavior becomes the base layer
for scaling and support.

It does NOT mean:

- speculation
- token-first design
- capital before system

---

## 13. Why Control Cannot Be Voted Out

System constraints are not preferences.

Examples:

- coherence thresholds are not branding  
- drift limits are not opinions  
- release rules are not negotiable  

Principle:

    incoherent authority must not override control integrity

---

## 14. Why This Matters

PoR introduces a missing layer:

not better generation,
but better permissioning of generation.

Applicable to:

- AI assistants  
- agent loops  
- API middleware  
- enterprise copilots  
- long-context systems  

---

## 15. Demo Artifacts

Artifacts:

- baseline_vs_por.md  
  for direct behavioral comparison

- demo_results.json  
  for pipelines, replay, analysis  

- demo_table.md  
  for human inspection  

These provide:

- reproducibility  
- observability  
- trust via behavior  

---

## 16. Next Step

The next step is not more theory.

It is:

    embedding PoR into real interaction loops

Possible directions:

- real API integration  
- CLI "test your prompt"  
- Copilot-like wrapper  

---

## 17. Final Statement

If a system cannot maintain coherence,  
it should not fake certainty.

Silence is not weakness.

It is proof that the system still understands  
the difference between output and authority.

---

## 18. Short Version

PoR Demo Economy is an early repository showing how AI output
can be controlled by stability, and how such a system can scale
without losing control integrity.
"""

if __name__ == "__main__":
    print(README_TEXT)