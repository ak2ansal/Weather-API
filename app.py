import requests
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

API_KEY = '538597e779004508610dd865f0a62281'
cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            "avg_temp": data['main']['temp'],
            "max_temp": data['main']['temp_max'],
            "min_temp": data['main']['temp_min'],
            "condition": data['weather'][0]['main'],
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
            "wind_speed": data['wind']['speed']
        }
        return weather_data
    else:
        print(f"Failed to retrieve data for {city}")
        return None

def plot_weather_graph(weather):
    fig, ax = plt.subplots(figsize=(5, 3))
    
    temps = ['Min Temp', 'Avg Temp', 'Max Temp']
    temp_values = [weather['min_temp'], weather['avg_temp'], weather['max_temp']]
    
    ax.bar(temps, temp_values, color=['blue', 'orange', 'red'])
    
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Temperature Overview')
    
    return fig

def update_weather(city):
    weather = get_weather_data(city)
    if weather:
        city_name_label.config(text=city)
        temp_label.config(text=f"{weather['avg_temp']}°C")
        condition_label.config(text=f"Condition: {weather['condition']}")
        humidity_label.config(text=f"Humidity: {weather['humidity']}%")
        pressure_label.config(text=f"Pressure: {weather['pressure']} mmHG")
        wind_label.config(text=f"Wind: {weather['wind_speed']} m/s")
        forecast_labels[0].config(text=f"Min: {weather['min_temp']}°C")
        forecast_labels[1].config(text=f"Max: {weather['max_temp']}°C")
        forecast_labels[2].config(text=f"Avg: {weather['avg_temp']}°C")
        
        # Clear any existing plot before adding a new one
        for widget in graph_frame.winfo_children():
            widget.destroy()

        # Plot the weather graph and embed it in the UI
        fig = plot_weather_graph(weather)
        canvas = FigureCanvasTkAgg(fig, master=graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

def update_all_cities():
    for city in cities:
        update_weather(city)
    root.after(300000, update_all_cities)  # Automatically refresh data every 5 minutes (300000 ms)

# Create the main window
root = tk.Tk()
root.title("Weather Data")
root.geometry("800x700")
root.configure(bg="#f0f0f0")

# Left frame for cities list
left_frame = tk.Frame(root, bg="#333", width=200, height=600)
left_frame.pack(side="left", fill="y")

# Right frame for weather details
right_frame = tk.Frame(root, bg="white", width=600, height=600)
right_frame.pack(side="right", fill="both", expand=True)

# City selection buttons
for city in cities:
    city_button = tk.Button(left_frame, text=city, font=("Arial", 16), bg="#444", fg="white", bd=0,
                            command=lambda city=city: update_weather(city))
    city_button.pack(fill="x", pady=10, padx=10)

# Weather display (Right frame)
city_name_label = tk.Label(right_frame, text="", font=("Arial", 30, "bold"), bg="white")
city_name_label.pack(pady=20)

temp_label = tk.Label(right_frame, text="", font=("Arial", 40), bg="white")
temp_label.pack()

condition_label = tk.Label(right_frame, text="", font=("Arial", 16), bg="white")
condition_label.pack(pady=10)

humidity_label = tk.Label(right_frame, text="", font=("Arial", 14), bg="white")
humidity_label.pack(pady=5)

pressure_label = tk.Label(right_frame, text="", font=("Arial", 14), bg="white")
pressure_label.pack(pady=5)

wind_label = tk.Label(right_frame, text="", font=("Arial", 14), bg="white")
wind_label.pack(pady=5)

# Forecast labels for min, max, and avg temperatures
forecast_frame = tk.Frame(right_frame, bg="white")
forecast_frame.pack(pady=20)

forecast_labels = []
for i in range(3):  # Min, Max, and Avg labels
    forecast_label = tk.Label(forecast_frame, text="", font=("Arial", 14), bg="white", width=10)
    forecast_label.grid(row=0, column=i, padx=5)
    forecast_labels.append(forecast_label)

# Graph frame to hold the graph below the temperature info
graph_frame = tk.Frame(right_frame, bg="white")
graph_frame.pack(pady=20)

# Initially load the weather data for all cities
update_all_cities()

# Run the Tkinter event loop
root.mainloop()
