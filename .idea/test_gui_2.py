import tkinter as tk
from tkinter import colorchooser

# Créer la fenêtre principale
root = tk.Tk()

# Créer un bouton qui ouvre le sélecteur de couleur
button = tk.Button(root, text="Sélectionner une couleur", command=lambda: colorchooser.askcolor())

# Ajouter le bouton à la fenêtre principale
button.pack()

# Afficher la fenêtre principale
root.mainloop()
