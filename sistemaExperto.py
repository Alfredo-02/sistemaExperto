#NUEVO CON CUADRO RELACIONNNNNNNNNN
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 19:42:35 2024

@author: Alfre
"""

import tkinter as tk
from tkinter import messagebox,Label, PhotoImage
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import simpledialog, messagebox
import mysql.connector 
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk 
import subprocess


def salir():
    if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
        root.destroy()

# Configura tu conexión a la base de datos
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",  # Cambia esto si es necesario
            user="root",  # Reemplaza con tu usuario
            password="",  # Reemplaza con tu contraseña
            database=""  # Reemplaza con tu base de datos
        )
        return conexion
    except mysql.connector.Error as e:
        messagebox.showerror("Error de conexión", str(e))
        return None
        
def cargar_gif(ruta, tamano=(300, 200)):
    imagen = Image.open(ruta)
    frames = [ImageTk.PhotoImage(imagen.resize(tamano))]

    try:
        while True:
            imagen.seek(len(frames))  # Ir al siguiente frame del GIF
            frames.append(ImageTk.PhotoImage(imagen.resize(tamano)))
    except EOFError:
        pass  # Hemos leído todos los frames

    return frames
def mostrar_contenido_futuro():
    ventana_futuro = tk.Toplevel(root)
    ventana_futuro.title("Yo en el futuro")
    ventana_futuro.attributes("-fullscreen", True)
    ventana_futuro.configure(bg="darkturquoise")

    titulo_label = tk.Label(ventana_futuro, text="YO EN EL FUTURO", font=("Comic Sans MS", 32, "bold"), fg="black", bd=15)
    titulo_label.place(x=640,y=40)
    # Carga los GIFs
    frames7 = cargar_gif("imagenes/graduarme.png")
    frames3 = cargar_gif("imagenes/trabajando.png")
    frames6 = cargar_gif("imagenes/casa.gif")
    frames5 = cargar_gif("imagenes/tienda.gif")
    frames1 = cargar_gif("imagenes/autoimg.png")
    frames2 = cargar_gif("imagenes/familia.png")
    frames4 = cargar_gif("imagenes/vacaciones.png")


    # Crea etiquetas para mostrar los GIFs
    etiqueta1 = tk.Label(ventana_futuro)
    etiqueta1.place(x=15, y=200)
    
    # Crear un label para el texto
    label_texto = Label(ventana_futuro, text='Graduarme', font=('Arial', 18,"bold"))  
    label_texto.place(x=100, y=410)  
    
    etiqueta2 = tk.Label(ventana_futuro)
    etiqueta2.place(x=415, y=200)
    
    label_texto = Label(ventana_futuro, text='Tener empleo', font=('Arial', 18,"bold"))  
    label_texto.place(x=500, y=410)  
    
    etiqueta3 = tk.Label(ventana_futuro)
    etiqueta3.place(x=815, y=200)
    
    label_texto = Label(ventana_futuro, text='Construir casa', font=('Arial', 18,"bold")) 
    label_texto.place(x=900, y=410) 
    
    etiqueta4 = tk.Label(ventana_futuro)
    etiqueta4.place(x=1215, y=200)
    
    label_texto = Label(ventana_futuro, text='Negocio', font=('Arial', 18,"bold"))  
    label_texto.place(x=1300, y=410) 
    
    etiqueta5 = tk.Label(ventana_futuro)
    etiqueta5.place(x=215, y=500)
    
    label_texto = Label(ventana_futuro, text='Tener carro', font=('Arial', 18,"bold"))  
    label_texto.place(x=300, y=710) 
    
    etiqueta6 = tk.Label(ventana_futuro)
    etiqueta6.place(x=615, y=500)
    
    label_texto = Label(ventana_futuro, text='Tener familia', font=('Arial', 18, "bold"))  
    label_texto.place(x=700, y=710) 
    
    etiqueta7 = tk.Label(ventana_futuro)
    etiqueta7.place(x=1015, y=500)
    
    label_texto = Label(ventana_futuro, text='Estar de vacaciones', font=('Arial', 18,"bold")) 
    label_texto.place(x=1050, y=710) 

    # Funciones para actualizar los frames de los GIFs
         
    def actualizar1(indice):
        frame = frames1[indice]
        indice = (indice + 1) % len(frames1)
        etiqueta5.configure(image=frame)
        ventana_futuro.after(100, actualizar1, indice)
         
    def actualizar2(indice):
        frame = frames2[indice]
        indice = (indice + 1) % len(frames2)
        etiqueta6.configure(image=frame)
        ventana_futuro.after(100, actualizar2, indice)

    def actualizar3(indice):
        frame = frames3[indice]
        indice = (indice + 1) % len(frames3)
        etiqueta2.configure(image=frame)
        ventana_futuro.after(100, actualizar3, indice)

    def actualizar4(indice):
        frame = frames4[indice]
        indice = (indice + 1) % len(frames4)
        etiqueta7.configure(image=frame)
        ventana_futuro.after(100, actualizar4, indice)
          
    def actualizar5(indice):
        frame = frames5[indice]
        indice = (indice + 1) % len(frames5)
        etiqueta4.configure(image=frame)
        ventana_futuro.after(100, actualizar5, indice)
     
    def actualizar6(indice):
        frame = frames6[indice]
        indice = (indice + 1) % len(frames6)
        etiqueta3.configure(image=frame)
        ventana_futuro.after(100, actualizar6, indice)
        
    def actualizar7(indice):
        frame = frames7[indice]
        indice = (indice + 1) % len(frames7)
        etiqueta1.configure(image=frame)
        ventana_futuro.after(100, actualizar7, indice)

    # Comienza la animación de los GIFs
    ventana_futuro.after(0, actualizar1, 0)
    ventana_futuro.after(0, actualizar2, 0)
    ventana_futuro.after(0, actualizar3, 0)  
    ventana_futuro.after(0, actualizar4, 0)
    ventana_futuro.after(0, actualizar5, 0)
    ventana_futuro.after(0, actualizar6, 0)
    ventana_futuro.after(0, actualizar7, 0)
  
    btn_regresar = tk.Button(ventana_futuro,text="Regresar", command=ventana_futuro.destroy,font=("Comic Sans MS", 19, "bold"),bg="lightcoral") 
    btn_regresar.place(x=800, y=770)
     
def mostrar_contenido_hobbies():
    ventana_hobbies = tk.Toplevel(root)
    ventana_hobbies.title("Yo en el futuro")
    ventana_hobbies.attributes("-fullscreen", True)
    ventana_hobbies.configure(bg="#BFBF00")

    titulo_label = tk.Label(ventana_hobbies, text="HOBBIES", font=("Comic Sans MS", 32, "bold"), fg="black", bd=15)
    titulo_label.place(x=640,y=40)
    # Carga los GIFs
    #frames1 = cargar_gif("imagenes/hobbie1.png")
    frames2 = cargar_gif("imagenes/hobbie2.png")
    frames3 = cargar_gif("imagenes/hobbie3.png")
    #frames4 = cargar_gif("imagenes/hobbie4.png")
    frames5 = cargar_gif("imagenes/hobbie5.png")
    frames6 = cargar_gif("imagenes/hobbie1.png")
    frames7 = cargar_gif("imagenes/hobbie4.png")

    # Crea etiquetas para mostrar los GIFs
    etiqueta1 = tk.Label(ventana_hobbies)
    etiqueta1.place(x=15, y=200)
     
    etiqueta2 = tk.Label(ventana_hobbies)
    etiqueta2.place(x=415, y=200)
     
    label_texto = Label(ventana_hobbies, text='Conciertos', font=('Arial', 18,"bold"))  
    label_texto.place(x=530, y=410)  
     
    etiqueta3 = tk.Label(ventana_hobbies)
    etiqueta3.place(x=815, y=200)
     
    label_texto = Label(ventana_hobbies, text='Jugar videojuegos', font=('Arial', 18,"bold")) 
    label_texto.place(x=900, y=410) 
     
    etiqueta4 = tk.Label(ventana_hobbies)
    etiqueta4.place(x=1215, y=200)

     
    etiqueta5 = tk.Label(ventana_hobbies)
    etiqueta5.place(x=215, y=500)
     
    label_texto = Label(ventana_hobbies, text='Manejar moto', font=('Arial', 18,"bold")) 
    label_texto.place(x=300, y=710)  
     
    etiqueta6 = tk.Label(ventana_hobbies)
    etiqueta6.place(x=615, y=500)
     
    label_texto = Label(ventana_hobbies, text='Peliculas', font=('Arial', 18,"bold")) 
    label_texto.place(x=730, y=710)  
     
    etiqueta7 = tk.Label(ventana_hobbies)
    etiqueta7.place(x=1015, y=500)
     
    label_texto = Label(ventana_hobbies, text='Programar', font=('Arial', 18,"bold"))  
    label_texto.place(x=1130, y=710) 

    def actualizar2(indice):
       frame = frames2[indice]
       indice = (indice + 1) % len(frames2)
       etiqueta2.configure(image=frame)
       ventana_hobbies.after(100, actualizar2, indice)
       
    def actualizar3(indice):
       frame = frames3[indice]
       indice = (indice + 1) % len(frames3)
       etiqueta3.configure(image=frame)
       ventana_hobbies.after(100, actualizar3, indice)
       
    def actualizar5(indice):
       frame = frames5[indice]
       indice = (indice + 1) % len(frames5)
       etiqueta5.configure(image=frame)
       ventana_hobbies.after(100, actualizar5, indice)
       
    def actualizar6(indice):
       frame = frames6[indice]
       indice = (indice + 1) % len(frames6)
       etiqueta6.configure(image=frame)
       ventana_hobbies.after(100, actualizar6, indice)
       
    def actualizar7(indice):
       frame = frames7[indice]
       indice = (indice + 1) % len(frames7)
       etiqueta7.configure(image=frame)
       ventana_hobbies.after(100, actualizar7, indice)
  
    ventana_hobbies.after(0, actualizar2, 0)
    ventana_hobbies.after(0, actualizar3, 0)  
    ventana_hobbies.after(0, actualizar5, 0)
    ventana_hobbies.after(0, actualizar6, 0)
    ventana_hobbies.after(0, actualizar7, 0)
 
    btn_regresar = tk.Button(ventana_hobbies,text="Regresar", command=ventana_hobbies.destroy,font=("Comic Sans MS", 19, "bold"),bg="lightcoral")
    btn_regresar.place(x=700, y=770)

def mostrar_contenido_actualmente():
    ventana_actualmente = tk.Toplevel(root)
    ventana_actualmente.title("Yo Actualmente")
    ventana_actualmente.attributes("-fullscreen", True)
    ventana_actualmente.configure(bg="#6A70FE")

    # Título centrado
    titulo_label = tk.Label(ventana_actualmente, text="YO ACTUALMENTE", font=("Comic Sans MS", 32, "bold"), fg="black", bd=15)
    titulo_label.place(x=640,y=40)
    
    # Carga los GIFs
    frames1 = cargar_img("imagenes/actualmente1.png")
    frames2 = cargar_img("imagenes/actualmente2.png")
    frames3 = cargar_img("imagenes/actualmente3.png")
    frames4 = cargar_img("imagenes/actualmente4.png")
    frames5 = cargar_gif("imagenes/actualmente5.png")
   
    # Crea etiquetas para mostrar los GIFs
    etiqueta1 = tk.Label(ventana_actualmente)
    etiqueta1.place(x=15, y=200)
    
    # Crear un label para el texto
    label_texto = Label(ventana_actualmente, text='Resido en Zacatepec\n mientras estudio', font=('Arial', 18, "bold"))
    label_texto.place(x=50, y=520) 
    
    etiqueta2 = tk.Label(ventana_actualmente)
    etiqueta2.place(x=415, y=200)
    
    label_texto = Label(ventana_actualmente, text='Estudio en el ITZ', font=('Arial', 18,"bold")) 
    label_texto.place(x=500, y=520) 
    
    etiqueta3 = tk.Label(ventana_actualmente)
    etiqueta3.place(x=815, y=200)
    
    label_texto = Label(ventana_actualmente, text='Hago tareas', font=('Arial', 18,"bold"))  
    label_texto.place(x=900, y=520)  
    
    etiqueta4 = tk.Label(ventana_actualmente)
    etiqueta4.place(x=1215, y=200)
    
    label_texto = Label(ventana_actualmente, text='Haciendo proyecto\n de software', font=('Arial', 18,"bold")) 
    label_texto.place(x=1240, y=520)  
   
    etiqueta5 = tk.Label(ventana_actualmente)
    etiqueta5.place(x=415, y=580)

    label_texto = Label(ventana_actualmente, text='Curso ingles', font=('Arial', 18,"bold"))  
    label_texto.place(x=505, y=800) 

  # Funciones para actualizar los frames de los GIFs
    def actualizar1(indice):
       frame = frames1[indice]
       indice = (indice + 1) % len(frames1)
       etiqueta1.configure(image=frame)
       ventana_actualmente.after(100, actualizar1, indice)

    def actualizar2(indice):
      frame = frames2[indice]
      indice = (indice + 1) % len(frames2)
      etiqueta2.configure(image=frame)
      ventana_actualmente.after(100, actualizar2, indice)
      
    def actualizar3(indice):
      frame = frames3[indice]
      indice = (indice + 1) % len(frames3)
      etiqueta3.configure(image=frame)
      ventana_actualmente.after(100, actualizar3, indice)
      
    def actualizar4(indice):
      frame = frames4[indice]
      indice = (indice + 1) % len(frames4)
      etiqueta4.configure(image=frame)
      ventana_actualmente.after(100, actualizar4, indice)
    
    def actualizar5(indice):
       frame = frames5[indice]
       indice = (indice + 1) % len(frames5)
       etiqueta5.configure(image=frame)
       ventana_actualmente.after(100, actualizar5, indice)
   

    # Comienza la animación de los GIFs
    ventana_actualmente.after(0, actualizar1, 0)
    ventana_actualmente.after(0, actualizar2, 0)
    ventana_actualmente.after(0, actualizar3, 0) 
    ventana_actualmente.after(0, actualizar4, 0)
    ventana_actualmente.after(0, actualizar5, 0)
   
    btn_regresar = tk.Button(ventana_actualmente,text="Regresar", command=ventana_actualmente.destroy,font=("Comic Sans MS", 19, "bold"),bg="lightcoral") 
   
def entrar():
    ventana_entrar = tk.Toplevel(root)
    ventana_entrar.title("Entrar")
    ventana_entrar.attributes("-fullscreen", True)
    # ventana_entrar.minsize(800, 500)
    
    # Título
    ventana_entrar.configure(bg="#6FB0B5")
    titulo_label = tk.Label(ventana_entrar, text="MENÚ", font=("Tahoma", 64, "bold"), fg="black", bd=19)
    titulo_label.place(x=650,y=100)
    

    btn_actualmente = tk.Button(ventana_entrar, text="Yo actualmente", command=mostrar_contenido_actualmente, font=("Georgia", 24, "bold"), bg="#6A70FE", width=15)
    btn_actualmente.place(x=620, y=350)

    btn_hobbies = tk.Button(ventana_entrar, text="Mis hobbies", command=mostrar_contenido_hobbies,font=("Georgia", 24, "bold"),bg="#BFBF00", width=15)
    btn_hobbies.place(x=620,y=450)

    btn_futuro = tk.Button(ventana_entrar, text="Yo en el futuro", command=mostrar_contenido_futuro,font=("Georgia", 24, "bold"),bg="darkturquoise", width=15)
    btn_futuro.place(x=620,y=550)

    btn_regresar = tk.Button(ventana_entrar,text="Regresar", command=ventana_entrar.destroy,font=("Georgia", 24, "bold"),bg="lightcoral",width=15)  
    btn_regresar.place(x=620, y=700)

    # Cargar y mostrar la imagen debajo de los botones
    imagen = Image.open("imagenes/actual.png") 
    imagen = imagen.resize((55, 55))
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_entrar, image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.place(x=550, y=355)  
   
    imagen = Image.open("imagenes/integracion.png") 
    imagen = imagen.resize((55, 55))
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_entrar, image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.place(x=550, y=455)  
    imagen = Image.open("imagenes/futuro.png")  
    imagen = imagen.resize((55, 55))
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_entrar, image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.place(x=550, y=555) 
    
def cargar_img(ruta, tamano=(50, 50)):
    imagen = Image.open(ruta)
    frames = [ImageTk.PhotoImage(imagen.resize(tamano))]

    try:
        while True:
            imagen.seek(len(frames))  
            frames.append(ImageTk.PhotoImage(imagen.resize(tamano)))
    except EOFError:
        pass  

    return frames    
 
def abrir_autores():
    ventana_autores = tk.Toplevel(root)
    ventana_autores.title("AUTORES DEL SISTEMA")
    ventana_autores.attributes("-fullscreen", True)
    
    # AUTOR 1
    ventana_autores.configure(bg="#00BFBF")
    titulo_label = tk.Label(ventana_autores, text="AUTORES DEL SISTEMA", font=("Trebuchet MS", 50, "bold"), bg="#00BFBF")
    titulo_label.place(x=500,y=40)
     
    imagen_izquierda = tk.PhotoImage(file="imagenes/descarga4.png")  
    imagen_izquierda = imagen_izquierda.subsample(10) 
    imagen_label_izquierda = tk.Label(ventana_autores, image=imagen_izquierda,bg="black")
    imagen_label_izquierda.image = imagen_izquierda
    imagen_label_izquierda.place(x=100, y=180) 

    # Información a la derecha
    info_text = "Datos personales\nNombre: Alfredo Valparaiso Pascual\nDireccion: Calle Efren Mancilla, Zacatepec, Morelos\nTelefono:7361089433\nEmail:L20091196@Zacatepec.tecnm.mx"
    info_label = tk.Label(ventana_autores, text=info_text, justify=tk.LEFT, font=("Trebuchet MS", 28, "bold"), bg="#00BFBF")
    info_label.place(x=500,y=180)

    #AUTOR 2
    imagen_izquierda = tk.PhotoImage(file="imagenes/perro.png")  
    imagen_izquierda = imagen_izquierda.subsample(2) 
    imagen_label_izquierda = tk.Label(ventana_autores, image=imagen_izquierda,bg="black")
    imagen_label_izquierda.image = imagen_izquierda
    imagen_label_izquierda.place(x=100, y=500)  

    # Información a la derecha
    info_text = "Datos personales\nNombre: Perrito\nDireccion: Calle Efren Mancilla, Zacatepec, Morelos\nTelefono:7361089433\nEmail:Perrito@Zacatepec.tecnm.mx"
    info_label = tk.Label(ventana_autores, text=info_text, justify=tk.LEFT, font=("Trebuchet MS", 28, "bold"), bg="#00BFBF")
    info_label.place(x=500,y=500)
    
    btn_regresar = tk.Button(ventana_autores, text="Regresar", command=ventana_autores.destroy,  font=("Comic Sans MS", 19, "bold"), bg="lightcoral", image=logo_salir, compound="left")
    btn_regresar.place(x=1300,y=750)

    #VENTANA ACERCA DE
def abrir_ventana_acerca_de():
    ventana_acerca_de = tk.Toplevel(root)
    ventana_acerca_de.title("ACERCA DEL SISTEMA")
    ventana_acerca_de.attributes("-fullscreen", True)
    
    # Título
    ventana_acerca_de.configure(bg="#00BFBF")
    titulo_label = tk.Label(ventana_acerca_de, text="ACERCA DEL SISTEMA", font=("Trebuchet MS", 50, "bold"), bg="#00BFBF")
    titulo_label.place(x=500,y=40) 

    imagen_izquierda = tk.PhotoImage(file="imagenes/logootro.png")  
    imagen_izquierda = imagen_izquierda.subsample(3)  
    imagen_label_izquierda = tk.Label(ventana_acerca_de, image=imagen_izquierda,bg="black")
    imagen_label_izquierda.image = imagen_izquierda
    imagen_label_izquierda.place(x=610, y=180)  

    # Información a la derecha
    info_text = "Versión 1. \nEste software es para uso exclusivo de los alumnos de la materia dde Inteligencia \nArtificial de la carrera de Ingenieria en sistemas..."
    info_label = tk.Label(ventana_acerca_de, text=info_text, justify=tk.LEFT, font=("Trebuchet MS", 28, "bold"), bg="#00BFBF")
    info_label.place(x=50,y=500)
    
    btn_autores = tk.Button(ventana_acerca_de, text="Autores ", command=abrir_autores,  font=("Comic Sans MS", 19, "bold"), bg="lightcoral", image=logo_autor, compound="left")
    btn_autores.place(x=1300,y=650)

    btn_regresar = tk.Button(ventana_acerca_de, text="Regresar", command=ventana_acerca_de.destroy,  font=("Comic Sans MS", 19, "bold"), bg="lightcoral", image=logo_salir, compound="left")
    btn_regresar.place(x=1300,y=750)


def agregar_sintomas():
    global objetos, indice_actual, imagen_path  
    ventana_sintoma = tk.Toplevel(root)
    ventana_sintoma.title("Agregar síntomas")
    ventana_sintoma.attributes("-fullscreen", True)
    
    # Inicializar las variables
    imagen_path = "" 
    objetos = [] 
    indice_actual = 0 

    def cargar_objetos_desde_db():
        global objetos
        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT sintoma, imagen_path FROM sintomas")
                objetos = cursor.fetchall()  
            except mysql.connector.Error as e:
                messagebox.showerror("Error al cargar", str(e), parent=ventana_sintoma)
            finally:
                cursor.close()
                conexion.close()

    def cargar_y_mostrar_imagen(label, ruta=None, tamano_maximo=(340, 340)):
        global imagen_path 

        if not ruta:
            ruta = filedialog.askopenfilename(
                parent=ventana_sintoma,
                title="Seleccionar Imagen",
                filetypes=[("Archivos de Imagen", "*.jpg;*.jpeg;*.png;*.gif")]
            )

        if not ruta:
            return  

        imagen_path = ruta 

        imagen_original = Image.open(ruta)
        
        ancho_label, alto_label = tamano_maximo
        
        relacion_aspecto = min(ancho_label / imagen_original.width, alto_label / imagen_original.height)
        nuevo_ancho = int(imagen_original.width * relacion_aspecto)
        nuevo_alto = int(imagen_original.height * relacion_aspecto)
        
        imagen_redimensionada = imagen_original.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
        
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        
        label.config(image=imagen_tk)
        label.image = imagen_tk  

        return ruta

    def mostrar_objeto(indice):
        global objetos, imagen_path
        if objetos:
            sintoma, imagen_path = objetos[indice]  
            
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, sintoma) 

            # Asegurarse de que el label de imagen tenga un tamaño antes de cargar
            ventana_sintoma.update_idletasks()
            cargar_y_mostrar_imagen(imagen_label, ruta=imagen_path)

    def mover_adelante():
        global indice_actual, objetos
        if not objetos:
            messagebox.showinfo("Sin objetos", "No hay síntomas para mostrar.", parent=ventana_sintoma)
            return
        if indice_actual < len(objetos) - 1:
            indice_actual += 1
            mostrar_objeto(indice_actual)
        else:
            messagebox.showinfo("Fin alcanzado", "Ya no hay más síntomas. Este es el último.", parent=ventana_sintoma)

    def mover_atras():
        global indice_actual, objetos
        if not objetos:
            messagebox.showinfo("Sin objetos", "No hay síntomas para mostrar.", parent=ventana_sintoma)
            return
        if indice_actual > 0:
            indice_actual -= 1
            mostrar_objeto(indice_actual)
        else:
            messagebox.showinfo("Inicio alcanzado", "Ya estás en el primer síntoma. No hay nada más atrás.", parent=ventana_sintoma)

    def ir_a_inicio():
        global indice_actual, objetos
        if not objetos:
            messagebox.showinfo("Sin objetos", "No hay síntomas para mostrar.", parent=ventana_sintoma)
            return
        if indice_actual == 0:
            messagebox.showinfo("Ya en el inicio", "Ya estás en el primer síntoma.", parent=ventana_sintoma)
        else:
            indice_actual = 0
            mostrar_objeto(indice_actual)

    def ir_a_final():
        global indice_actual, objetos
        if not objetos:
            messagebox.showinfo("Sin objetos", "No hay síntomas para mostrar.", parent=ventana_sintoma)
            return
        if indice_actual == len(objetos) - 1:
            messagebox.showinfo("Ya en el final", "Ya estás en el último síntoma.", parent=ventana_sintoma)
        else:
            indice_actual = len(objetos) - 1
            mostrar_objeto(indice_actual)
            
    # Función para eliminar el síntoma señalado en la navegación
    def eliminar_objeto():
        global indice_actual, objetos
        if not objetos:
            messagebox.showwarning("No hay objetos", "No hay síntomas para eliminar.", parent=ventana_sintoma)
            return

        sintoma_actual = objetos[indice_actual]
        confirmacion = messagebox.askyesno("Confirmar eliminación", 
                                        f"¿Está seguro que desea eliminar el síntoma '{sintoma_actual[0]}'?", 
                                        parent=ventana_sintoma)
        
        if confirmacion:
            conexion = conectar_db()
            if conexion:
                cursor = conexion.cursor()
                try:
                    # Primero, obtener las enfermedades afectadas y sus pesos actuales
                    cursor.execute("""
                        SELECT e.id_enfermedad, e.suma_peso, cr.peso
                        FROM enfermedades e
                        JOIN cuadro_relacion cr ON e.id_enfermedad = cr.id_enfermedad
                        JOIN sintomas s ON cr.id_sintoma = s.id_sintoma
                        WHERE s.sintoma = %s
                    """, (sintoma_actual[0],))
                    enfermedades_afectadas = cursor.fetchall()

                    # Eliminar el síntoma
                    cursor.execute("DELETE FROM sintomas WHERE sintoma = %s", (sintoma_actual[0],))

                    # Actualizar la suma de peso para cada enfermedad afectada
                    for id_enfermedad, suma_peso_actual, peso_eliminado in enfermedades_afectadas:
                        nueva_suma = max(0, suma_peso_actual - peso_eliminado)
                        cursor.execute("""
                            UPDATE enfermedades 
                            SET suma_peso = %s 
                            WHERE id_enfermedad = %s
                        """, (nueva_suma, id_enfermedad))

                    conexion.commit()
                    messagebox.showinfo("Éxito", "Síntoma eliminado exitosamente", parent=ventana_sintoma)
                    
                    # Actualizar la lista de objetos y mostrar el siguiente
                    cargar_objetos_desde_db()
                    if objetos:
                        if indice_actual >= len(objetos):
                            indice_actual = len(objetos) - 1
                        mostrar_objeto(indice_actual)
                    else:
                        # Si no quedan objetos, limpiar los campos
                        nombre_entry.delete(0, tk.END)
                        imagen_label.config(image="")
                except mysql.connector.Error as e:
                    messagebox.showerror("Error al eliminar", str(e), parent=ventana_sintoma)
                finally:
                    cursor.close()
                    conexion.close()


    def realizar_consulta():
        tipo_consulta = messagebox.askquestion("Tipo de Consulta", "¿Desea realizar una consulta general?",
                                               icon='question', parent=ventana_sintoma)
        if tipo_consulta == 'yes':
            consulta_general()
        else:
            consulta_individual()

    def consulta_general():
        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT id_sintoma, sintoma, imagen_path FROM sintomas")
                resultados = cursor.fetchall()

                # Crear una nueva ventana para mostrar los resultados
                ventana_resultados = tk.Toplevel(ventana_sintoma)
                ventana_resultados.title("Consulta General")
                ventana_resultados.geometry("1000x600")
                ventana_resultados.configure(bg="#F0F0F0")

                # Estilo personalizado para el Treeview
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview", background="#D3D3D3",
                                fieldbackground="#D3D3D3", foreground="black")
                style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))

                # Crear un frame para contener el Treeview y la barra de desplazamiento
                frame = tk.Frame(ventana_resultados)
                frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

                # Crear un canvas y un frame interior para el scrolling
                canvas = tk.Canvas(frame)
                scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
                scrollable_frame = tk.Frame(canvas)

                scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )

                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)

                # Colocar el título en la fila 0 y abarcar todas las columnas
                tk.Label(scrollable_frame, text="Síntomas", font=('Helvetica', 20, 'bold')).grid(row=0, column=0, columnspan=3, pady=10)

                # Crear etiquetas para los encabezados en la fila 1
                tk.Label(scrollable_frame, text="ID", font=('Helvetica', 16, 'bold'), width=10).grid(row=1, column=0, padx=5, pady=5)
                tk.Label(scrollable_frame, text="Síntoma", font=('Helvetica', 16, 'bold'), width=20).grid(row=1, column=1, padx=5, pady=5)
                tk.Label(scrollable_frame, text="Imagen", font=('Helvetica', 16, 'bold'), width=20).grid(row=1, column=2, padx=5, pady=5)

                # Insertar los datos en el frame
                for i, row in enumerate(resultados, start=2):  # Iniciar en la fila 2 para los datos
                    id, sintoma, imagen_path = row
                    tk.Label(scrollable_frame, text=id, width=10, font=("Arial", 14)).grid(row=i, column=0, padx=5, pady=5)
                    tk.Label(scrollable_frame, text=sintoma, width=40, anchor="center", font=("Arial", 14)).grid(row=i, column=1, padx=5, pady=5)

                    # Mostrar la imagen si existe
                    if imagen_path:
                        try:
                            img = Image.open(imagen_path)
                            img = img.resize((200, 200), Image.LANCZOS)
                            photo = ImageTk.PhotoImage(img)
                            img_label = tk.Label(scrollable_frame, image=photo)
                            img_label.image = photo  # Mantener una referencia
                            img_label.grid(row=i, column=2, padx=5, pady=5)
                        except Exception as e:
                            tk.Label(scrollable_frame, text="Error al cargar imagen").grid(row=i, column=2, padx=5, pady=5)
                    else:
                        tk.Label(scrollable_frame, text="Sin imagen").grid(row=i, column=2, padx=5, pady=5)

                # Empaquetar el canvas y la barra de desplazamiento
                canvas.pack(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")

            except mysql.connector.Error as e:
                messagebox.showerror("Error en la consulta", str(e), parent=ventana_sintoma)
            finally:
                cursor.close()
                conexion.close()


    def consulta_individual():
        nombre_consulta = simpledialog.askstring("Consulta Individual", "Ingrese el síntoma:", parent=ventana_sintoma)
        if nombre_consulta:
            conexion = conectar_db()
            if conexion:
                cursor = conexion.cursor()
                try:
                    cursor.execute("SELECT id_sintoma, sintoma, imagen_path FROM sintomas WHERE sintoma = %s", (nombre_consulta,))
                    resultado = cursor.fetchone()

                    if resultado:
                        # Crear una nueva ventana para mostrar el resultado
                        ventana_resultado = tk.Toplevel(ventana_sintoma)
                        ventana_resultado.title(f"Síntoma: {nombre_consulta}")
                        ventana_resultado.geometry("1000x300")
                        ventana_resultado.configure(bg="#F0F0F0")

                        # Crear un frame para contener el canvas y la barra de desplazamiento
                        frame = tk.Frame(ventana_resultado)
                        frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

                        # Crear un canvas y un frame interior para el scrolling
                        canvas = tk.Canvas(frame)
                        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
                        scrollable_frame = tk.Frame(canvas)

                        scrollable_frame.bind(
                            "<Configure>",
                            lambda e: canvas.configure(
                                scrollregion=canvas.bbox("all")
                            )
                        )

                        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                        canvas.configure(yscrollcommand=scrollbar.set)

                        # Crear etiquetas para los encabezados
                        tk.Label(scrollable_frame, text="ID", font=('Helvetica', 16, 'bold'), width=10).grid(row=0, column=0, padx=5, pady=5)
                        tk.Label(scrollable_frame, text="Síntoma", font=('Helvetica', 16, 'bold'), width=20).grid(row=0, column=1, padx=5, pady=5)
                        tk.Label(scrollable_frame, text="Imagen", font=('Helvetica', 16, 'bold'), width=20).grid(row=0, column=2, padx=5, pady=5)

                        # Insertar los datos del objeto en la fila correspondiente
                        id, sintoma, imagen_path = resultado
                        tk.Label(scrollable_frame, text=id, width=10, font=("Arial", 14)).grid(row=1, column=0, padx=5, pady=5)
                        tk.Label(scrollable_frame, text=sintoma, width=40, anchor="center", font=("Arial", 14)).grid(row=1, column=1, padx=5, pady=5)

                        # Mostrar la imagen si existe
                        if imagen_path:
                            try:
                                img = Image.open(imagen_path)
                                img = img.resize((150, 150), Image.LANCZOS)
                                photo = ImageTk.PhotoImage(img)
                                img_label = tk.Label(scrollable_frame, image=photo)
                                img_label.image = photo  # Mantener una referencia
                                img_label.grid(row=1, column=2, padx=5, pady=5)
                            except Exception as e:
                                tk.Label(scrollable_frame, text="Error al cargar imagen").grid(row=1, column=2, padx=5, pady=5)
                        else:
                            tk.Label(scrollable_frame, text="Sin imagen").grid(row=1, column=2, padx=5, pady=5)

                        # Empaquetar el canvas y la barra de desplazamiento
                        canvas.pack(side="left", fill="both", expand=True)
                        scrollbar.pack(side="right", fill="y")

                    else:
                        messagebox.showinfo("Sin resultado", f"No se encontró el síntoma '{nombre_consulta}' en la base de datos.", parent=ventana_sintoma)

                except mysql.connector.Error as e:
                    messagebox.showerror("Error en la consulta", str(e), parent=ventana_sintoma)
                finally:
                    cursor.close()
                    conexion.close()

    
 

    ventana_sintoma.configure(bg="#00BFBF")
    titulo_label = tk.Label(ventana_sintoma, text="DATOS SÍNTOMAS", font=("Trebuchet MS", 50, "bold"), bg="#00BFBF")
    titulo_label.place(x=530, y=40)

    # Labels y Entries para los datos del objeto
    tk.Label(ventana_sintoma, text="Nombre_síntoma:", font=("Trebuchet MS", 20), bg="#00BFBF").place(x=250, y=250)
    nombre_entry = tk.Entry(ventana_sintoma, font=("Trebuchet MS", 18))
    nombre_entry.place(x=250, y=300, width=500, height=50)

    imagen_label = tk.Label(ventana_sintoma, bg="white")
    imagen_label.place(x=950, y=150, width=350, height=350)

    cargar_imagen_button = tk.Button(
        ventana_sintoma,
        text="Cargar Imagen",
        command=lambda: cargar_y_mostrar_imagen(imagen_label),
        font=("Georgia", 18, "bold"),
        bg="#6A70FE",
        width=12
    )
    cargar_imagen_button.place(x=1100, y=150)

    def guardar_objeto():
        global imagen_path, indice_actual, objetos

        nombre_objeto = nombre_entry.get()

        if not nombre_objeto or not imagen_path:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios", parent=ventana_sintoma)
            return

        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            try:
                # Verificar si el nombre ya existe en la base de datos
                cursor.execute("SELECT COUNT(*) FROM sintomas WHERE sintoma = %s", (nombre_objeto,))
                (count,) = cursor.fetchone()
                
                if count > 0:
                    messagebox.showwarning("Nombre duplicado", "El nombre del síntoma ya existe. Introduce uno diferente.", parent=ventana_sintoma)
                    return

                # Insertar el nuevo síntoma
                cursor.execute("""
                    INSERT INTO sintomas (sintoma, imagen_path)
                    VALUES (%s, %s)
                """, (nombre_objeto, imagen_path))

                conexion.commit()
                messagebox.showinfo("Éxito", "Síntoma agregado exitosamente", parent=ventana_sintoma)
                
                # Recargar los objetos desde la base de datos
                cargar_objetos_desde_db()

                # Actualizar el índice actual al último objeto (el recién agregado)
                indice_actual = len(objetos) - 1
                mostrar_objeto(indice_actual)

            except mysql.connector.Error as e:
                messagebox.showerror("Error al agregar", str(e), parent=ventana_sintoma)
            finally:
                cursor.close()
                conexion.close()

    def modificar():
        global indice_actual, objetos, imagen_path

        if not objetos:
            messagebox.showwarning("No hay objetos", "No hay objetos para modificar.", parent=ventana_sintoma)
            return

        nuevo_nombre = nombre_entry.get()
        objeto_actual = objetos[indice_actual]

        # Verificar si hay cambios
        if (nuevo_nombre == objeto_actual[0] and imagen_path == objeto_actual[1]):
            messagebox.showinfo("Sin cambios", "No se han realizado modificaciones.", parent=ventana_sintoma)
            return

        # Preguntar al usuario si está seguro de modificar
        confirmacion = messagebox.askyesno("Confirmar modificación", 
                                            f"¿Está seguro que desea modificar el síntoma '{objeto_actual[0]}'?", 
                                            parent=ventana_sintoma)
        
        if confirmacion:
            conexion = conectar_db()
            if conexion:
                cursor = conexion.cursor()
                try:
                    cursor.execute("""
                        UPDATE sintomas 
                        SET sintoma = %s, imagen_path = %s
                        WHERE sintoma = %s
                    """, (nuevo_nombre, imagen_path, objeto_actual[0]))
                    
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Síntoma modificado exitosamente", parent=ventana_sintoma)
                    
                    # Actualizar la lista de objetos y mostrar el objeto modificado
                    cargar_objetos_desde_db()
                    for i, obj in enumerate(objetos):
                        if obj[0] == nuevo_nombre:
                            indice_actual = i
                            break
                    mostrar_objeto(indice_actual)
                except mysql.connector.Error as e:
                    messagebox.showerror("Error al modificar", str(e), parent=ventana_sintoma)
                finally:
                    cursor.close()
                    conexion.close()


    # Botón para avanzar a la siguiente entrada
    button_adelante = tk.Button(ventana_sintoma, text="Adelante", command=mover_adelante, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_adelante.place(x=210, y=550)

    # Botón para retroceder a la entrada anterior
    button_atras = tk.Button(ventana_sintoma, text="Atras", command=mover_atras, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_atras.place(x=510, y=550)

    # Botón para ir al inicio de la lista
    button_inicio = tk.Button(ventana_sintoma, text="Inicio", command=ir_a_inicio, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_inicio.place(x=810, y=550)

    # Botón para ir al final de la lista
    button_final = tk.Button(ventana_sintoma, text="Final", command=ir_a_final, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_final.place(x=1110, y=550)

    # Cargar los objetos desde la base de datos al iniciar la ventana
    cargar_objetos_desde_db()
    if objetos:
        # Retrasar la carga de la primera imagen
        ventana_sintoma.after(100, lambda: mostrar_objeto(indice_actual))

    # Botón para agregar un nuevo objeto (sintoma)
    agregar_button = tk.Button(ventana_sintoma, text="Altas", command=guardar_objeto, font=("Georgia", 24, "bold"), bg="#6A70FE", width=10)
    agregar_button.place(x=110, y=650)

    # Botón para eliminar un objeto (sintoma)
    eliminar_button = tk.Button(ventana_sintoma, text="Bajas eliminar", command=eliminar_objeto, font=("Georgia", 24, "bold"), bg="#FF6961", width=12)
    eliminar_button.place(x=380, y=650)

    # Botón para realizar consultas sobre los objetos
    consultas_button = tk.Button(ventana_sintoma, text="Consultas", command=realizar_consulta, font=("Georgia", 24, "bold"), bg="green", width=10)
    consultas_button.place(x=690, y=650)

    # Botón para modificar un objeto existente
    Modificar_button = tk.Button(ventana_sintoma, text="Modificar", command=modificar, font=("Georgia", 24, "bold"), bg="#FFD700", width=10)
    Modificar_button.place(x=950, y=650)

    # Botón para salir de la aplicación
    btn_regresar = tk.Button(ventana_sintoma, text="Salir", command=ventana_sintoma.destroy, font=("Georgia", 24, "bold"), bg="#FF6B6B", width=10)
    btn_regresar.place(x=1210, y=650)



def agregar_objeto():
    global objetos, indice_actual, imagen_path 
    ventana_agregarobj = tk.Toplevel(root)
    ventana_agregarobj.title("Agregar obj")
    ventana_agregarobj.attributes("-fullscreen", True)
    
    imagen_path = ""  
    objetos = []  
    indice_actual = 0  


    def cargar_objetos_desde_db():
        global objetos
        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT nombre_objeto, descripcion, imagen_path FROM enfermedades")
                objetos = cursor.fetchall() 
            except mysql.connector.Error as e:
                messagebox.showerror("Error al cargar", str(e), parent=ventana_agregarobj)
            finally:
                cursor.close()
                conexion.close()

    def cargar_y_mostrar_imagen(label, ruta=None, tamano_maximo=(340, 340)):
        global imagen_path 

        if not ruta:
            ruta = filedialog.askopenfilename(
                parent=ventana_agregarobj,
                title="Seleccionar Imagen",
                filetypes=[("Archivos de Imagen", "*.jpg;*.jpeg;*.png;*.gif")]
            )

        if not ruta:
            return 

        imagen_path = ruta 

        imagen_original = Image.open(ruta)
        
        ancho_label, alto_label = tamano_maximo
        
        relacion_aspecto = min(ancho_label / imagen_original.width, alto_label / imagen_original.height)
        nuevo_ancho = int(imagen_original.width * relacion_aspecto)
        nuevo_alto = int(imagen_original.height * relacion_aspecto)
        
        imagen_redimensionada = imagen_original.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
        
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        
        label.config(image=imagen_tk)
        label.image = imagen_tk 

        return ruta

    def mostrar_objeto(indice):
        global objetos, imagen_path
        if objetos:
            nombre_objeto, descripcion, imagen_path = objetos[indice]
            nombre_entry.delete(0, tk.END)
            nombre_entry.insert(0, nombre_objeto)

            descripcion_text.delete("1.0", tk.END)
            descripcion_text.insert("1.0", descripcion)

            ventana_agregarobj.update_idletasks()
            cargar_y_mostrar_imagen(imagen_label, ruta=imagen_path)

    def mover_adelante():
        global indice_actual, objetos
        if not objetos:
            messagebox.showinfo("Sin objetos", "No hay objetos para mostrar.", parent=ventana_agregarobj)
            return
        if indice_actual < len(objetos) - 1:
            indice_actual += 1
            mostrar_objeto(indice_actual)
        else:
            messagebox.showinfo("Fin alcanzado", "Ya no hay más objetos. Este es el último.", parent=ventana_agregarobj)


    def mover_atras():
        global indice_actual, objetos
        if not objetos:
            messagebox.showinfo("Sin objetos", "No hay objetos para mostrar.", parent=ventana_agregarobj)
            return
        if indice_actual > 0:
            indice_actual -= 1
            mostrar_objeto(indice_actual)
        else:
            messagebox.showinfo("Inicio alcanzado", "Ya estás en el primer objeto. No hay nada más atrás.", parent=ventana_agregarobj)

    def ir_a_inicio():
        global indice_actual, objetos
        if not objetos:
            messagebox.showinfo("Sin objetos", "No hay objetos para mostrar.", parent=ventana_agregarobj)
            return
        if indice_actual == 0:
            messagebox.showinfo("Ya en el inicio", "Ya estás en el primer objeto.", parent=ventana_agregarobj)
        else:
            indice_actual = 0
            mostrar_objeto(indice_actual)
    def ir_a_final():
        global indice_actual, objetos
        if not objetos:
            messagebox.showinfo("Sin objetos", "No hay objetos para mostrar.", parent=ventana_agregarobj)
            return
        if indice_actual == len(objetos) - 1:
            messagebox.showinfo("Ya en el final", "Ya estás en el último objeto.", parent=ventana_agregarobj)
        else:
            indice_actual = len(objetos) - 1
            mostrar_objeto(indice_actual)
    def eliminar_objeto():
        global indice_actual, objetos
        if not objetos:
            messagebox.showwarning("No hay objetos", "No hay objetos para eliminar.", parent=ventana_agregarobj)
            return

        objeto_actual = objetos[indice_actual]
        confirmacion = messagebox.askyesno("Confirmar eliminación", 
                                           f"¿Está seguro que desea eliminar la enfermedad '{objeto_actual[0]}'?", 
                                           parent=ventana_agregarobj)
        
        if confirmacion:
            conexion = conectar_db()
            if conexion:
                cursor = conexion.cursor()
                try:
                    cursor.execute("DELETE FROM enfermedades WHERE nombre_objeto = %s", (objeto_actual[0],))
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Enfermedad eliminada exitosamente", parent=ventana_agregarobj)
                    
                    cargar_objetos_desde_db()
                    if objetos:
                        if indice_actual >= len(objetos):
                            indice_actual = len(objetos) - 1
                        mostrar_objeto(indice_actual)
                    else:
                        nombre_entry.delete(0, tk.END)
                        descripcion_text.delete("1.0", tk.END)
                        imagen_label.config(image="")
                except mysql.connector.Error as e:
                    messagebox.showerror("Error al eliminar", str(e), parent=ventana_agregarobj)
                finally:
                    cursor.close()
                    conexion.close()

    def realizar_consulta():
        tipo_consulta = messagebox.askquestion("Tipo de Consulta", "¿Desea realizar una consulta general?",
                                               icon='question',parent=ventana_agregarobj)
        if tipo_consulta == 'yes':
            consulta_general()
        else:
            consulta_individual()

    def consulta_general():
        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT id_enfermedad, nombre_objeto, descripcion, imagen_path FROM enfermedades")
                resultados = cursor.fetchall()

                # Crear una nueva ventana para mostrar los resultados
                ventana_resultados = tk.Toplevel(ventana_agregarobj)
                ventana_resultados.title("Consulta General")
                ventana_resultados.geometry("1100x600")
                ventana_resultados.configure(bg="#F0F0F0")

                # Estilo personalizado para el Treeview
                style = ttk.Style()
                style.theme_use("clam")
                style.configure("Treeview", background="#D3D3D3",
                                fieldbackground="#D3D3D3", foreground="black")
                style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))

                frame = tk.Frame(ventana_resultados)
                frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

                canvas = tk.Canvas(frame)
                scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
                scrollable_frame = tk.Frame(canvas)

                scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )

                canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                canvas.configure(yscrollcommand=scrollbar.set)

                tk.Label(scrollable_frame, text="Enfermedades", font=('Helvetica', 20, 'bold')).grid(row=0, column=0, columnspan=4, pady=10)

                # Crear etiquetas para los encabezados en la fila 1
                tk.Label(scrollable_frame, text="ID", font=('Helvetica', 16, 'bold'), width=10).grid(row=1, column=0, padx=5, pady=5)
                tk.Label(scrollable_frame, text="Nombre", font=('Helvetica', 16, 'bold'), width=20).grid(row=1, column=1, padx=5, pady=5)
                tk.Label(scrollable_frame, text="Descripción", font=('Helvetica', 16, 'bold'), width=30).grid(row=1, column=2, padx=5, pady=5)
                tk.Label(scrollable_frame, text="Imagen", font=('Helvetica', 16, 'bold'), width=20).grid(row=1, column=3, padx=5, pady=5)

                # Insertar los datos en el frame
                for i, row in enumerate(resultados, start=2):  # Iniciar en la fila 2 para los datos
                    id, nombre, descripcion, imagen_path = row
                    tk.Label(scrollable_frame, text=id, width=10, font=("Arial", 14)).grid(row=i, column=0, padx=5, pady=5)
                    tk.Label(scrollable_frame, text=nombre, width=20, anchor="center", font=("Arial", 14)).grid(row=i, column=1, padx=5, pady=5)
                    tk.Label(scrollable_frame, text=descripcion, width=30, anchor="center", wraplength=300, font=("Arial", 14)).grid(row=i, column=2, padx=5, pady=5)

                    if imagen_path:
                        try:
                            img = Image.open(imagen_path)
                            img = img.resize((150, 150), Image.LANCZOS)
                            photo = ImageTk.PhotoImage(img)
                            img_label = tk.Label(scrollable_frame, image=photo)
                            img_label.image = photo  # Mantener una referencia
                            img_label.grid(row=i, column=3, padx=5, pady=5)
                        except Exception as e:
                            tk.Label(scrollable_frame, text="Error al cargar imagen").grid(row=i, column=3, padx=5, pady=5)
                    else:
                        tk.Label(scrollable_frame, text="Sin imagen").grid(row=i, column=3, padx=5, pady=5)

                # Empaquetar el canvas y la barra de desplazamiento
                canvas.pack(side="left", fill="both", expand=True)
                scrollbar.pack(side="right", fill="y")

            except mysql.connector.Error as e:
                messagebox.showerror("Error en la consulta", str(e), parent=ventana_agregarobj)
            finally:
                cursor.close()
                conexion.close()


    def consulta_individual():
        nombre_consulta = simpledialog.askstring("Consulta Individual", "Ingrese el nombre de la enfermedad:", parent=ventana_agregarobj)
        if nombre_consulta:
            conexion = conectar_db()
            if conexion:
                cursor = conexion.cursor()
                try:
                    cursor.execute("SELECT id_enfermedad, nombre_objeto, descripcion, imagen_path FROM enfermedades WHERE nombre_objeto = %s", (nombre_consulta,))
                    resultado = cursor.fetchone()
                    
                    if resultado:
                        # Crear una nueva ventana para mostrar el resultado
                        ventana_resultado = tk.Toplevel(ventana_agregarobj)
                        ventana_resultado.title(f"Enfermedad: {nombre_consulta}")
                        ventana_resultado.geometry("1100x300")
                        ventana_resultado.configure(bg="#F0F0F0")

                        # Crear un frame para contener el canvas y la barra de desplazamiento
                        frame = tk.Frame(ventana_resultado)
                        frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

                        # Crear un canvas y un frame interior para el scrolling
                        canvas = tk.Canvas(frame)
                        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
                        scrollable_frame = tk.Frame(canvas)

                        scrollable_frame.bind(
                            "<Configure>",
                            lambda e: canvas.configure(
                                scrollregion=canvas.bbox("all")
                            )
                        )

                        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
                        canvas.configure(yscrollcommand=scrollbar.set)

                        # Crear etiquetas para los encabezados
                        tk.Label(scrollable_frame, text="ID", font=('Helvetica', 16, 'bold'), width=10).grid(row=0, column=0, padx=5, pady=5)
                        tk.Label(scrollable_frame, text="Nombre", font=('Helvetica', 16, 'bold'), width=20).grid(row=0, column=1, padx=5, pady=5)
                        tk.Label(scrollable_frame, text="Descripción", font=('Helvetica', 16, 'bold'), width=30).grid(row=0, column=2, padx=5, pady=5)
                        tk.Label(scrollable_frame, text="Imagen", font=('Helvetica', 16, 'bold'), width=20).grid(row=0, column=3, padx=5, pady=5)

                        # Insertar los datos del objeto en la fila correspondiente
                        id, nombre, descripcion, imagen_path = resultado
                        tk.Label(scrollable_frame, text=id, width=10, font=("Arial", 14)).grid(row=1, column=0, padx=5, pady=5)
                        tk.Label(scrollable_frame, text=nombre, width=20, anchor="center", font=("Arial", 14)).grid(row=1, column=1, padx=5, pady=5)
                        tk.Label(scrollable_frame, text=descripcion, width=30, anchor="center", wraplength=300, font=("Arial", 14)).grid(row=1, column=2, padx=5, pady=5)

                        # Mostrar la imagen si existe
                        if imagen_path:
                            try:
                                img = Image.open(imagen_path)
                                img = img.resize((150, 150), Image.LANCZOS)
                                photo = ImageTk.PhotoImage(img)
                                img_label = tk.Label(scrollable_frame, image=photo)
                                img_label.image = photo  # Mantener una referencia
                                img_label.grid(row=1, column=3, padx=5, pady=5)
                            except Exception as e:
                                tk.Label(scrollable_frame, text="Error al cargar imagen").grid(row=1, column=3, padx=5, pady=5)
                        else:
                            tk.Label(scrollable_frame, text="Sin imagen").grid(row=1, column=3, padx=5, pady=5)

                        # Empaquetar el canvas y la barra de desplazamiento
                        canvas.pack(side="left", fill="both", expand=True)
                        scrollbar.pack(side="right", fill="y")

                    else:
                        messagebox.showinfo("No encontrado", f"No se encontró ningúna enfermedad con el nombre {nombre_consulta}", parent=ventana_agregarobj)

                except mysql.connector.Error as e:
                    messagebox.showerror("Error en la consulta", str(e), parent=ventana_agregarobj)
                finally:
                    cursor.close()
                    conexion.close()


    ventana_agregarobj.configure(bg="#00BFBF")
    titulo_label = tk.Label(ventana_agregarobj, text="DATOS ENFERMEDADES", font=("Trebuchet MS", 50, "bold"), bg="#00BFBF")
    titulo_label.place(x=530, y=40)

    tk.Label(ventana_agregarobj, text="Nombre_enfermedad:", font=("Trebuchet MS", 20), bg="#00BFBF").place(x=250, y=150)
    nombre_entry = tk.Entry(ventana_agregarobj, font=("Trebuchet MS", 18))
    nombre_entry.place(x=250, y=200)

    tk.Label(ventana_agregarobj, text="Descripción:", font=("Trebuchet MS", 20), bg="#00BFBF").place(x=250, y=235)

    frame = tk.Frame(ventana_agregarobj)
    frame.place(x=250, y=280)

    descripcion_text = tk.Text(frame, font=("Trebuchet MS", 18), height=7, width=35)
    descripcion_text.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(frame, command=descripcion_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    descripcion_text.config(yscrollcommand=scrollbar.set)

    imagen_label = tk.Label(ventana_agregarobj, bg="white")
    imagen_label.place(x=950, y=150, width=350, height=350)

    cargar_imagen_button = tk.Button(
        ventana_agregarobj,
        text="Cargar Imagen",
        command=lambda: cargar_y_mostrar_imagen(imagen_label),
        font=("Georgia", 18, "bold"),
        bg="#6A70FE",
        width=12
    )
    cargar_imagen_button.place(x=1100, y=150)

    def guardar_objeto():
        global imagen_path, indice_actual, objetos

        nombre_objeto = nombre_entry.get()
        descripcion = descripcion_text.get("1.0", tk.END).strip()

        if not nombre_objeto or not descripcion or not imagen_path:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios", parent=ventana_agregarobj)
            return

        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            try:
                cursor.execute("SELECT COUNT(*) FROM enfermedades WHERE nombre_objeto = %s", (nombre_objeto,))
                (count,) = cursor.fetchone()
                
                if count > 0:
                    messagebox.showwarning("Nombre duplicado", "El nombre de la enfermedad ya existe. Introduce uno diferente.", parent=ventana_agregarobj)
                    return

                cursor.execute("""
                    INSERT INTO enfermedades (nombre_objeto, descripcion, imagen_path)
                    VALUES (%s, %s, %s)
                """, (nombre_objeto, descripcion, imagen_path))

                conexion.commit()
                messagebox.showinfo("Éxito", "Enfermedad agregada exitosamente", parent=ventana_agregarobj)
                
                cargar_objetos_desde_db()

                indice_actual = len(objetos) - 1
                mostrar_objeto(indice_actual)

            except mysql.connector.Error as e:
                messagebox.showerror("Error al agregar", str(e), parent=ventana_agregarobj)
            finally:
                cursor.close()
                conexion.close()


    def modificar():
        global indice_actual, objetos, imagen_path

        if not objetos:
            messagebox.showwarning("No hay objetos", "No hay objetos para modificar.", parent=ventana_agregarobj)
            return

        nuevo_nombre = nombre_entry.get()
        nueva_descripcion = descripcion_text.get("1.0", tk.END).strip()
        objeto_actual = objetos[indice_actual]

        if (nuevo_nombre == objeto_actual[0] and
            nueva_descripcion == objeto_actual[1] and
            imagen_path == objeto_actual[2]):
            messagebox.showinfo("Sin cambios", "No se han realizado modificaciones.", parent=ventana_agregarobj)
            return

        confirmacion = messagebox.askyesno("Confirmar modificación", 
                                        f"¿Está seguro que desea modificar la enfermedad '{objeto_actual[0]}'?", 
                                        parent=ventana_agregarobj)
        
        if confirmacion:
            conexion = conectar_db()
            if conexion:
                cursor = conexion.cursor()
                try:
                    cursor.execute("""
                        UPDATE enfermedades 
                        SET nombre_objeto = %s, descripcion = %s, imagen_path = %s
                        WHERE nombre_objeto = %s
                    """, (nuevo_nombre, nueva_descripcion, imagen_path, objeto_actual[0]))
                    
                    conexion.commit()
                    messagebox.showinfo("Éxito", "Enfermedad modificado exitosamente", parent=ventana_agregarobj)
                    
                    cargar_objetos_desde_db()
                    for i, obj in enumerate(objetos):
                        if obj[0] == nuevo_nombre:
                            indice_actual = i
                            break
                    mostrar_objeto(indice_actual)
                except mysql.connector.Error as e:
                    messagebox.showerror("Error al modificar", str(e), parent=ventana_agregarobj)
                finally:
                    cursor.close()
                    conexion.close()

    button_adelante = tk.Button(ventana_agregarobj, text="Adelante", command=mover_adelante, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_adelante.place(x=210, y=550)

    button_atras = tk.Button(ventana_agregarobj, text="Atras", command=mover_atras, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_atras.place(x=510, y=550)
    
    button_inicio = tk.Button(ventana_agregarobj, text="Inicio", command=ir_a_inicio, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_inicio.place(x=810, y=550)

    button_final = tk.Button(ventana_agregarobj, text="Final", command=ir_a_final, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_final.place(x=1110, y=550)

    
    cargar_objetos_desde_db()
    if objetos:
        ventana_agregarobj.after(100, lambda: mostrar_objeto(indice_actual))

    button_inicio = tk.Button(ventana_agregarobj, text="Inicio", command=ir_a_inicio, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_inicio.place(x=810, y=550)

    button_final = tk.Button(ventana_agregarobj, text="Final", command=ir_a_final, font=("Georgia", 18, "bold"), bg="gray70", width=10)
    button_final.place(x=1110, y=550)

    agregar_button = tk.Button(ventana_agregarobj, text="Altas", command=guardar_objeto, font=("Georgia", 24, "bold"), bg="#6A70FE", width=10)
    agregar_button.place(x=110, y=650)

    eliminar_button = tk.Button(ventana_agregarobj, text="Bajas eliminar", command=eliminar_objeto, font=("Georgia", 24, "bold"), bg="#FF6961", width=12)
    eliminar_button.place(x=380, y=650)

    consultas_button = tk.Button(ventana_agregarobj, text="Consultas", command=realizar_consulta, font=("Georgia", 24, "bold"), bg="green", width=10)
    consultas_button.place(x=690, y=650)

    Modificar_button = tk.Button(ventana_agregarobj, text="Modificar", command=modificar, font=("Georgia", 24, "bold"), bg="#FFD700", width=10)
    Modificar_button.place(x=950, y=650)
    
    btn_regresar = tk.Button(ventana_agregarobj,text="Salir", command=ventana_agregarobj.destroy,font=("Georgia", 24, "bold"),bg="lightcoral",width=10)  # Elimina el bordeborderwidth=0,  # Elimina el ancho del borde
    btn_regresar.place(x=1210, y=650)



ventana_menu_expe = None 

def mostrar_menu_experto():
    global ventana_menu_expe

    ventana_menu_expe = tk.Toplevel(root)
    ventana_menu_expe.title("MENU EXPERTO")
    ventana_menu_expe.attributes("-fullscreen", True)
        
    ventana_menu_expe.configure(bg="#00BFBF")
    titulo_label = tk.Label(ventana_menu_expe, text="MENU EXPERTO", font=("Trebuchet MS", 50, "bold"), bg="#00BFBF")
    titulo_label.place(x=550,y=40)

        
    agregarobj = tk.Button(ventana_menu_expe, text="Agregar enfermedad", command=agregar_objeto, font=("Georgia", 24, "bold"), bg="#6A70FE", width=20)
    agregarobj.place(x=620, y=350)

    agregarCarac= tk.Button(ventana_menu_expe, text="Agregar sintomas", command=agregar_sintomas,font=("Georgia", 24, "bold"),bg="#BFBF00", width=20)
    agregarCarac.place(x=620,y=450)

    cuadroRelacion = tk.Button(ventana_menu_expe, text="Cuadro-Relación", command=abrir_cuadro_relacion, font=("Georgia", 24, "bold"), bg="darkturquoise", width=20)
    cuadroRelacion.place(x=620, y=550)

    btn_regresar = tk.Button(ventana_menu_expe,text="Regresar", command=ventana_menu_expe.destroy,font=("Georgia", 24, "bold"),bg="lightcoral",width=15)  # Elimina el bordeborderwidth=0,  # Elimina el ancho del borde
    btn_regresar.place(x=1100, y=750)

   
    imagen = Image.open("imagenes/actual.png") 
    imagen = imagen.resize((55, 55))
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_menu_expe, image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.place(x=550, y=355) 
    imagen = Image.open("imagenes/integracion.png")  
    imagen = imagen.resize((55, 55))
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_menu_expe, image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.place(x=550, y=455) 
    imagen = Image.open("imagenes/futuro.png") 
    imagen = imagen.resize((55, 55))
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_menu_expe, image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.place(x=550, y=555) 

from interfazUsuario import interfaz_usuario

def interfaces():
    ventana_interfaces = tk.Toplevel(root)
    ventana_interfaces.title("Entrar")
    ventana_interfaces.attributes("-fullscreen", True)
    
    # Título
    ventana_interfaces.configure(bg="#6FB0B5")
    titulo_label = tk.Label( ventana_interfaces, text="Interfaces", font=("Tahoma", 64, "bold"), fg="black", bd=19)
    titulo_label.place(x=100,y=100)

    def pedir_contraseña():
        contraseña_correcta = "" 
        contraseña_ingresada = simpledialog.askstring("Contraseña", "Ingrese la contraseña:", show='*')

        if contraseña_ingresada == contraseña_correcta:
            messagebox.showinfo("Acceso concedido", "La contraseña es correcta", parent=ventana_interfaces)
            mostrar_menu_experto()  
        else:
            messagebox.showerror("Contraseña incorrecta", "La contraseña ingresada es incorrecta, vuelve a intentarlo")

    def abrir_interfaz_usuario():
        ventana_interfaces.withdraw() 
        interfaz_usuario(ventana_interfaces)  
            

    experto = tk.Button( ventana_interfaces, text="Experto   ", command=pedir_contraseña, font=("Georgia", 24, "bold"), bg="#6A70FE", width=15)
    experto.place(x=620, y=350)

    usuario = tk.Button(ventana_interfaces, text="Usuario   ", command=abrir_interfaz_usuario, font=("Georgia", 24, "bold"), bg="#BFBF00", width=15)
    usuario.place(x=620,y=450)

    btn_regresar = tk.Button(ventana_interfaces,text="Regresar", command=ventana_interfaces.destroy,font=("Georgia", 24, "bold"),bg="#FF6B6B",width=15)  # Elimina el bordeborderwidth=0,  # Elimina el ancho del borde
    btn_regresar.place(x=1100, y=700)

    imagen = Image.open("imagenes/actual.png")  
    imagen = imagen.resize((55, 55))
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_interfaces, image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.place(x=550, y=355) 
    imagen = Image.open("imagenes/integracion.png") 
    imagen = imagen.resize((55, 55))
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_interfaces, image=imagen_tk)
    imagen_label.image = imagen_tk
    imagen_label.place(x=550, y=455) 

def abrir_cuadro_relacion():
    ventana_menu_expe.withdraw()  
    import cuadroRelacion  
    cuadroRelacion.abrir_cuadro_relacion(ventana_menu_expe)  


#PAGINA PRINCIPAL
def cargar_imagen_izquierda():
    imagen_izquierda = tk.PhotoImage(file="imagenes/descarga2.png")  
    imagen_izquierda = imagen_izquierda.subsample(7)
    imagen_label_izquierda = tk.Label(root, image=imagen_izquierda)
    imagen_label_izquierda.image = imagen_izquierda
    imagen_label_izquierda.place(x=100, y=10)  

def cargar_imagen_derecha():
    imagen_derecha = tk.PhotoImage(file="imagenes/descarga1.png")  
    imagen_derecha = imagen_derecha.subsample(1)  
    imagen_label_derecha = tk.Label(root, image=imagen_derecha)
    imagen_label_derecha.image = imagen_derecha
    imagen_label_derecha.place(x=1200, y=10)


if __name__ == "__main__":
    root = tk.Tk()

    root.attributes("-fullscreen", True)

    root.minsize(800, 500)

    root.title("Tarea")
    root.iconbitmap("imagenes/pagina-de-inicio.ico")  


    fondo_imagen = Image.open("imagenes/itz.png") 
    fondo_photo = ImageTk.PhotoImage(fondo_imagen)

    fondo_label = tk.Label(root, image=fondo_photo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    texto = tk.Label(root, text="BIENVENIDOS\n INSTITUTO TECNOLÓGICO DE ZACATEPEC", font=("Comic Sans MS", 26, "bold"), bg="#FAEBD7")
    texto.pack(pady=160)

    cargar_imagen_izquierda()
    cargar_imagen_derecha()

    texto = tk.Label(root, text="SISTEMA EXPERTO PARA EL \nDIAGNOSTICO DE \nENFERMEDADES", font=("Comic Sans MS", 40, "bold"), bg="#FAEBD7")
    texto.pack(pady=10)

    logo_acerca_de = cargar_img("imagenes/informacion.png")
    logo_entrar= cargar_img("imagenes/mapa-marcador-inicio.png")
    logo_salir = cargar_img("imagenes/dejar.png")
    logo_autor = cargar_img("imagenes/derechos-de-autor.png")

    btn_acerca_de = tk.Button(root, text="Acerca de", command=abrir_ventana_acerca_de, font=("Comic Sans MS", 19, "bold"), bg="yellow", image=logo_acerca_de, compound="left")
    btn_acerca_de.place(x=1300, y=600)

    btn_entrar = tk.Button(root, text="Entrar    ", command=interfaces, font=("Comic Sans MS", 19, "bold"), bg="lime green", image=logo_entrar, compound="left")
    btn_entrar.place(x=1300, y=700)

    btn_salir = tk.Button(root, text="Salir     ", command=salir, font=("Comic Sans MS", 19, "bold"), bg="#FF6B6B", image=logo_salir, compound="left")
    btn_salir.place(x=100, y=750)

    root.mainloop()