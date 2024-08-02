import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / (height * height)
        bmi = round(bmi, 2)
        messagebox.showinfo("BMI Result", f"Your BMI is: {bmi}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for height and weight")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create and place the height label and entry
label_height = tk.Label(root, text="Enter height in meters (e.g., 1.65):")
label_height.pack()

entry_height = tk.Entry(root)
entry_height.pack()

# Create and place the weight label and entry
label_weight = tk.Label(root, text="Enter weight in kilograms (e.g., 72):")
label_weight.pack()

entry_weight = tk.Entry(root)
entry_weight.pack()

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Run the main loop
root.mainloop()
