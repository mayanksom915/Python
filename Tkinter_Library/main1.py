import tkinter as tk

root = tk.Tk()         
root.title("--- GARENA ---")
root.geometry("700x600")
root.configure(bg="black")
label=tk.Label(
    root,
    text="FREE FIRE INDIA",
    bg="yellow",
    fg="darkgreen",
    padx=180,
    pady = 50,
    font=("Arial",30)
)
label.pack(pady=150,padx=150)
root.mainloop()