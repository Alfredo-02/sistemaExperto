import tkinter as tk
from tkinter import messagebox
import mysql.connector  
from tkinter import ttk  
from PIL import Image, ImageTk 
import tkinter.font as tkFont
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password="", 
            database=""  
        )
        return conexion
    except mysql.connector.Error as e:
        messagebox.showerror("Error de conexión", str(e))
        return None

def obtener_enfermedades():
    conexion = conectar_db()
    if conexion is None:
        return []

    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT nombre_objeto FROM enfermedades")
            enfermedades = [fila[0] for fila in cursor.fetchall()]
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron cargar las enfermedades: {str(e)}")
        enfermedades = []
    finally:
        conexion.close()
    
    return enfermedades

def obtener_imagen_por_enfermedad(enfermedad):
    conexion = conectar_db()
    if conexion is None:
        return None

    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT imagen_path FROM enfermedades WHERE nombre_objeto = %s", (enfermedad,))
            resultado = cursor.fetchone()
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudo obtener la imagen: {str(e)}")
        resultado = None
    finally:
        conexion.close()

    return resultado[0] if resultado else None

def obtener_sintomas():
    conexion = conectar_db()
    if conexion is None:
        return []

    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT sintoma FROM sintomas")
            sintomas = [fila[0] for fila in cursor.fetchall()]
    except mysql.connector.Error as e:
        messagebox.showerror("Error", f"No se pudieron cargar los síntomas: {str(e)}")
        sintomas = []
    finally:
        conexion.close()
    
    return sintomas

