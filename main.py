import tkinter as tk
root = tk.Tk()
root.title("My Window")
root.geometry("600x600")
root.configure(bg="pink")

label = tk.Label(root, text="Click the button for a surprise!", bg="pink", font=("Arial", 20), fg="black")
label.pack()

def on_button_click():
    label.config(text="BOO!", font= ("Arial", 40), fg="red", bg="pink")
    label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()


root.mainloop()
