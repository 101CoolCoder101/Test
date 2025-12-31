# Creating pie chart for global device market share (November 2025)
import matplotlib.pyplot as plt

# Use 'seaborn-v0_8' style for clean aesthetics
plt.style.use('seaborn-v0_8')

# Data from Statcounter (November 2025)
labels = ['Mobile', 'Desktop', 'Tablet']
sizes = [51.56, 47.02, 1.42]
colors = ['#66c2a5', '#fc8d62', '#8da0cb']

# Create pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
ax.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle
plt.title('Global Device Market Share (November 2025)')

# Save the figure
output_path = '/mnt/data/global_device_market_share_nov2025.png'
plt.savefig(output_path)

print("Created pie chart showing global device market share (November 2025) and saved as global_device_market_share_nov2025.png")
