import tkinter as tk

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["/", "*", "-", "+", "="]
top_symbols = ["AC", "+/-", "%", "√"]

row_count = len(button_values)  # 5
column_count = len(button_values[0])  # 4

color_light_grey = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_grey = "#505050"
color_orange = "#FF9500"
color_white = "white"

# Window setup
window = tk.Tk()
window.title("Simple Calculator")
window.resizable(False, False)

# Display
display = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Function to handle button clicks
def button_click(value):
    current = display.get()
    if value == "AC":
        display.delete(0, tk.END)
    elif value == "+/-":
        if current and current[0] == "-":
            display.delete(0, 1)
        else:
            display.insert(0, "-")
    elif value == "%":
        try:
            result = str(eval(current) / 100)
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif value == "√":
        try:
            result = str(float(current) ** 0.5)
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    elif value == "=":
        try:
            result = str(eval(current))
            display.delete(0, tk.END)
            display.insert(0, result)
        except:
            display.delete(0, tk.END)
            display.insert(0, "Error")
    else:
        display.insert(tk.END, value)

# Create buttons
for i in range(row_count):
    for j in range(column_count):
        value = button_values[i][j]
        if value in right_symbols:
            bg_color = color_orange
            fg_color = color_white
        elif value in top_symbols:
            bg_color = color_dark_grey
            fg_color = color_white
        else:
            bg_color = color_light_grey
            fg_color = color_black
        
        button = tk.Button(window, text=value, font=("Arial", 18), bg=bg_color, fg=fg_color,
                           command=lambda v=value: button_click(v))
        button.grid(row=i+1, column=j, sticky="nsew")

# Configure grid weights
for i in range(row_count + 1):
    window.grid_rowconfigure(i, weight=1)
for j in range(column_count):
    window.grid_columnconfigure(j, weight=1)

window.mainloop()