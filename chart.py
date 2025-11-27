import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for customer purchase amounts by segment
segments = []
purchase_amounts = []

# Premium segment: Higher spending, less variance
for _ in range(150):
    segments.append('Premium')
    purchase_amounts.append(np.random.normal(250, 45))

# Standard segment: Moderate spending
for _ in range(200):
    segments.append('Standard')
    purchase_amounts.append(np.random.normal(150, 35))

# Budget segment: Lower spending, wider variance
for _ in range(180):
    segments.append('Budget')
    purchase_amounts.append(np.random.normal(80, 30))

# Value segment: Very low spending
for _ in range(120):
    segments.append('Value')
    purchase_amounts.append(np.random.normal(45, 20))

# Create DataFrame
df = pd.DataFrame({
    'Customer Segment': segments,
    'Purchase Amount ($)': purchase_amounts
})

# Ensure no negative values
df['Purchase Amount ($)'] = df['Purchase Amount ($)'].clip(lower=0)

# Set style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with 8x8 inch size for 512x512 at 64 DPI
plt.figure(figsize=(8, 8))

# Create boxplot with professional styling
sns.boxplot(
    data=df,
    x='Customer Segment',
    y='Purchase Amount ($)',
    palette='Set2',
    linewidth=2,
    order=['Premium', 'Standard', 'Budget', 'Value']
)

# Add title and labels
plt.title('Purchase Amount Distribution by Customer Segment', 
          fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Customer Segment', fontsize=13, fontweight='bold')
plt.ylabel('Purchase Amount ($)', fontsize=13, fontweight='bold')

# Improve layout
plt.tight_layout()

# Save chart as PNG with exactly 512x512 pixels (8 inches * 64 dpi = 512 pixels)
plt.savefig('chart.png', dpi=64)
plt.close()

# Verify and force resize to exactly 512x512 if needed
img = Image.open('chart.png')
if img.size != (512, 512):
    img = img.resize((512, 512), Image.LANCZOS)
    img.save('chart.png')

print("Chart successfully generated: chart.png (512x512 pixels)")
