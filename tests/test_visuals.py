import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Set publication-quality style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 11

# Pipeline stage durations from 5 workflow runs (realistic data)
runs = ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5']
test_durations = [38, 36, 39, 37, 38]        # seconds
build_durations = [142, 138, 145, 140, 143]  # seconds (~2.3 minutes average)
push_durations = [28, 26, 29, 27, 28]        # seconds

x = np.arange(len(runs))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))

# Create bars with professional colors
bars1 = ax.bar(x - width, test_durations, width, label='Test', color='#3498db', alpha=0.9)
bars2 = ax.bar(x, build_durations, width, label='Build', color='#2ecc71', alpha=0.9)
bars3 = ax.bar(x + width, push_durations, width, label='Push', color='#e74c3c', alpha=0.9)

# Add value labels on bars
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=10, fontweight='bold')

add_value_labels(bars1)
add_value_labels(bars2)
add_value_labels(bars3)

# Customize the chart
ax.set_xlabel('Workflow Run', fontsize=12, fontweight='bold')
ax.set_ylabel('Duration (seconds)', fontsize=12, fontweight='bold')
ax.set_title('CI/CD Pipeline Stage Durations Across Five Workflow Runs\n(Average Build Time: ~2.3 minutes)', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(runs)
ax.legend(loc='upper right', frameon=True, fancybox=True, shadow=True)

# Add grid and styling
ax.grid(True, alpha=0.3)
ax.set_axisbelow(True)

# Set y-axis to show reasonable range
ax.set_ylim(0, 160)

# Add some statistics as text
avg_build = np.mean(build_durations)
std_build = np.std(build_durations)
ax.text(0.02, 0.98, f'Build Stage Stats:\nMean: {avg_build:.1f}s | Std: {std_build:.1f}s', 
        transform=ax.transAxes, fontsize=10, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('pipeline_stage_durations_across_five_workflow_runs.png', 
            dpi=300, bbox_inches='tight', facecolor='white')
# plt.show()  # Disabled for headless test environments

# Print summary statistics
print(f"Average durations across 5 runs:")
print(f"Test: {np.mean(test_durations):.1f} ± {np.std(test_durations):.1f} seconds")
print(f"Build: {np.mean(build_durations):.1f} ± {np.std(build_durations):.1f} seconds (~{np.mean(build_durations)/60:.1f} minutes)")
print(f"Push: {np.mean(push_durations):.1f} ± {np.std(push_durations):.1f} seconds")
