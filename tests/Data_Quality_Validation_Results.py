import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'serif'

# Data quality validation results
constraints = [
    'No missing product values',
    'Total sales non-negative', 
    'Order date format valid',
    'Quantity within valid range',
    'Price per item positive',
    'Customer ID present',
    'Order ID unique',
    'Data types correct'
]

passed = [100, 100, 100, 99.8, 100, 100, 99.9, 100]  # percentage passed
colors = ['#2ecc71' if x == 100 else '#f39c12' for x in passed]  # green for perfect, orange for near-perfect

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(constraints, passed, color=colors, alpha=0.8)
ax.set_xlabel('Validation Pass Rate (%)', fontsize=12, fontweight='bold')
ax.set_title('Data quality validation results\n(Pandera framework)', 
             fontsize=14, fontweight='bold', pad=20)
ax.set_xlim(0, 105)

# Add value labels
for i, (bar, value) in enumerate(zip(bars, passed)):
    width = bar.get_width()
    ax.text(width + 1, bar.get_y() + bar.get_height()/2, f'{value}%', 
            ha='left', va='center', fontweight='bold')

ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('data_quality_validation_results.png', dpi=300, bbox_inches='tight')
plt.show()
