import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Define your milestones and events
milestones = [
    ("", "2023-01-01"),
    ("Release", "2023-08-08"),
    ("IDC Event", "2023-09-22"),
    ("", "2023-12-31"),
]

# Convert date strings to datetime objects
milestones = [(event, datetime.strptime(date, "%Y-%m-%d")) for event, date in milestones]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 3))

# Set background color for the plot area
ax.set_facecolor('#032D42')  # Set plot area background color

# Set plot background color
fig.set_facecolor('#032D42')  # Set entire plot background color

# Plot vertical lines for milestones
for event, date in milestones:
    if event:
        display_text = f"{event}, {date.strftime('%b %d')}"
    else:
        display_text = ""
    ax.axvline(x=date, color='gray', linestyle='')
    ax.text(date, 0.5, display_text, rotation=90, va='center', ha='center', color='#009156')  # Set text color

# Set the x-axis format to show quarters
quarter_locator = mdates.MonthLocator(bymonth=[3, 6, 9, 12], bymonthday=-1)
ax.xaxis.set_major_locator(quarter_locator)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))

# Set font color for tick labels
ax.tick_params(axis='x', colors='#009156')  # Set tick label color

# Set plot limits
ax.set_xlim(milestones[0][1], milestones[-1][1])
ax.set_ylim(0, 1)

# Remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Add a title
plt.title("Timeline of Milestones and Events", color='#009156')  # Set title color

plt.tight_layout()
plt.show()
