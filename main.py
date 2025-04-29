import tkinter as tk
from tkinter import messagebox
import subprocess

# Función para capturar imágenes
def capturar_imagenes():
    try:
        subprocess.run(["python", "capturandoRostros.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar capturandoRostros.py: {e}")

# Función para entrenar modelo
def entrenar_modelo():
    try:
        subprocess.run(["python", "entrenando.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar entrenando.py: {e}")

# Función para validar emoción
def validar_emocion():
    try:
        subprocess.run(["python", "reconocimientoEmociones.py"])
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo ejecutar reconocimientoEmociones.py: {e}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Detección de emociones")
ventana.geometry("400x300")

# Crear un Frame
frame = tk.Frame(ventana, padx=20, pady=20)
frame.pack(expand=True)

# Etiqueta de título
titulo = tk.Label(frame, text="Detección de emociones", font=("Arial", 16))
titulo.pack(pady=10)

# Botones
btn_capturar = tk.Button(frame, text="Capturar imágenes", command=capturar_imagenes, width=25)
btn_capturar.pack(pady=5)

btn_entrenar = tk.Button(frame, text="Entrenar modelo", command=entrenar_modelo, width=25)
btn_entrenar.pack(pady=5)

btn_validar = tk.Button(frame, text="Validar emoción detectada", command=validar_emocion, width=25)
btn_validar.pack(pady=5)

# Iniciar el bucle de la interfaz
ventana.mainloop()
