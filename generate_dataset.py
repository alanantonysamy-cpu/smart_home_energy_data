
import pandas as pd
import numpy as np

# Generate 500 sample records
np.random.seed(42)

n = 500

# Input features
temperature = np.random.uniform(18, 40, n).round(1)

occupancy = np.random.randint(0, 2, n)

light_lux = np.random.randint(20, 1000, n)

usage_hours = np.random.uniform(0, 12, n).round(1)

# Generate output labels

# Light recommendation
light_status = np.where(
    (occupancy == 1) & (light_lux < 300),
    "ON",
    "OFF"
)

# Fan recommendation
fan_status = np.where(
    (occupancy == 1) & (temperature >= 28),
    "ON",
    "OFF"
)

# Appliance recommendation
appliance_status = np.where(
    (occupancy == 1) & (usage_hours >= 0.5),
    "ON",
    "OFF"
)

# Create dataset
df = pd.DataFrame({

    "temperature": temperature,

    "occupancy": occupancy,

    "light_lux": light_lux,

    "usage_hours": usage_hours,

    "light_status": light_status,

    "fan_status": fan_status,

    "appliance_status": appliance_status

})

# Save dataset as CSV
df.to_csv("smart_home_energy_data.csv", index=False)

# Display dataset
print("Dataset Generated Successfully!")

print("\nFirst 10 Records:")
print(df.head(10))

print("\nDataset Information:")
print(df.info())

print("\nTotal Records:", len(df))

print("\nCSV file saved successfully!")