def abrir_cuadro_relacion(ventana_menu_expe):
    ventana_cuadro_relacion = tk.Toplevel()
    ventana_cuadro_relacion.title("Cuadro-Relación")
    ventana_cuadro_relacion.attributes("-fullscreen", True)
    
    ventana_cuadro_relacion.configure(bg="#00BFBF")
    label = tk.Label(ventana_cuadro_relacion, text="CUADRO-RELACIÓN", font=("Trebuchet MS", 50, "bold"), bg="#00BFBF")
    label.pack(pady=50)

    label_enfermedad = tk.Label(ventana_cuadro_relacion, text="Selecciona una enfermedad:", font=("Trebuchet MS", 20), bg="#00BFBF")
    label_enfermedad.place(x=250, y=150)

    enfermedades = obtener_enfermedades()
    
    fuente = tkFont.Font(family="Helvetica", size=15) 

    style = ttk.Style()
    style.configure("TCombobox", font=fuente)  

    combo_enfermedad = ttk.Combobox(ventana_cuadro_relacion, values=enfermedades, state="readonly", width=30)  
    combo_enfermedad.place(x=250, y=200)

    combo_enfermedad['font'] = fuente

    imagen_label = tk.Label(ventana_cuadro_relacion, bg="#00BFBF")
    imagen_label.place(x=950, y=150)

    label_sintoma = tk.Label(ventana_cuadro_relacion, text="Selecciona un síntoma:", font=("Trebuchet MS", 20), bg="#00BFBF")
    label_sintoma.place(x=250, y=235)

    sintomas = obtener_sintomas()
    
    combo_sintoma = ttk.Combobox(ventana_cuadro_relacion, values=sintomas, state="readonly", width=30)
    combo_sintoma.place(x=250, y=285)

    combo_sintoma['font'] = fuente

    label_peso = tk.Label(ventana_cuadro_relacion, text="Selecciona peso:", font=("Trebuchet MS", 20), bg="#00BFBF")
    label_peso.place(x=250, y=315)

    frame_peso = tk.Frame(ventana_cuadro_relacion, width=200, height=100)
    frame_peso.place(x=250, y=360)

    entry_peso = tk.Entry(frame_peso, width=10, font=fuente)
    entry_peso.pack(side="left")

    label_porcentaje = tk.Label(frame_peso, text="%")
    label_porcentaje.pack(side="left")

    style = ttk.Style()
    fuente_tabla = tkFont.Font(family="Helvetica", size=15)  
    fuente_encabezados = tkFont.Font(family="Helvetica", size=15, weight="bold") 

    style.configure("Treeview", font=fuente_tabla) 
    style.configure("Treeview.Heading", font=fuente_encabezados, background="lightblue", foreground="black") 

    tabla = ttk.Treeview(ventana_cuadro_relacion, columns=("Síntoma", "Peso"), show="headings")
    tabla.heading("Síntoma", text="Síntoma")
    tabla.heading("Peso", text="Peso")

    tabla.column("Síntoma", width=500)  
    tabla.column("Peso", width=100, anchor="center") 

    tabla.place(x=250, y=400, width=600, height=200)



    btn_volver = tk.Button(ventana_cuadro_relacion, text="Volver", font=("Georgia", 24, "bold"), bg="lightcoral", width=15,
                            command=lambda: volver_a_menu_experto(ventana_cuadro_relacion, ventana_menu_expe))
    btn_volver.place(x=1100, y=700)

    
    def añadir_caracteristica():
        sintoma = combo_sintoma.get()
        peso = entry_peso.get()
        
        if sintoma and peso:
            for item in tabla.get_children():
                if tabla.item(item)['values'][0] == sintoma:
                    tabla.item(item, values=(sintoma, f"{peso}%"))
                    break
            else:
                tabla.insert("", "end", values=(sintoma, f"{peso}%"))
            
       
            combo_sintoma.set('') 
            entry_peso.delete(0, tk.END) 
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.", parent=ventana_cuadro_relacion)

    style = ttk.Style()
    style.configure('CustomButton.TButton', 
        font=('Arial', 12),
        background='white',
        foreground='black',
        padding=5
    )
    style.map('CustomButton.TButton',
        background=[('active', '#e6e6e6')],
        relief=[('pressed', 'sunken'), ('!pressed', 'raised')]
    )

    boton1 = ttk.Button(ventana_cuadro_relacion, text="Añadir", command=añadir_caracteristica, style='CustomButton.TButton')
    boton1.place(x=250, y=620, width=100, height=30)

    def cancelar_cambios():
        respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres cancelar los cambios?", parent=ventana_cuadro_relacion)
        if respuesta:
            for i in tabla.get_children():
                tabla.delete(i)
            buscar_sintomas()
            messagebox.showinfo("Información", "Cambios cancelados. Se han restaurado los datos originales.", parent=ventana_cuadro_relacion)

    def borrar_relaciones():
        enfermedad = combo_enfermedad.get()
        seleccion = tabla.selection()
        
        if not enfermedad:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una enfermedad.", parent=ventana_cuadro_relacion)
            return
        
        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, selecciona un síntoma para borrar.", parent=ventana_cuadro_relacion)
            return

        item = tabla.item(seleccion[0])
        sintoma = item['values'][0]

        respuesta = messagebox.askyesno("Confirmar", f"¿Estás seguro de que quieres borrar la relación para el síntoma '{sintoma}'?", parent=ventana_cuadro_relacion)
        if respuesta:
            conexion = conectar_db()
            if conexion:
                try:
                    with conexion.cursor() as cursor:
                        cursor.execute("SELECT id_enfermedad FROM enfermedades WHERE nombre_objeto = %s", (enfermedad,))
                        id_enfermedad = cursor.fetchone()
                        
                        cursor.execute("SELECT id_sintoma FROM sintomas WHERE sintoma = %s", (sintoma,))
                        id_sintoma = cursor.fetchone()
                        
                        if id_enfermedad and id_sintoma:
                            id_enfermedad = id_enfermedad[0]
                            id_sintoma = id_sintoma[0]
                            cursor.execute("DELETE FROM cuadro_relacion WHERE id_enfermedad = %s AND id_sintoma = %s", (id_enfermedad, id_sintoma))
                            conexion.commit()
                            messagebox.showinfo("Éxito", f"Se ha borrado la relación para el síntoma '{sintoma}'.", parent=ventana_cuadro_relacion)
                            tabla.delete(seleccion[0])
                        else:
                            messagebox.showinfo("Información", "No se encontró la relación en la base de datos.", parent=ventana_cuadro_relacion)
                except mysql.connector.Error as e:
                    messagebox.showerror("Error", f"No se pudo borrar la relación: {str(e)}", parent=ventana_cuadro_relacion)
                finally:
                    conexion.close()
            
        
    def guardar_caracteristicas():
        conexion = conectar_db()
        if conexion:
            cursor = conexion.cursor()
            try:
                if not tabla.get_children():
                    messagebox.showwarning("Advertencia", "No hay datos para guardar.", parent=ventana_cuadro_relacion)
                    return
                
                enfermedad_seleccionada = combo_enfermedad.get()
                if not enfermedad_seleccionada:
                    messagebox.showwarning("Advertencia", "Debes seleccionar una enfermedad.", parent=ventana_cuadro_relacion)
                    return

                cursor.execute("SELECT id_enfermedad FROM enfermedades WHERE nombre_objeto = %s", (enfermedad_seleccionada,))
                id_enfermedad = cursor.fetchone()
                if id_enfermedad is None:
                    messagebox.showwarning("Advertencia", f"No se encontró la enfermedad: {enfermedad_seleccionada}", parent=ventana_cuadro_relacion)
                    return
                id_enfermedad = id_enfermedad[0]

                cursor.execute("DELETE FROM cuadro_relacion WHERE id_enfermedad = %s", (id_enfermedad,))

                for item in tabla.get_children():
                    sintoma, peso = tabla.item(item)['values']
                    peso = peso.rstrip('%')  

                    cursor.execute("SELECT id_sintoma FROM sintomas WHERE sintoma = %s", (sintoma,))
                    id_sintoma = cursor.fetchone()
                    if id_sintoma is None:
                        continue
                    id_sintoma = id_sintoma[0]

                    cursor.execute("""
                        INSERT INTO cuadro_relacion (id_enfermedad, id_sintoma, peso)
                        VALUES (%s, %s, %s)
                    """, (id_enfermedad, id_sintoma, peso))
                
                conexion.commit()
                messagebox.showinfo("Éxito", "Características guardadas correctamente.", parent=ventana_cuadro_relacion)

                combo_sintoma.set('')  
                entry_peso.delete(0, tk.END) 

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"No se pudo guardar: {str(e)}", parent=ventana_cuadro_relacion)
            finally:
                cursor.close()
                conexion.close()

    def buscar_sintomas():
        enfermedad = combo_enfermedad.get()
        if not enfermedad:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una enfermedad.", parent=ventana_cuadro_relacion)
            return

        for i in tabla.get_children():
            tabla.delete(i)
        
        conexion = conectar_db()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    cursor.execute("SELECT id_enfermedad FROM enfermedades WHERE nombre_objeto = %s", (enfermedad,))
                    id_enfermedad = cursor.fetchone()
                    
                    if id_enfermedad:
                        id_enfermedad = id_enfermedad[0]
                        cursor.execute("""
                            SELECT s.sintoma, cr.peso 
                            FROM cuadro_relacion cr
                            JOIN sintomas s ON cr.id_sintoma = s.id_sintoma
                            WHERE cr.id_enfermedad = %s
                        """, (id_enfermedad,))
                        resultados = cursor.fetchall()
                        for sintoma, peso in resultados:
                            tabla.insert("", "end", values=(sintoma, f"{peso}%"))
                        
                        if not resultados:
                            messagebox.showinfo("Información", "No hay síntomas registrados para esta enfermedad.",parent= ventana_cuadro_relacion)
                    else:
                        messagebox.showinfo("Información", "No se encontró la enfermedad en la base de datos.",parent= ventana_cuadro_relacion)
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"No se pudieron cargar los síntomas: {str(e)}", parent= ventana_cuadro_relacion)
            finally:
                conexion.close()
      
        

    boton_guardar = ttk.Button(ventana_cuadro_relacion, text="Guardar",command=guardar_caracteristicas, style='CustomButton.TButton')
    boton_guardar.place(x=360, y=620, width=100, height=30)

    boton_cancelar = ttk.Button(ventana_cuadro_relacion, text="Cancelar", command=cancelar_cambios, style='CustomButton.TButton')
    boton_cancelar.place(x=470, y=620, width=100, height=30)

    boton_borrar = ttk.Button(ventana_cuadro_relacion, text="Borrar", command=borrar_relaciones, style='CustomButton.TButton')
    boton_borrar.place(x=580, y=620, width=100, height=30)


    combo_enfermedad.bind("<<ComboboxSelected>>", lambda event: ejecutar_metodos(combo_enfermedad.get(), imagen_label))
    def ejecutar_metodos(enfermedad, label):
        mostrar_imagen(enfermedad, label)  
        buscar_sintomas()  
        
def mostrar_imagen(enfermedad, label):
    if enfermedad:
        imagen_path = obtener_imagen_por_enfermedad(enfermedad)
        if imagen_path:
            cargar_y_mostrar_imagen(label, imagen_path)
        else:
            messagebox.showwarning("Advertencia", "No se encontró imagen para esta enfermedad.")
    else:
        messagebox.showwarning("Advertencia", "Por favor selecciona una enfermedad.")

def cargar_y_mostrar_imagen(label, ruta):
    try:
        # Cargar la imagen usando PIL
        imagen_original = Image.open(ruta)
        
        # Redimensionar la imagen
        imagen_redimensionada = imagen_original.resize((350, 350), Image.LANCZOS)
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        
        label.config(image=imagen_tk)
        label.image = imagen_tk 
    except Exception as e:
        messagebox.showerror("Error al cargar imagen", str(e))

def volver_a_menu_experto(ventana_cuadro_relacion, ventana_menu_expe):
    ventana_cuadro_relacion.destroy()
    ventana_menu_expe.deiconify()
