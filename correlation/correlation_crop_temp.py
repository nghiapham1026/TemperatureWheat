import pandas as pd

# Load the merged dataset
merged_data_path = '../data/crop_temp.csv'
merged_data_df = pd.read_csv(merged_data_path)

# Assuming the dataset contains columns like 'Year', 'Area' (for France and Germany), 'Value' (wheat yields), and 'Anomaly' (temperature anomalies)
# and that the data might need filtering to focus on the wheat yields and temperature anomalies

# Pivot the dataset to have one row per year, columns for France and Germany yields, and a column for temperature anomalies
# This is necessary if the dataset has one row per country per year
pivot_df = merged_data_df.pivot_table(index='Year', columns='Area', values='Value').reset_index()
pivot_df['Anomaly'] = merged_data_df.groupby('Year')['Anomaly'].mean().values  # assuming anomaly data is duplicated for both countries

# Now, calculate the correlation
# First, calculate correlations between France's yields and anomalies
france_correlation = pivot_df[['France', 'Anomaly']].corr().iloc[0, 1]

# Then, calculate correlations between Germany's yields and anomalies
germany_correlation = pivot_df[['Germany', 'Anomaly']].corr().iloc[0, 1]

print(f"Correlation between wheat yields in France and temperature anomalies: {france_correlation}")
print(f"Correlation between wheat yields in Germany and temperature anomalies: {germany_correlation}")
