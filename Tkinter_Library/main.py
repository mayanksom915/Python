import tkinter as tk

# Main window
root = tk.Tk()
root.title("My Tkinter App")
root.geometry("500x400")
root.configure(bg="lightblue")

# Label
label = tk.Label(
    root,
    text="Welcome to Tkinter!",
    bg="black",
    fg="white",
    padx=20,
    pady=10,
    font=("Arial", 16)
)
label.pack(padx=20, pady=30)

# Button click function
def change_text():
    label.config(text="Button Clicked!")

# Button
button = tk.Button(
    root,
    text="Click Me",
    command=change_text,
    bg="green",
    fg="white",
    padx=15,
    pady=8
)
button.pack()

# Run window
root.mainloop()

 