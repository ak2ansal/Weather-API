import tkinter as tk
from tkinter import ttk

def show_weather_ui(city_weather_data):
    
    root = tk.Tk()
    root.title("City Weather Data")
    root.geometry("600x400")

    
    title_label = tk.Label(root, text="Weather Data for Cities", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    
    frame = ttk.Frame(root)
    frame.pack(padx=20, pady=20)

    
    row = 0
    for city, data in city_weather_data.items():
        city_label = tk.Label(frame, text=f"City: {city}", font=("Arial", 12, "bold"))
        city_label.grid(row=row, column=0, sticky="w", padx=10, pady=5)

        temp_label = tk.Label(frame, text=f"Average Temp: {data['avg_temp']:.2f} °C", font=("Arial", 10))
        temp_label.grid(row=row, column=1, padx=10, pady=5)

        max_label = tk.Label(frame, text=f"Max Temp: {data['max_temp']:.2f} °C", font=("Arial", 10))
        max_label.grid(row=row, column=2, padx=10, pady=5)

        min_label = tk.Label(frame, text=f"Min Temp: {data['min_temp']:.2f} °C", font=("Arial", 10))
        min_label.grid(row=row, column=3, padx=10, pady=5)

        condition_label = tk.Label(frame, text=f"Condition: {data['condition']}", font=("Arial", 10))
        condition_label.grid(row=row, column=4, padx=10, pady=5)

        row += 1

    
    root.mainloop()
