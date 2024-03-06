import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import ccf
import matplotlib.pyplot as plt

# Load the dataset
file_path = '../data/crop_temp.csv'
data = pd.read_csv(file_path)

# Assuming 'data' is your DataFrame loaded previously
data_france = data[data['Area'] == 'France'].copy()
data_france['Year'] = pd.to_datetime(data_france['Year'], format='%Y')
data_france.set_index('Year', inplace=True)

# Select the columns for yield and temperature anomalies for easier access
yield_france = data_france['Value']  # Assuming 'Value' represents the wheat yield
anomaly_france = data_france['Anomaly']  # Assuming 'Anomaly' represents the temperature anomaly

yield_france = (yield_france - yield_france.mean()) / yield_france.std()
anomaly_france = (anomaly_france - anomaly_france.mean()) / anomaly_france.std()

# Adjusted for deprecated 'unbiased' warning
ccf_values = ccf(anomaly_france, yield_france, adjusted=True)

# Decompose the wheat yield time series
yield_decompose = seasonal_decompose(yield_france, model='additive')
temperature_decompose = seasonal_decompose(anomaly_france, model='additive')

# Plot decomposition results for wheat yield
yield_decompose.plot()
plt.title('Decomposition of Wheat Yield Time Series in France')
plt.show()

# Plot decomposition results for temperature anomaly
temperature_decompose.plot()
plt.title('Decomposition of Temperature Anomaly Time Series in France')
plt.show()

plt.figure(figsize=(10, 6))
plt.stem(range(len(ccf_values)), ccf_values)
plt.title('Cross-Correlation Function Between Temperature Anomalies and Wheat Yields in France')
plt.xlabel('Lag')
plt.ylabel('CCF')
plt.show()
