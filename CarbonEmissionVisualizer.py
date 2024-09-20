
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate carbon emission for each activity
def calculate_emission(activity, quantity):
    # Emission factors (kgCO2 per unit) for different daily activities
    emission_factors = {
        "Driving": 0.108,  # kgCO2 per km
        "Train": 0.35,
        "Motorbike": 0.113,
        "Bus": 0.16,
        "Plane": 0.115,
        "Light bulb": 0.0038,  # kgCO2 per hour
        "AC": 0.9,
        "Refrigerator": 0.010,
        "TV": 0.088,
        "Vegan meal": 0.7,  # kgCO2 per 1000 calories
        "Vegetarian meal": 1.16,
        "Pascatarian meal": 1.66,
        "Omnivorous meal": 2.23,
        "Keto meal": 2.91
    }
    emission = emission_factors[activity] * quantity
    return emission

# Function to handle button click
def submit_activities():
    emissions = []
    for activity, scale_var in activity_vars.items():
        quantity = scale_var.get() / 2 
        emission = calculate_emission(activity, quantity)
        emissions.append((activity, emission))
    plot_emissions(emissions)

# Function to plot the emissions
def plot_emissions(emissions):
    activities, values = zip(*emissions)
    plt.figure(figsize=(10, 6))
    plt.bar(activities, values, color='palevioletred')
    plt.xlabel('Activity')
    plt.ylabel('Carbon Emission (kgCO2)')
    plt.title('Carbon Emission from Daily Activities')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(np.arange(0, max(values)+1, 0.5))  
    plt.tight_layout()
    plt.show()

# Create tkinter GUI
root = tk.Tk()
root.title("Carbon Emission Visualizer")

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

inner_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

# Define activities
activities = {
    "Driving": "km",
    "Train": "km",
    "Motorbike": "km",
    "Bus": "km",
    "Plane": "km",
    "Light bulb": "hours",
    "AC": "hours",
    "Refrigerator": "hours",
    "TV": "hours",
    "Vegan meal": "meals",
    "Vegetarian meal": "meals",
    "Pascatarian meal": "meals",
    "Omnivorous meal": "meals",
    "Keto meal": "meals"
}

# Create scales for each activity
activity_vars = {}
for i, (activity, unit) in enumerate(activities.items()):
    tk.Label(inner_frame, text=activity).grid(row=i, column=0, padx=5, pady=5, sticky='w')
    scale_var = tk.Scale(inner_frame, from_=0, to=48, orient='horizontal', length=350, tickinterval=6, resolution=0.5)
    scale_var.grid(row=i, column=1, padx=5, pady=5)
    activity_vars[activity] = scale_var
    unit_label = tk.Label(inner_frame, text=unit)
    unit_label.grid(row=i, column=2, padx=5, pady=5, sticky='w')

inner_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

submit_button = tk.Button(root, text="Submit", command=submit_activities)
submit_button.pack(pady=10)

root.mainloop()
