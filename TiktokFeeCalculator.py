import tkinter as tk
from tkinter import messagebox

def calculate_fee():
    try:
        # 1. Fetch values and handle empty inputs
        val_amount = entry_amount.get().strip()
        val_source = source_amount.get().strip()
        
        if not val_amount or not val_source:
            raise ValueError("All fields are required.")
            
        amount = float(val_amount)
        source_price = float(val_source)
        
        # 2. Correct validation logic
        if amount < 0 or source_price < 0:
            raise ValueError("Numbers must be positive.")
        
        # 3. Calculate asking price
        base_fee = 0.75
        percentage_rate = 0.16
        total_fee = base_fee + (amount * percentage_rate) 
        asking_price =  total_fee + source_price
        
        # 4. Calculate PnL string safely
        pnl_value = amount - asking_price
            
        # 5. Update UI
        label_fee.config(text=f"PnL: £{pnl_value:.2f}")
        label_total_fee.config(text=f"Total Fee: £{total_fee:.2f}")
        label_total.config(text=f"Total Cost: £{asking_price:.2f}")
        
    except ValueError as e:
        messagebox.showerror("Error", str(e) if str(e) else "Please enter valid positive numbers.")

# Window Setup
root = tk.Tk()
root.title("Fee Calculator")
root.geometry("380x320") # Expanded slightly to fit all fields comfortably

# Widgets layout
tk.Label(root, text="Enter Transaction Amount (£):", font=("Arial", 11)).pack(pady=5)
entry_amount = tk.Entry(root, font=("Arial", 11))
entry_amount.pack(pady=5)

tk.Label(root, text="Enter Source Price (£):", font=("Arial", 11)).pack(pady=5)
source_amount = tk.Entry(root, font=("Arial", 11))
source_amount.pack(pady=5)

btn_calc = tk.Button(root, text="Calculate", font=("Arial", 11, "bold"), command=calculate_fee, bg="#007bff", fg="white")
btn_calc.pack(pady=15)

label_fee = tk.Label(root, text="PnL: £0.00", font=("Arial", 11, "bold"))
label_fee.pack(pady=5)

label_total_fee = tk.Label(root, text="Fee: £0.00", font=("Arial", 11, "bold"))
label_total_fee.pack(pady=5)

label_total = tk.Label(root, text="Asking Price: £0.00", font=("Arial", 11, "bold"))
label_total.pack(pady=5)

root.mainloop()