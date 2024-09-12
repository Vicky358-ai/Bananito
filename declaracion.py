import tkinter as tk
from tkinter import messagebox
import webbrowser
import random

# Crear la ventana principal
root = tk.Tk()
root.title("¿Quieres salir conmigo el domingo?")

# Configuración del tamaño de la ventana
root.geometry("400x200")

# Texto principal
label = tk.Label(root, text="¿QUIERES SALIR CONMIGO EL DOMINGO Y EL RESTO DE LOS DOMINGOS LINDOTE?", wraplength=350, font=("Arial", 12), pady=20)
label.pack()

# Función para cuando se elige "Sí"
def si():
    messagebox.showinfo("Respuesta", "¡Sabía que dirías que sí! 😊")

# Función para cuando se intenta hacer clic en "No"
def no_move(event):
    # Generar nuevas posiciones aleatorias para el botón "No"
    x = random.randint(0, root.winfo_width() - no_button.winfo_width())
    y = random.randint(50, root.winfo_height() - no_button.winfo_height())
    
    no_button.place(x=x, y=y)

# Botón "Sí"
yes_button = tk.Button(root, text="Sí", command=si, width=10, bg="green", fg="white")
yes_button.pack(side="left", padx=20, pady=20)

# Botón "No"
no_button = tk.Button(root, text="No", width=10, bg="red", fg="white")
no_button.place(x=250, y=100)

# Detectar cuando el cursor se acerca al botón "No"
no_button.bind("<Enter>", no_move)

# Iniciar la ventana
root.mainloop()

