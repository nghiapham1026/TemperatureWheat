import pandas as pd

# Step 1: Read the CSV file
file_path = '../data/crop_yield_FRA_GER.csv'
df = pd.read_csv(file_path)

# Step 2: Filter the DataFrame to include only rows where the "Item" is "Wheat"
filtered_df = df[df['Item'] == 'Wheat']

# Optional Step 3: Save the filtered DataFrame to a new CSV file
output_path = '../data/filtered_wheat_data.csv'
filtered_df.to_csv(output_path, index=False)

print(f'Filtered DataFrame saved to {output_path}')
