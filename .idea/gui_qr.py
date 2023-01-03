import customtkinter
from tkinter import *
from tkinter import ttk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk() and tk.Tk()
root.geometry("500x350")



def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login Accueil",)
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Entrez votre nom")
entry1.pack(pady=12,padx=10)
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Entrez votre mot de passe", show="*")
entry2.pack(pady=12,padx=10)
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()
