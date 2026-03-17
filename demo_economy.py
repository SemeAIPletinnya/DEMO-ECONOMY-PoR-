"""DEMO-ECONOMY-PoR: Proof-of-Resonance economy simulation.

This script demonstrates an economy where control emerges from resonance
(coherence + stability), not from capital concentration.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


# Fixed PoR equity map:
# - Founder Phase Anchor is the coherence source and is NOT for sale.
# - Other pools support participation and long-term stability.
EQUITY_DISTRIBUTION = {
    "Founder Phase Anchor": 51,
    "Investors": 21,
    "Core Team": 12,
    "Community Pool": 10,
    "Stability Pool": 6,
}


@dataclass(frozen=True)
class Agent:
    """Simple resonant actor with a base alignment strength."""

    name: str
    base_alignment: float


def por_gain(coherence: float, drift: float) -> float:
    """PoR-Gain metric in [0, 1].

    PoR-Gain is a compact measure of productive resonance:
    - higher coherence increases gain,
    - higher phase drift decreases gain.
    """

    gain = coherence * (1.0 - drift)
    return float(np.clip(gain, 0.0, 1.0))


def silence_as_control(coherence: float, drift: float) -> bool:
    """Silence-as-Control primitive.

    If resonance quality is unsafe (coherence < 0.7 OR drift > 0.3),
    all agent actions become "SILENCE".
    This prevents unstable control from propagating through the system.
    """

    return coherence < 0.7 or drift > 0.3


def simulate(days: int = 365, seed: int = 42) -> dict[str, np.ndarray]:
    """Run the DEMO-ECONOMY-PoR simulation for a fixed number of days."""

    rng = np.random.default_rng(seed)
    agents = [
        Agent("Founder", 0.95),
        Agent("Investors", 0.74),
        Agent("Team", 0.82),
        Agent("Community", 0.78),
    ]

    coherences = np.zeros(days)
    drifts = np.zeros(days)
    gains = np.zeros(days)
    silence_rates = np.zeros(days)

    for day in range(days):
        t = day / max(days - 1, 1)

        # Coherence follows a smooth baseline with low noise.
        coherence = 0.78 + 0.12 * math.sin(2 * math.pi * t * 3.0) + rng.normal(0, 0.03)
        coherence = float(np.clip(coherence, 0.0, 1.0))

        # Phase drift grows when coherence weakens, with bounded noise.
        drift = 0.18 + 0.20 * (1.0 - coherence) + rng.normal(0, 0.02)
        drift = float(np.clip(drift, 0.0, 1.0))

        gains[day] = por_gain(coherence, drift)
        coherences[day] = coherence
        drifts[day] = drift

        # Silence-as-Control applied per step for each agent.
        silenced = 0
        for agent in agents:
            _action = "SILENCE" if silence_as_control(coherence, drift) else f"ACT({agent.base_alignment:.2f})"
            if _action == "SILENCE":
                silenced += 1

        silence_rates[day] = (silenced / len(agents)) * 100.0

        if (day + 1) % 30 == 0 or day == 0 or day == days - 1:
            print(
                f"Day {day + 1:03d} | "
                f"PoR-Gain: {gains[day]:.2f} | "
                f"Coherence: {coherence:.2f} | "
                f"Drift: {drift:.2f} | "
                f"Silence: {silence_rates[day]:.0f}%"
            )

    return {
        "coherence": coherences,
        "drift": drifts,
        "gain": gains,
        "silence_rate": silence_rates,
    }


def print_summary(metrics: dict[str, np.ndarray]) -> None:
    """Print a concise summary table for key PoR metrics."""

    print("\nSummary Table")
    print("-" * 66)
    print(f"{'Metric':<20} {'Mean':>10} {'Min':>10} {'Max':>10} {'Final':>10}")
    print("-" * 66)

    rows = [
        ("PoR-Gain", metrics["gain"]),
        ("Coherence", metrics["coherence"]),
        ("Phase Drift", metrics["drift"]),
        ("Silence Rate (%)", metrics["silence_rate"]),
    ]

    for label, values in rows:
        print(
            f"{label:<20} "
            f"{np.mean(values):>10.3f} "
            f"{np.min(values):>10.3f} "
            f"{np.max(values):>10.3f} "
            f"{values[-1]:>10.3f}"
        )

    print("-" * 66)


def plot_equity_distribution() -> None:
    """Render the fixed PoR equity distribution pie chart.

    Phase Anchor concept:
    Founder allocation is treated as the coherence anchor of the system,
    not a speculative sale allocation.
    """

    labels = list(EQUITY_DISTRIBUTION.keys())
    sizes = list(EQUITY_DISTRIBUTION.values())
    explode = [0.05 if label == "Founder Phase Anchor" else 0.0 for label in labels]

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.0f%%",
        startangle=140,
        explode=explode,
        wedgeprops={"linewidth": 1, "edgecolor": "white"},
    )
    ax.set_title("PoR Equity Distribution — Control-First")
    ax.axis("equal")
    plt.tight_layout()
    plt.savefig("por_equity_distribution.png", dpi=150)


def main() -> None:
    metrics = simulate(days=365)
    print_summary(metrics)
    plot_equity_distribution()
    print("\n✅ DEMO-ECONOMY-PoR complete. Control = Coherence, not capital.")


if __name__ == "__main__":
    main()
