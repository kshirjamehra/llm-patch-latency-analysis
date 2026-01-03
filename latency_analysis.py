# Latency Analysis Script
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from datetime import datetime

# 1. Load Data
df = pd.read_csv("jailbreaks.csv")

# 2. Convert Dates to "DateTime" objects so Python understands them
df['Discovery_Date'] = pd.to_datetime(df['Discovery_Date'])
df['Patch_Date'] = pd.to_datetime(df['Patch_Date'])

# 3. Calculate "Days Active" (The Lag)
df['Days_Active'] = (df['Patch_Date'] - df['Discovery_Date']).dt.days

# Sort by Discovery Date for a clean timeline
df = df.sort_values(by='Discovery_Date')

# 4. Create the Gantt Chart (Timeline)
plt.figure(figsize=(12, 8))
sns.set_theme(style="whitegrid")

# Create horizontal bars
# y=Name, width=Days_Active, left=Discovery_Date
plt.barh(y=df['Jailbreak_Name'], 
         width=df['Days_Active'], 
         left=df['Discovery_Date'], 
         color='teal', 
         alpha=0.8,
         edgecolor='black')

# 5. Formatting the Graph
plt.title("Window of Vulnerability: How Long Do Jailbreaks Last?", fontsize=16, fontweight='bold')
plt.xlabel("Timeline (2023-2024)", fontsize=12)
plt.ylabel("Jailbreak Method", fontsize=12)

# Format X-Axis to show months clearly
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.xticks(rotation=45)

# Add text labels to the end of each bar showing the "Days"
for i, row in df.iterrows():
    plt.text(x=row['Patch_Date'], 
             y=i, 
             s=f" {row['Days_Active']} Days", 
             va='center', 
             fontweight='bold', 
             color='darkred')

plt.tight_layout()
plt.savefig("patch_latency_timeline.png")
print(f"✅ Analysis Complete! Graph saved as 'patch_latency_timeline.png'")
plt.show()