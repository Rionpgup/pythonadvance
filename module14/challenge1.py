
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('weather_tokyo_data.csv')


df = df[['Date', 'Temperature']]
df.dropna(inplace=True)


average_temp = round(df['Temperature'].mean(), 2)
print(f"Average temperature for the entire dataset: {average_temp}°")


df['Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby('Month')['Temperature'].mean()


monthly_avg.plot(kind='bar', figsize=(12, 5), title='Monthly Average Temperature')
plt.ylabel('Temperature (°)')
plt.xlabel('Month')
plt.tight_layout()
plt.show()


hottest_day = df.loc[df['Temperature'].idxmax()]
coldest_day = df.loc[df['Temperature'].idxmin()]

print(f"Hottest day: {hottest_day['Date'].date()} with {hottest_day['Temperature']}°")
print(f"Coldest day: {coldest_day['Date'].date()} with {coldest_day['Temperature']}°")


df_sorted = df.sort_values(by='Date')
plt.figure(figsize=(14, 6))
plt.plot(df_sorted['Date'], df_sorted['Temperature'], label='Daily Temperature')
plt.title("Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°)")
plt.legend()
plt.tight_layout()
plt.show()


df['Season'] = df['Date'].dt.month % 12 // 3 + 1
season_map = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
df['Season'] = df['Season'].map(season_map)
seasonal_avg = df.groupby('Season')['Temperature'].mean()

print("Seasonal Average Temperatures:")
print(seasonal_avg.round(2))
