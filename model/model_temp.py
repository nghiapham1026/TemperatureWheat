import matplotlib.pyplot as plt
import pandas as pd

df_new = pd.read_csv('../data/temp_anomalies_EU.csv')

# Convert 'Date' column to datetime format for better plotting
df_new['Date'] = pd.to_datetime(df_new['Date'], format='%Y%m')

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df_new['Date'], df_new['Anomaly'], label='Temperature Anomaly', color='blue')
plt.title('Temperature Anomalies in Europe Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature Anomaly (°C)')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()