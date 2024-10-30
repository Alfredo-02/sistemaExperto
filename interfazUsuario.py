import tkinter as tk
from tkinter import messagebox

def interfaz_usuario(ventana_anterior):
    # Crear nueva ventana
    ventana_usuario = tk.Toplevel()
    ventana_usuario.title("Sistema de Búsqueda")
    ventana_usuario.attributes("-fullscreen", True)
    ventana_usuario.configure(bg="#6FB0B5")
    
    # Título
    titulo_label = tk.Label(
        ventana_usuario, 
        text="Sistema de Búsqueda", 
        font=("Tahoma", 64, "bold"), 
        fg="black",
        bg="#6FB0B5",
        bd=19
    )
    titulo_label.pack(pady=50)
    
    # Frame para centrar los botones
    frame_botones = tk.Frame(ventana_usuario, bg="#6FB0B5")
    frame_botones.pack(expand=True)
    
    # Botones
    btn_sintomas = tk.Button(
        frame_botones,
        text="Búsqueda por síntomas",
        font=("Georgia", 24, "bold"),
        bg="#6A70FE",
        width=25,
        command=lambda: busqueda_sintomas()
    )
    btn_sintomas.pack(pady=20)
    
    btn_enfermedad = tk.Button(
        frame_botones,
        text="Búsqueda por enfermedad",
        font=("Georgia", 24, "bold"),
        bg="#BFBF00",
        width=25,
        command=lambda: busqueda_enfermedad()
    )
    btn_enfermedad.pack(pady=20)
    
    # Botón regresar en la parte inferior
    btn_regresar = tk.Button(
        ventana_usuario,
        text="Regresar",
        font=("Georgia", 18, "bold"),
        bg="#FF6B6B",
        width=15,
        command=lambda: regresar()
    )
    btn_regresar.pack(side=tk.BOTTOM, pady=50)
    
    # Funciones de los botones
    def busqueda_sintomas():
        messagebox.showinfo("Búsqueda por síntomas", "Función en desarrollo")
        
    def busqueda_enfermedad():
        messagebox.showinfo("Búsqueda por enfermedad", "Función en desarrollo")
        
    def regresar():
        ventana_usuario.destroy()
        ventana_anterior.deiconify()