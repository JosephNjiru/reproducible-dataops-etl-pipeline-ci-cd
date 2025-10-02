import matplotlib.pyplot as plt
import numpy as np

# Professional settings
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10

# Create the chart
fig, ax = plt.subplots(figsize=(12, 8))

# Your actual data from the paper
runs = ['Run 1', 'Run 2', 'Run 3', 'Run 4', 'Run 5']
test = [38, 36, 39, 37, 38]
build = [142, 138, 145, 140, 143]
push = [28, 26, 29, 27, 28]

x = np.arange(len(runs))
width = 0.25

# Create bars
bars1 = ax.bar(x - width, test, width, label='Test', color='blue', alpha=0.7)
bars2 = ax.bar(x, build, width, label='Build', color='green', alpha=0.7)
bars3 = ax.bar(x + width, push, width, label='Push', color='red', alpha=0.7)

# Add labels and styling
ax.set_xlabel('Workflow Run')
ax.set_ylabel('Duration (seconds)')
ax.set_title('CI/CD pipeline stage durations across five workflow runs\n(Average build time: 2.4 minutes)', fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(runs)
ax.legend()
ax.grid(True, alpha=0.3)

# Add value labels on bars
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('pipeline_chart_final.png', dpi=300, bbox_inches='tight')
plt.show()
