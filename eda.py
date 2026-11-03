import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Database se data read karein
conn = sqlite3.connect('weather_data.db')
df = pd.read_sql('SELECT * FROM city_weather', conn)
conn.close()

print("--- Loaded Data from Database ---")
print(df)

# 2. Basic Summary Statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# 3. Visualizations (4 Graphs: Temp, Humidity, Wind Speed, Pressure)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(14, 10))

# Graph 1: Temperature
plt.subplot(2, 2, 1)
sns.barplot(x='city', y='temperature', data=df, palette='coolwarm')
plt.title('Temperature Across Cities (°C)')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')

# Graph 2: Humidity
plt.subplot(2, 2, 2)
sns.barplot(x='city', y='humidity', data=df, palette='Blues_r')
plt.title('Humidity Across Cities (%)')
plt.xlabel('City')
plt.ylabel('Humidity (%)')

# Graph 3: Wind Speed
plt.subplot(2, 2, 3)
sns.barplot(x='city', y='wind_speed', data=df, palette='Greens_r')
plt.title('Wind Speed Across Cities (m/s)')
plt.xlabel('City')
plt.ylabel('Wind Speed (m/s)')

# Graph 4: Pressure
plt.subplot(2, 2, 4)
sns.barplot(x='city', y='pressure', data=df, palette='Purples_r')
plt.title('Pressure Across Cities (hPa)')
plt.xlabel('City')
plt.ylabel('Pressure (hPa)')

plt.tight_layout()

# Graph ko save karna
plt.savefig('weather_eda_analysis.png')
print("\nAll 4 EDA Graphs successfully generated and saved as 'weather_eda_analysis.png'!")

# Graph screen par show karne ke liye
plt.show()