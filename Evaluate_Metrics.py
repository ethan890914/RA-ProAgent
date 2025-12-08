import os
import json
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np

# Only plot these two keys
PLOT_KEYS = ["tool_call_id", "construction_time(sec)"]


def load_values(root_folder, keys):
    """
    Load meta.meta values for IDs 1–40.
    Folder names may be: ID_38, ID_38-1, ID_38-extra, etc.
    """
    values = {k: [] for k in keys}
    ids = list(range(1, 41))

    for i in ids:
        # match folders starting with ID_i
        matches = [
            name for name in os.listdir(root_folder)
            if name.startswith(f"ID_{i}")
        ]

        if not matches:
            for k in keys:
                values[k].append(None)
            continue

        folder = os.path.join(root_folder, matches[0])
        meta_file = os.path.join(folder, "meta.meta")

        if not os.path.exists(meta_file):
            for k in keys:
                values[k].append(None)
            continue

        with open(meta_file, "r") as f:
            data = json.load(f)

        for k in keys:
            values[k].append(data.get(k, None))

    return ids, values


def average(values_list):
    """Compute average ignoring None."""
    nums = [v for v in values_list if v is not None]
    return sum(nums) / len(nums) if nums else 0


def plot_two_subfigures(baseline_folder, rarefine_folder):
    # Load values
    ids, baseline_vals = load_values(baseline_folder, PLOT_KEYS)
    _, rarefine_vals = load_values(rarefine_folder, PLOT_KEYS)

    x = np.arange(len(ids))  # 0..39
    width = 0.4

    fig, axes = plt.subplots(2, 1, figsize=(14, 18))

    for ax, key in zip(axes, PLOT_KEYS):

        # Compute averages
        baseline_avg = average(baseline_vals[key])
        rarefine_avg = average(rarefine_vals[key])

        # Plot bar chart
        ax.bar(x - width/2, baseline_vals[key], width, label=f"Baseline (avg={baseline_avg:.2f})")
        ax.bar(x + width/2, rarefine_vals[key],  width, label=f"ProAgent (avg={rarefine_avg:.2f})")

        if key == "tool_call_id":
            ax.set_title(f"number of rounds\nBaseline Avg={baseline_avg:.2f} | RA-ProAgent Avg={rarefine_avg:.2f}", fontsize=14)
        else:
            ax.set_title(f"{key}\nBaseline Avg={baseline_avg:.2f} | ProAgent Avg={rarefine_avg:.2f}", fontsize=14)
        ax.set_xlabel("ID (1–40)")
        ax.set_ylabel(key)
        ax.set_xticks(x, ids)
        ax.grid(axis="y", alpha=0.4)
        ax.legend()

    plt.tight_layout()

    # Save PNG
    output_path = "comparison.png"
    plt.savefig(output_path, dpi=200)
    print(f"Saved figure to: {output_path}")

    plt.show()


if __name__ == "__main__":
    baseline_path = "./apa_case_storage/Development_unseen"
    rarefine_path = "./apa_case_storage/RARefine_evaluation"

    plot_two_subfigures(baseline_path, rarefine_path)
