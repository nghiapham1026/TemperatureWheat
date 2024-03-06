import pandas as pd

# Load both datasets
wheat_data_path = '../data/filtered_wheat_data.csv'
temp_anomalies_path = '../data/temp_anomalies_EU.csv'

wheat_df = pd.read_csv(wheat_data_path)
temp_anomalies_df = pd.read_csv(temp_anomalies_path)

# Prepare the temperature anomalies dataset
# Convert 'Date' to datetime to extract the year, then calculate mean anomaly per year
temp_anomalies_df['Year'] = pd.to_datetime(temp_anomalies_df['Date'], format='%Y%m').dt.year
annual_temp_anomalies = temp_anomalies_df.groupby('Year')['Anomaly'].mean().reset_index()

# Prepare the wheat yield dataset if necessary (it seems ready based on your description)

# Merge the datasets on 'Year'
merged_df = pd.merge(wheat_df, annual_temp_anomalies, on='Year', how='inner')

# Optional: Filter for France and Germany if your analysis is focused on these countries
merged_france_germany_df = merged_df[merged_df['Area'].isin(['France', 'Germany'])]

# You might need to adjust the columns if necessary, depending on your analysis needs

# Save or display the merged dataset
print(merged_france_germany_df.head())

# Further analysis code here
output_path = '../data/crop_temp.csv'
merged_france_germany_df.to_csv(output_path, index=False)