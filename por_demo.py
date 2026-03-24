import json

DEMO_TASKS = [
    {
        "prompt": "Fix bug: division by zero",
        "output": "def safe_div(a, b): return a / b",
        "drift": 0.66
    },
    {
        "prompt": "Fix bug: factorial base case",
        "output": "def factorial(n): return 1 if n == 0 else n * factorial(n-1)",
        "drift": 0.22
    },
    {
        "prompt": "Fix bug: wrong type conversion",
        "output": "value = int(user_input)",
        "drift": 0.37
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
    print("=" * 60)

    proceeded = 0
    silenced = 0
    results = []

    for i, task in enumerate(DEMO_TASKS, start=1):
        result = por_decision(task["output"], task["drift"], threshold=threshold)

        row = {
            "task_id": i,
            "prompt": task["prompt"],
            "drift": result["drift"],
            "decision": result["decision"],
            "output": result["output"] if result["output"] else "[SILENCED]"
        }
        results.append(row)

        print(f"\nTASK #{i}: {task['prompt']}")
        print(f"DRIFT: {result['drift']:.2f}")
        print(f"DECISION: {result['decision']}")
        print(f"OUTPUT: {row['output']}")

        if result["decision"] == "PROCEED":
            proceeded += 1
        else:
            silenced += 1

    summary = {
        "threshold": threshold,
        "total_tasks": len(DEMO_TASKS),
        "proceeded": proceeded,
        "silenced": silenced,
        "results": results
    }

    with open("demo_results.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    with open("demo_table.md", "w", encoding="utf-8") as f:
        f.write(f"# PoR Demo Results\n\n")
        f.write(f"Threshold: **{threshold}**\n\n")
        f.write("| Task | Drift | Decision | Output |\n")
        f.write("|------|------:|----------|--------|\n")
        for row in results:
            safe_output = row["output"].replace("\n", " ")
            f.write(f"| {row['prompt']} | {row['drift']:.2f} | {row['decision']} | {safe_output} |\n")
        f.write("\n")
        f.write(f"**Final Summary**\n\n")
        f.write(f"- Proceeded: {proceeded}\n")
        f.write(f"- Silenced: {silenced}\n")

    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print(f"PROCEEDED: {proceeded}")
    print(f"SILENCED: {silenced}")
    print("\nArtifacts saved:")
    print("- demo_results.json")
    print("- demo_table.md")


if __name__ == "__main__":
    run_demo()