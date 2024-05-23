import tkinter as tk
from tkinter import ttk

import tkinter as tk
from tkinter import ttk

# def set_dark_theme():
#     style = ttk.Style()
#     style.theme_use("clam")
#     style.configure(".", background="#333333", foreground="white")
#     style.map("TButton", background=[("active", "#666666")])
#     style.map("TScrollbar", background=[("active", "#666666")])

# def citeste_input():
#     try:
#         with open("input.txt", "r") as file:
#             input_text = file.read()
#     except FileNotFoundError:
#         input_text = ""
#     text_input.delete("1.0", "end")
#     text_input.insert("1.0", input_text)

# def salveaza_input():
#     input_text = text_input.get("1.0", "end-1c")
#     with open("input.txt", "w") as file:
#         file.write(input_text)
#     root.destroy()



# root = tk.Tk()
# root.title("Introducere date pentru input.txt")
# set_dark_theme()
# label = tk.Label(root, text="Introduceți sau editați datele:", bg="#333333", fg="white")
# label.pack()
# text_input = tk.Text(root, height=50, width=100, bg="#333333", fg="white")
# text_input.pack()
# button_save = tk.Button(root, text="Salvează", command=salveaza_input, bg="#666666", fg="white")
# button_save.pack(side="bottom", padx=5)
# citeste_input()
# root.mainloop()