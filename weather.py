import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timezone
import matplotlib.pyplot as plt
import time 
import numpy as np
# Auto-refresh every 10 seconds
#st_autorefresh(interval=10 * 1000, key="data_refresh")

# Replace with your OpenWeatherMap API Key
API_KEY = '41457ae77bbcb6a6303be45d635ff971'
CITY = 'London'  # Example city, change as needed

# Initialize a list to store the temperature and humidity over time
temperature_data = []
humidity_data = []
time_data = []

# Define a function to fetch live weather data
def fetch_live_weather():
    #url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'
    #response = requests.get(url, timeout=10)
    #data = response.json()

    #if response.status_code == 200:
        # Extract relevant data
    weather_info = {
        'City': CITY,
        'Temperature (°C)': np.random.randint(10, 30), #data['main']['temp'],
        'Humidity (%)': np.random.randint(30, 80), #data['main']['humidity'],
        'Time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return weather_info
    #else:
    #    return {'Error': 'Failed to fetch data'}

# Set up Streamlit layout
st.title("Live Weather Data Fetcher")
st.write("This app fetches live weather data every 10 seconds and displays it as a plot.")

# Create a placeholder for the plot
plot_placeholder = st.empty()

# Main loop to update data and plot
while True:
    # Fetch live weather data
    weather_info = fetch_live_weather()

    if 'Temperature (°C)' in weather_info:  # Check if data fetched successfully
        # Append the new data to the lists
        temperature_data.append(weather_info['Temperature (°C)'])
        humidity_data.append(weather_info['Humidity (%)'])
        time_data.append(weather_info['Time'])

        # Plot the data
        fig, ax1 = plt.subplots()

        # Plot temperature on the left axis
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Temperature (°C)', color='tab:red')
        ax1.plot(time_data, temperature_data, color='tab:red', label="Temperature (°C)")
        ax1.tick_params(axis='y', labelcolor='tab:red')

        # Create a second y-axis for humidity
        ax2 = ax1.twinx()
        ax2.set_ylabel('Humidity (%)', color='tab:blue')
        ax2.plot(time_data, humidity_data, color='tab:blue', label="Humidity (%)")
        ax2.tick_params(axis='y', labelcolor='tab:blue')

        # Rotate x-axis labels to avoid overlap
        plt.xticks(rotation=45)

        # Title and layout
        plt.title(f"Live Weather Data for {CITY}")
        #fig.tight_layout()

        # Display the plot in the Streamlit app
        plot_placeholder.pyplot(fig)

    # Sleep for 10 seconds before fetching new data
    time.sleep(2)
