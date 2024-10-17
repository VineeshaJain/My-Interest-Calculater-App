import tkinter as tk
from tkinter import messagebox

# Function to calculate Simple Interest and Compound Interest
def calculate_interest():
    try:
        principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())

        # Calculate Simple Interest (SI)
        simple_interest = (principal * time * rate) / 100

        # Calculate Compound Interest (CI) assuming compound annually
        compound_interest = principal * (pow((1 + rate / 100), time)) - principal

        # Display results
        si_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        ci_label.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Create the main window
window = tk.Tk()
window.title("Interest Calculator")

# Principal amount label and entry
tk.Label(window, text="Principal Amount:").grid(row=0, column=0, padx=10, pady=10)
principal_entry = tk.Entry(window)
principal_entry.grid(row=0, column=1, padx=10, pady=10)

# Time period label and entry
tk.Label(window, text="Time Period (years):").grid(row=1, column=0, padx=10, pady=10)
time_entry = tk.Entry(window)
time_entry.grid(row=1, column=1, padx=10, pady=10)

# Rate of interest label and entry
tk.Label(window, text="Rate of Interest (%):").grid(row=2, column=0, padx=10, pady=10)
rate_entry = tk.Entry(window)
rate_entry.grid(row=2, column=1, padx=10, pady=10)

# Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_interest)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Labels to display results
si_label = tk.Label(window, text="Simple Interest: ")
si_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

ci_label = tk.Label(window, text="Compound Interest: ")
ci_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI application
window.mainloop()