import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Create widgets
label1 = tk.Label(window, text="Hello, World!")
label2 = tk.Label(window, text="This is a resizable window!")

# Grid layout
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

# Run the Tkinter event loop
window.mainloop()
