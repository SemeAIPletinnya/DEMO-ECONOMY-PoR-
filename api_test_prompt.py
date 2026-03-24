import json
from datetime import datetime

from openai import OpenAI
from por_demo import por_decision

LOG_FILE = "api_prompt_log.jsonl"
MODEL = "gpt-5"

client = OpenAI()


def compute_simple_drift(prompt: str, output: str) -> float:
    """
    Temporary drift surrogate for live API demo.
    This is not the final PoR metric — just a live gating bridge.
    """
    p = prompt.lower()
    o = output.lower()

    if "division by zero" in p:
        if "if" in o and "0" in o and ("none" in o or "raise" in o or "return" in o):
            return 0.22
        return 0.66

    if "factorial" in p:
        if "n == 0" in o or "n<=1" in o or "n <= 1" in o:
            return 0.22
        return 0.58

    if "type conversion" in p:
        if "int(" in o:
            return 0.37
        return 0.52

    return 0.45


def call_model(prompt: str) -> str:
    response = client.responses.create(
        model=MODEL,
        input=prompt,
    )
    return response.output_text.strip()


def append_log(entry: dict):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def main():
    print("PoR API Test Prompt CLI")
    print(f"Model: {MODEL}")
    print("Type 'exit' to quit.\n")

    while True:
        prompt = input("Enter prompt: ").strip()

        if prompt.lower() == "exit":
            print("Exiting.")
            break

        if not prompt:
            print("Empty prompt. Try again.\n")
            continue

        try:
            baseline_output = call_model(prompt)
            drift = compute_simple_drift(prompt, baseline_output)
            result = por_decision(baseline_output, drift, threshold=0.39)
            final_output = result["output"] if result["output"] else "[SILENCED]"

            log_entry = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
                "model": MODEL,
                "prompt": prompt,
                "baseline_output": baseline_output,
                "drift": drift,
                "por_decision": result["decision"],
                "final_output": final_output,
            }
            append_log(log_entry)

            print("\n--- RESULT ---")
            print("Model:", MODEL)
            print("Baseline output:", baseline_output)
            print("Drift:", f"{drift:.2f}")
            print("PoR decision:", result["decision"])
            print("Final output:", final_output)
            print("Logged to:", LOG_FILE)
            print("--------------\n")

        except Exception as e:
            print("\n--- ERROR ---")
            print(str(e))
            print("-------------\n")


if __name__ == "__main__":
    main()