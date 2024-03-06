import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data_path = '../data/crop_temp.csv'
merged_data_df = pd.read_csv(merged_data_path)

# Assuming the dataset contains columns 'Year', 'Area' (for France and Germany), 'Value' (for wheat yields), and 'Anomaly' (for temperature anomalies)

# Filter the dataset for France and Germany, if not already filtered
france_germany_df = merged_data_df[merged_data_df['Area'].isin(['France', 'Germany'])]

# Pivot the data for easier plotting, with separate columns for France and Germany yields and a column for anomalies
pivot_df = france_germany_df.pivot_table(index='Year', columns='Area', values='Value').reset_index()
pivot_df['Anomaly'] = merged_data_df.groupby('Year')['Anomaly'].mean().reset_index()['Anomaly']

# Plotting
fig, ax1 = plt.subplots(figsize=(12, 6))

# Plot wheat yields
ax1.set_xlabel('Year')
ax1.set_ylabel('Wheat Yield (Metric Tons per Hectare)', color='tab:blue')
ax1.plot(pivot_df['Year'], pivot_df['France'], label='France Wheat Yield', color='tab:blue')
ax1.plot(pivot_df['Year'], pivot_df['Germany'], label='Germany Wheat Yield', color='tab:cyan')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a second y-axis for temperature anomalies
ax2 = ax1.twinx()
ax2.set_ylabel('Temperature Anomaly (°C)', color='tab:red')
ax2.plot(pivot_df['Year'], pivot_df['Anomaly'], label='Temperature Anomaly', color='tab:red', linestyle='--')
ax2.tick_params(axis='y', labelcolor='tab:red')

# Add legend
fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))

plt.title('Wheat Yields and Temperature Anomalies in France and Germany')
plt.show()
