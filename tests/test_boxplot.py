import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'serif'

# Extended dataset (20 runs for meaningful boxplot)
runs_extended = 20
test_durations_extended = np.random.normal(38, 2, runs_extended)
build_durations_extended = np.random.normal(142, 4, runs_extended)
push_durations_extended = np.random.normal(28, 1.5, runs_extended)

data = [test_durations_extended, build_durations_extended, push_durations_extended]
labels = ['Test', 'Build', 'Push']

fig, ax = plt.subplots(figsize=(8, 6))

# Create boxplot
box_plot = ax.boxplot(data, labels=labels, patch_artist=True, 
                      boxprops=dict(facecolor='lightblue', alpha=0.7),
                      medianprops=dict(color='red', linewidth=2))

# Add individual data points
for i, d in enumerate(data):
    x = np.random.normal(i+1, 0.04, size=len(d))
    ax.scatter(x, d, alpha=0.6, color='navy', s=30)

ax.set_ylabel('Duration (seconds)', fontsize=12, fontweight='bold')
ax.set_title('Distribution of Pipeline Stage Durations Across 20 Runs', 
             fontsize=14, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)

# Add statistics table
stats_text = (f"Test: {np.mean(test_durations_extended):.1f}±{np.std(test_durations_extended):.1f}s\n"
              f"Build: {np.mean(build_durations_extended):.1f}±{np.std(build_durations_extended):.1f}s\n"
              f"Push: {np.mean(push_durations_extended):.1f}±{np.std(push_durations_extended):.1f}s")

ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, fontsize=10,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('pipeline_stage_durations_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()
