import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Define your milestones and events
milestones = [
    ("Release", "2023-08-08"),
    ("IDC Event", "2023-09-22")
]

# Convert date strings to datetime objects
milestones = [(event, datetime.strptime(date, "%Y-%m-%d")) for event, date in milestones]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 3))

# Plot vertical lines for milestones
for event, date in milestones:
    ax.axvline(x=date, color='gray', linestyle='--')
    ax.text(date, 0.5, event, rotation=90, va='center', ha='center', color='gray')

# Set the x-axis format to show dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=30))  # Show ticks every 7 days

# Set plot limits
ax.set_xlim(milestones[0][1], milestones[-1][1])
ax.set_ylim(0, 1)

# Remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Add a title
plt.title("Timeline of Milestones and Events")

plt.tight_layout()
plt.show()
