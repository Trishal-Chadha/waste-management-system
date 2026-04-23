import tkinter as tk
from tkinter import messagebox
import pickle
import winsound
import matplotlib.pyplot as plt

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

history = []

def predict():
    try:
        fill = float(entry_fill.get())
        weight = float(entry_weight.get())
        time = float(entry_time.get())

        history.append(fill)

        # Save log
        with open("log.txt", "a") as f:
            f.write(f"{fill},{weight},{time}\n")

        if fill >= 80:
            result = "🚨 ALERT: Bin is 80% FULL!"
            output_label.config(text=result, fg="red")
            winsound.Beep(1000, 500)
            messagebox.showwarning("Alert", result)
        else:
            pred = model.predict([[fill, weight, time]])
            if pred[0] == 1:
                result = "Bin is FULL 🚨"
                output_label.config(text=result, fg="orange")
            else:
                result = "Bin is NOT FULL ✅"
                output_label.config(text=result, fg="green")

    except:
        messagebox.showerror("Error", "Invalid input!")

def reset():
    entry_fill.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    output_label.config(text="")

# 📊 GRAPH FUNCTION
def show_graph():
    if len(history) == 0:
        messagebox.showinfo("Info", "No data to display!")
        return

    plt.plot(history)
    plt.title("Waste Level Trend")
    plt.xlabel("Entries")
    plt.ylabel("Fill Level (%)")
    plt.grid()
    plt.show()

# WINDOW
root = tk.Tk()
root.title("Smart Waste Management System")
root.geometry("420x400")
root.configure(bg="#1e1e2f")

# TITLE
tk.Label(root, text="SMART WASTE SYSTEM", 
         font=("Arial", 18, "bold"), 
         fg="white", bg="#1e1e2f").pack(pady=15)

# INPUTS
def create_input(label):
    tk.Label(root, text=label, fg="white", bg="#1e1e2f").pack()
    entry = tk.Entry(root, bg="#2e2e3e", fg="white", insertbackground="white")
    entry.pack(pady=5)
    return entry

entry_fill = create_input("Fill Level (%)")
entry_weight = create_input("Weight (kg)")
entry_time = create_input("Time (hours)")

# BUTTONS
tk.Button(root, text="Predict", command=predict, bg="#4CAF50", fg="white", width=15).pack(pady=10)
tk.Button(root, text="Reset", command=reset, bg="#607D8B", fg="white", width=15).pack()
tk.Button(root, text="Show Graph", command=show_graph, bg="#2196F3", fg="white", width=15).pack(pady=10)

# OUTPUT
output_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#1e1e2f")
output_label.pack(pady=10)

root.mainloop()