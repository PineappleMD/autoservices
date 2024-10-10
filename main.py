import tkinter as tk
from tkinter import messagebox

# Dictionary to store the service charges
service_charges = {
    "Oil Change": 30,
    "Lube Job": 20,
    "Radiator Flush": 40,
    "Transmission Flush": 100,
    "Inspection": 35,
    "Muffler Replacement": 200,
    "Tire Rotation": 20
}

def calculate_charges():
    total_charges = 0
    for service, charge in service_charges.items():
        if service_vars[service].get():
            total_charges += charge
    messagebox.showinfo("Total Charges", f"Total Charges: ${total_charges}")

# Create the main window
window = tk.Tk()
window.title("Service Selection")

# Create check buttons for each service
service_vars = {}
for service in service_charges:
    service_vars[service] = tk.BooleanVar()
    service_check = tk.Checkbutton(window, text=service, variable=service_vars[service])
    service_check.pack(anchor="w")

# Create a button to calculate charges
calculate_button = tk.Button(window, text="Calculate Charges", command=calculate_charges)
calculate_button.pack(pady=10)

# Start the main loop
window.mainloop()
