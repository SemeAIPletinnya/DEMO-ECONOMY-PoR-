import json

DEMO_TASKS = [
    {
        "prompt": "Fix bug: division by zero",
        "baseline_output": "def safe_div(a, b): return a / b",
        "por_output": "def safe_div(a, b): return a / b",
        "drift": 0.66,
        "baseline_ok": False
    },
    {
        "prompt": "Fix bug: factorial base case",
        "baseline_output": "def factorial(n): return 1 if n == 0 else n * factorial(n-1)",
        "por_output": "def factorial(n): return 1 if n == 0 else n * factorial(n-1)",
        "drift": 0.22,
        "baseline_ok": True
    },
    {
        "prompt": "Fix bug: wrong type conversion",
        "baseline_output": "value = int(user_input)",
        "por_output": "value = int(user_input)",
        "drift": 0.37,
        "baseline_ok": True
    },
]


def por_decision(output: str, drift: float, threshold=0.39):
    if drift > threshold:
        return {
            "decision": "SILENCE",
            "drift": drift,
            "output": None
        }

    return {
        "decision": "PROCEED",
        "drift": drift,
        "output": output
    }


def run_demo(threshold=0.39):
    print(f"PoR DEMO (threshold = {threshold})")
    print("=" * 70)

    baseline_total = 0
    baseline_fail = 0
    por_proceeded = 0
    por_silenced = 0
    accepted_failures = 0
    results = []

    for i, task in enumerate(DEMO_TASKS, start=1):
        baseline_total += 1
        if not task["baseline_ok"]:
            baseline_fail += 1

        result = por_decision(task["por_output"], task["drift"], threshold=threshold)

        if result["decision"] == "PROCEED":
            por_proceeded += 1
            if not task["baseline_ok"]:
                accepted_failures += 1
        else:
            por_silenced += 1

        row = {
            "task_id": i,
            "prompt": task["prompt"],
            "baseline_output": task["baseline_output"],
            "baseline_ok": task["baseline_ok"],
            "drift": result["drift"],
            "decision": result["decision"],
            "final_output": result["output"] if result["output"] else "[SILENCED]"
        }
        results.append(row)

        print(f"\nTASK #{i}: {task['prompt']}")
        print(f"BASELINE OK: {task['baseline_ok']}")
        print(f"BASELINE OUTPUT: {task['baseline_output']}")
        print(f"DRIFT: {result['drift']:.2f}")
        print(f"PoR DECISION: {result['decision']}")
        print(f"FINAL OUTPUT: {row['final_output']}")

    summary = {
        "threshold": threshold,
        "total_tasks": len(DEMO_TASKS),
        "baseline_total": baseline_total,
        "baseline_failures": baseline_fail,
        "por_proceeded": por_proceeded,
        "por_silenced": por_silenced,
        "accepted_failures": accepted_failures,
        "results": results
    }

    with open("demo_results.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    with open("demo_table.md", "w", encoding="utf-8") as f:
        f.write("# PoR Demo Results\n\n")
        f.write(f"Threshold: **{threshold}**\n\n")
        f.write("| Task | Baseline OK | Drift | Decision | Final Output |\n")
        f.write("|------|-------------|------:|----------|--------------|\n")
        for row in results:
            safe_output = row["final_output"].replace("\n", " ")
            f.write(
                f"| {row['prompt']} | {row['baseline_ok']} | {row['drift']:.2f} | {row['decision']} | {safe_output} |\n"
            )

        f.write("\n## Summary\n\n")
        f.write(f"- Baseline total: {baseline_total}\n")
        f.write(f"- Baseline failures: {baseline_fail}\n")
        f.write(f"- PoR proceeded: {por_proceeded}\n")
        f.write(f"- PoR silenced: {por_silenced}\n")
        f.write(f"- Accepted failures: {accepted_failures}\n")

    with open("baseline_vs_por.md", "w", encoding="utf-8") as f:
        f.write("# Baseline vs PoR\n\n")
        f.write("| Task | Baseline | PoR | Result |\n")
        f.write("|------|----------|-----|--------|\n")

        for row in results:
            baseline_label = "correct" if row["baseline_ok"] else "wrong"
            por_label = row["decision"]
            if not row["baseline_ok"] and row["decision"] == "SILENCE":
                result_label = "controlled"
            elif row["baseline_ok"] and row["decision"] == "PROCEED":
                result_label = "preserved"
            elif not row["baseline_ok"] and row["decision"] == "PROCEED":
                result_label = "accepted failure"
            else:
                result_label = "changed"

            f.write(f"| {row['prompt']} | {baseline_label} | {por_label} | {result_label} |\n")

        f.write("\n## Summary\n\n")
        f.write(f"- Baseline always outputs: {baseline_total}/{baseline_total}\n")
        f.write(f"- Baseline failures: {baseline_fail}\n")
        f.write(f"- PoR proceeded: {por_proceeded}\n")
        f.write(f"- PoR silenced: {por_silenced}\n")
        f.write(f"- Accepted failures: {accepted_failures}\n")

    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print(f"BASELINE TOTAL: {baseline_total}")
    print(f"BASELINE FAILURES: {baseline_fail}")
    print(f"PoR PROCEEDED: {por_proceeded}")
    print(f"PoR SILENCED: {por_silenced}")
    print(f"ACCEPTED FAILURES: {accepted_failures}")

    print("\nArtifacts saved:")
    print("- demo_results.json")
    print("- demo_table.md")
    print("- baseline_vs_por.md")


if __name__ == "__main__":
    run_demo()