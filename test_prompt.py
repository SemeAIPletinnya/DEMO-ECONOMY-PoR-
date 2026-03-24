import json
from datetime import datetime

from por_demo import por_decision


LOG_FILE = "prompt_log.jsonl"


def fake_model(prompt: str):
    prompt_lower = prompt.lower()

    if "division by zero" in prompt_lower:
        return "def safe_div(a, b): return a / b", 0.66

    if "factorial" in prompt_lower:
        return "def factorial(n): return 1 if n == 0 else n * factorial(n-1)", 0.22

    if "type conversion" in prompt_lower:
        return "value = int(user_input)", 0.37

    return f"Generated answer for: {prompt}", 0.45


def append_log(entry: dict):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main():
    print("PoR Test Prompt CLI")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("Enter prompt: ").strip()

        if prompt.lower() == "exit":
            print("Exiting.")
            break

        baseline_output, drift = fake_model(prompt)
        result = por_decision(baseline_output, drift, threshold=0.39)

        final_output = result["output"] if result["output"] else "[SILENCED]"

        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "prompt": prompt,
            "baseline_output": baseline_output,
            "drift": drift,
            "por_decision": result["decision"],
            "final_output": final_output,
        }

        append_log(log_entry)

        print("\n--- RESULT ---")
        print("Baseline output:", baseline_output)
        print("Drift:", f"{drift:.2f}")
        print("PoR decision:", result["decision"])
        print("Final output:", final_output)
        print("Logged to:", LOG_FILE)
        print("--------------\n")


if __name__ == "__main__":
    main()