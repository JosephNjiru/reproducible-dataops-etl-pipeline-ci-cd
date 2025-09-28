
import matplotlib.pyplot as plt
import numpy as np

# Example pipeline stage durations from 5 workflow runs
runs = np.arange(1, 6)
test = [0.25, 0.22, 0.24, 0.23, 0.25]  # seconds
build = [140, 138, 142, 139, 141]      # seconds (example)
push = [28, 30, 29, 27, 28]            # seconds (example)

bar_width = 0.25
plt.figure(figsize=(8, 5))

# Use more contrasting colors
plt.bar(runs - bar_width, test, width=bar_width, color='#1f77b4', label='Test')      # Blue
plt.bar(runs, build, width=bar_width, color='#d62728', label='Build')                # Red
plt.bar(runs + bar_width, push, width=bar_width, color='#ff7f0e', label='Push')      # Orange

# Add value labels on top of each bar
for i in range(len(runs)):
	plt.text(runs[i] - bar_width, test[i] + 2, f'{test[i]:.2f}', ha='center', va='bottom', fontsize=10, color='#1f77b4')
	plt.text(runs[i], build[i] + 2, f'{build[i]:.0f}', ha='center', va='bottom', fontsize=10, color='#d62728')
	plt.text(runs[i] + bar_width, push[i] + 2, f'{push[i]:.0f}', ha='center', va='bottom', fontsize=10, color='#ff7f0e')

plt.xlabel('Run Number', fontsize=12)
plt.ylabel('Duration (seconds)', fontsize=12)
plt.title('CI/CD Pipeline Stage Durations Across Five Runs', fontsize=14)
plt.xticks(runs)
plt.legend(loc='upper right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('pipeline_stage_durations_across_five_workflow_runs.png', dpi=300)
plt.show()
