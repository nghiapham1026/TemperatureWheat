import pandas as pd
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data_path = '../data/crop_temp.csv'
merged_data_df = pd.read_csv(merged_data_path)

# Pivot the dataset to have one row per year, columns for France and Germany yields, and a column for temperature anomalies
pivot_df = merged_data_df.pivot_table(index='Year', columns='Area', values='Value').reset_index()
pivot_df['Anomaly'] = merged_data_df.groupby('Year')['Anomaly'].mean().values  # assuming anomaly data is duplicated for both countries

# Calculate the correlation
france_correlation = pivot_df[['France', 'Anomaly']].corr().iloc[0, 1]
germany_correlation = pivot_df[['Germany', 'Anomaly']].corr().iloc[0, 1]

# Visualize the correlation with scatter plots
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# France
axes[0].scatter(pivot_df['Anomaly'], pivot_df['France'], color='blue', alpha=0.5)
axes[0].set_title(f'France Wheat Yield vs. Temperature Anomaly\nCorrelation: {france_correlation:.2f}')
axes[0].set_xlabel('Temperature Anomaly (°C)')
axes[0].set_ylabel('Wheat Yield (Metric Tons per Hectare)')

# Germany
axes[1].scatter(pivot_df['Anomaly'], pivot_df['Germany'], color='green', alpha=0.5)
axes[1].set_title(f'Germany Wheat Yield vs. Temperature Anomaly\nCorrelation: {germany_correlation:.2f}')
axes[1].set_xlabel('Temperature Anomaly (°C)')
# axes[1].set_ylabel('Wheat Yield (Metric Tons per Hectare)')  # Y-axis label is shared

plt.tight_layout()
plt.show()
