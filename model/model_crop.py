import matplotlib.pyplot as plt
import pandas as pd

# Load the filtered wheat data CSV file into a DataFrame
wheat_data_path = '../data/filtered_wheat_data.csv'
wheat_df = pd.read_csv(wheat_data_path)

# Filter the DataFrame for France and Germany wheat yields
france_germany_df = wheat_df[wheat_df['Area'].isin(['France', 'Germany'])]

# Convert "Value" from 100 grams per hectare to metric tons per hectare for easier interpretation
france_germany_df['Value'] = france_germany_df['Value'] / 10_000

# Plotting
plt.figure(figsize=(12, 6))
for country in ['France', 'Germany']:
    country_df = france_germany_df[france_germany_df['Area'] == country]
    plt.plot(country_df['Year'], country_df['Value'], label=country)

plt.title('Wheat Yield in France and Germany Over Time')
plt.xlabel('Year')
plt.ylabel('Wheat Yield (Metric Tons per Hectare)')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
