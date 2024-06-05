import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Create widgets
label1 = tk.Label(window, text="Hello, World!")
label2 = tk.Label(window, text="This is a resizable window!")

# Pack widgets into the window
label1.pack()
label2.pack()

# Run the Tkinter event loop
window.mainloop()
