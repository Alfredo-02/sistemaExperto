import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import tkinter.font as tkFont
import mysql.connector
from cuadroRelacion import conectar_db, cargar_y_mostrar_imagen

def obtener_sintomas():
    conexion = conectar_db()
    if conexion is None:
        return []

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT sintoma FROM sintomas ORDER BY sintoma")
        sintomas = [fila[0] for fila in cursor.fetchall()]
        cursor.close()
        return sintomas
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron cargar los síntomas: {str(e)}")
        return []
    finally:
        if conexion:
            conexion.close()

def abrir_busqueda_sintomas(ventana_anterior):
    ventana_sintomas = tk.Toplevel()
    ventana_sintomas.title("Búsqueda por Síntomas")
    ventana_sintomas.attributes("-fullscreen", True)
    ventana_sintomas.configure(bg="#00BFBF")

    # Título
    titulo_label = tk.Label(ventana_sintomas, 
                          text="BÚSQUEDA POR SÍNTOMAS", 
                          font=("Trebuchet MS", 50, "bold"), 
                          bg="#00BFBF")
    titulo_label.place(x=530, y=40)

    # ComboBox para síntomas
    fuente = tkFont.Font(family="Trebuchet MS", size=15)
    style = ttk.Style()
    style.configure("TCombobox", font=fuente)

    # Etiqueta para síntomas
    label_sintomas = tk.Label(ventana_sintomas, text="Síntomas", font=("Trebuchet MS", 18))
    label_sintomas.place(x=250, y=210)  # Posición de la etiqueta

    # ComboBox para síntomas
    sintomas = obtener_sintomas()
    combo_sintomas = ttk.Combobox(ventana_sintomas, 
                                values=sintomas, 
                                state="readonly", 
                                font=("Trebuchet MS", 18))
    combo_sintomas.place(x=250, y=250, width=500, height=40)

    # Label para la imagen
    imagen_label = tk.Label(ventana_sintomas, bg="white")
    imagen_label.place(x=950, y=150, width=350, height=350)

    # Tabla de síntomas seleccionados
    style.configure("Treeview", 
                   font=("Trebuchet MS", 15),
                   rowheight=30)
    style.configure("Treeview.Heading", 
                   font=("Trebuchet MS", 15, "bold"), 
                   background="lightblue", 
                   foreground="black")

    frame_tabla = tk.Frame(ventana_sintomas, bg="#00BFBF")
    frame_tabla.place(x=250, y=350)

    tabla = ttk.Treeview(frame_tabla, 
                        columns=("Síntoma",), 
                        show="headings", 
                        height=8)
    tabla.heading("Síntoma", text="Síntomas Seleccionados")
    tabla.column("Síntoma", width=500, anchor="center")
    tabla.pack(side=tk.LEFT)

    # Scrollbar para la tabla
    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    tabla.configure(yscrollcommand=scrollbar.set)

    def mostrar_imagen(sintoma):
        """Función unificada para mostrar imagen de un síntoma"""
        if sintoma:
            conexion = conectar_db()
            if conexion:
                try:
                    cursor = conexion.cursor()
                    cursor.execute("SELECT imagen_path FROM sintomas WHERE sintoma = %s", 
                                 (sintoma,))
                    resultado = cursor.fetchone()
                    if resultado and resultado[0]:
                        imagen_path = resultado[0]
                        try:
                            imagen = Image.open(imagen_path)
                            # Redimensionar manteniendo proporción
                            ancho_max = 350
                            alto_max = 350
                            proporcion = min(ancho_max/float(imagen.size[0]), 
                                          alto_max/float(imagen.size[1]))
                            nuevo_ancho = int(float(imagen.size[0]) * float(proporcion))
                            nuevo_alto = int(float(imagen.size[1]) * float(proporcion))
                            imagen = imagen.resize((nuevo_ancho, nuevo_alto), 
                                                Image.Resampling.LANCZOS)
                            foto = ImageTk.PhotoImage(imagen)
                            imagen_label.config(image=foto)
                            imagen_label.image = foto
                        except Exception as e:
                            messagebox.showerror("Error", 
                                               f"No se pudo cargar la imagen: {str(e)}")
                    cursor.close()
                finally:
                    conexion.close()



    def on_sintoma_seleccionado(*args):
        """Manejador de evento cuando se selecciona un síntoma del combobox"""
        sintoma = combo_sintomas.get()
        if sintoma:
            # Verificar si el síntoma ya está en la tabla
            items = tabla.get_children()
            if not any(tabla.item(item)['values'][0] == sintoma for item in items):
                tabla.insert("", "end", values=(sintoma,))
                mostrar_imagen(sintoma)
                #combo_sintomas.set('')  # Limpiar selección

    def on_tabla_seleccionado(event):
        """Manejador de evento cuando se selecciona un ítem en la tabla"""
        seleccion = tabla.selection()
        if seleccion:
            item = tabla.item(seleccion[0])
            sintoma = item['values'][0]
            mostrar_imagen(sintoma)

    def eliminar_sintoma():
        seleccion = tabla.selection()
        if seleccion:
            tabla.delete(seleccion)
        else:
            messagebox.showwarning("Advertencia", 
                                 "Por favor, seleccione un síntoma para eliminar", 
                                 parent=ventana_sintomas)

    # Botones
    estilo_boton = {"font": ("Georgia", 18, "bold"), "width": 12}
    
    btn_eliminar = tk.Button(ventana_sintomas, 
                            text="Eliminar", 
                            command=eliminar_sintoma,
                            bg="#6A70FE",
                            **estilo_boton)
    btn_eliminar.place(x=800, y=450)

    btn_volver = tk.Button(ventana_sintomas, 
                          text="Volver", 
                          command=lambda: volver_a_anterior(ventana_sintomas, 
                                                          ventana_anterior),
                          bg="lightcoral",
                          **estilo_boton)
    btn_volver.place(x=800, y=590)

    # Vincular eventos
    combo_sintomas.bind('<<ComboboxSelected>>', on_sintoma_seleccionado)
    tabla.bind('<<TreeviewSelect>>', on_tabla_seleccionado)  # Nuevo evento para la tabla

    # Cargar síntomas iniciales
    if sintomas:
        combo_sintomas['values'] = sintomas
    else:
        messagebox.showwarning("Advertencia", "No se pudieron cargar los síntomas")


def volver_a_anterior(ventana_actual, ventana_anterior):
    ventana_actual.destroy()
    ventana_anterior.deiconify()