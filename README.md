# PoR Demo Economy

![PoR Control](./assets/por_control.png)

A control-first AI system demonstrating how output release is governed by stability, not just generation.

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

This turns the repository from a conceptual explanation into an artifact-backed proof.

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

## Live API Demo

Run locally:

    python api_test_prompt.py

This demonstrates:

- real model output  
- drift evaluation  
- PoR decision  
- final release / silence  
- JSONL logging via `api_prompt_log.jsonl`  

---

## What This Is

This repository is a minimal but real demonstration of a control layer placed between model generation and output release.

It shows that:

- generation can happen internally  
- release is conditional  
- instability leads to silence  

This is not theory.  
This is executable control behavior.

---

## What PoR Is

Proof-of-Resonance (PoR) is a control layer that evaluates:

- coherence  
- drift  
- stability  
- reliability  

If the output is outside the acceptable regime:

    → SILENCE

Silence is not failure.  
It is an explicit control decision.

---

## Core Runtime Logic

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

## Demo Behavior

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

- risky task → SILENCE  
- stable task → PROCEED  

---

## Why Silence Matters

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

## What This Is NOT

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

## Repository Structure

Core files:

- por_demo.py — minimal working demo  
- baseline_vs_por.md — direct comparison  
- demo_results.json — machine-readable results  
- demo_table.md — human-readable summary  
- demo_economy.py — conceptual layer  
- api_test_prompt.py — live API demo  
- api_prompt_log.jsonl — logging  

---

## Current Status

Already implemented:

- PoR demo  
- runtime gating  
- baseline vs PoR comparison  
- live API test  
- logging  

Not yet implemented:

- UI  
- SDK  
- production integration  

Current state:

    integration-ready, early stage

---

## Core Principle

Generation is not authority.  

Release must be earned by stability.

---

## What This Shows

- baseline always speaks → can be wrong  
- PoR speaks only when stable  

→ zero accepted failures  

---

## Why This Matters

This is not better generation.  

This is control over generation.  

Applicable to:

- AI assistants  
- agent loops  
- API middleware  
- enterprise copilots  
- long-context systems  

---

## Next Step

Not more theory.

    → real integrations  
    → Copilot layer  
    → production API  

---

## Final Statement

If a system cannot maintain coherence,  
it should not fake certainty.

Silence is not weakness.  

It is proof of control.

---

## Short Version

PoR Demo Economy shows how AI output can be controlled by stability, not just generated — with measurable, reproducible behavior.