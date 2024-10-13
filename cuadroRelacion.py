import tkinter as tk
from tkinter import messagebox
import mysql.connector  # type: ignore
from tkinter import ttk  # Importar ttk para usar el ComboBox
from PIL import Image, ImageTk  # Asegúrate de tener Pillow instalado# type: ignore
import tkinter.font as tkFont
def conectar_db():
    try:
        conexion = mysql.connector.connect(
            host="localhost",  # Cambia esto si es necesario
            user="root",  # Reemplaza con tu usuario
            password="123456",  # Reemplaza con tu contraseña
            database="SistemaExperto"  # Reemplaza con tu base de datos
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

    # Etiqueta para seleccionar enfermedad
    label_enfermedad = tk.Label(ventana_cuadro_relacion, text="Selecciona una enfermedad:", font=("Trebuchet MS", 20), bg="#00BFBF")
    label_enfermedad.place(x=250, y=150)

    # Obtener las enfermedades de la base de datos
    enfermedades = obtener_enfermedades()
    
    fuente = tkFont.Font(family="Helvetica", size=15)  # Cambia "Helvetica" y 12 por la fuente y tamaño que desees

    # Establecer el estilo del Combobox
    style = ttk.Style()
    style.configure("TCombobox", font=fuente)  # Aplicar la fuente al Combobox

    # Crear el Combobox con un ancho específico
    combo_enfermedad = ttk.Combobox(ventana_cuadro_relacion, values=enfermedades, state="readonly", width=30)  # Cambia 30 por el ancho que desees
    combo_enfermedad.place(x=250, y=200)

    # Aplicar la fuente personalizada al Combobox
    combo_enfermedad['font'] = fuente

    # Label para mostrar la imagen
    imagen_label = tk.Label(ventana_cuadro_relacion, bg="#00BFBF")
    imagen_label.place(x=950, y=150)

    # Etiqueta para seleccionar sintoma
    label_sintoma = tk.Label(ventana_cuadro_relacion, text="Selecciona un síntoma:", font=("Trebuchet MS", 20), bg="#00BFBF")
    label_sintoma.place(x=250, y=235)

    # sintomas de la base de datos
    sintomas = obtener_sintomas()
    
    # Crear un ComboBox para seleccionar el sintoma
    combo_sintoma = ttk.Combobox(ventana_cuadro_relacion, values=sintomas, state="readonly", width=30)
    combo_sintoma.place(x=250, y=285)

    combo_sintoma['font'] = fuente

    # Etiqueta para seleccionar peso
    label_peso = tk.Label(ventana_cuadro_relacion, text="Selecciona peso:", font=("Trebuchet MS", 20), bg="#00BFBF")
    label_peso.place(x=250, y=315)

    # Frame para organizar el campo de texto y el símbolo %
    frame_peso = tk.Frame(ventana_cuadro_relacion, width=200, height=100)
    frame_peso.place(x=250, y=360)

    # Campo de texto para ingresar el peso
    entry_peso = tk.Entry(frame_peso, width=10, font=fuente)
    entry_peso.pack(side="left")

    # Etiqueta de porcentaje %
    label_porcentaje = tk.Label(frame_peso, text="%")
    label_porcentaje.pack(side="left")

    # Crear un estilo para la tabla
    style = ttk.Style()
    fuente_tabla = tkFont.Font(family="Helvetica", size=15)  # Cambia "Helvetica" y 12 por la fuente y tamaño que desees
    fuente_encabezados = tkFont.Font(family="Helvetica", size=15, weight="bold")  # Fuente para encabezados en negrita

    style.configure("Treeview", font=fuente_tabla)  # Cambia el estilo de los datos
    style.configure("Treeview.Heading", font=fuente_encabezados, background="lightblue", foreground="black")  # Estilo de encabezados

    # Tabla para mostrar características seleccionadas
    tabla = ttk.Treeview(ventana_cuadro_relacion, columns=("Síntoma", "Peso"), show="headings")
    tabla.heading("Síntoma", text="Síntoma")
    tabla.heading("Peso", text="Peso")

    # Ajustar el ancho de las columnas
    tabla.column("Síntoma", width=500)  # Ajustar ancho y centrar
    tabla.column("Peso", width=100, anchor="center")  # Ajustar ancho y centrar

    tabla.place(x=250, y=400, width=600, height=200)



    btn_volver = tk.Button(ventana_cuadro_relacion, text="Volver", font=("Georgia", 24, "bold"), bg="lightcoral", width=15,
                            command=lambda: volver_a_menu_experto(ventana_cuadro_relacion, ventana_menu_expe))
    btn_volver.place(x=1100, y=700)

    
    def añadir_caracteristica():
        sintoma = combo_sintoma.get()
        peso = entry_peso.get()
        
        if sintoma and peso:
            # Verificar si el síntoma ya existe en la tabla
            for item in tabla.get_children():
                if tabla.item(item)['values'][0] == sintoma:
                    tabla.item(item, values=(sintoma, f"{peso}%"))
                    break
            else:
                tabla.insert("", "end", values=(sintoma, f"{peso}%"))
            
            # Limpiar los campos después de añadir
            combo_sintoma.set('')  # Limpiar el Combobox del síntoma
            entry_peso.delete(0, tk.END)  # Limpiar el campo de texto del peso
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.", parent=ventana_cuadro_relacion)

    # Configuración del estilo para los botones
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

    # Creación de los botones
    boton1 = ttk.Button(ventana_cuadro_relacion, text="Añadir", command=añadir_caracteristica, style='CustomButton.TButton')
    boton1.place(x=250, y=620, width=100, height=30)

    def cancelar_cambios():
        respuesta = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres cancelar los cambios?", parent=ventana_cuadro_relacion)
        if respuesta:
            # Limpiar la tabla
            for i in tabla.get_children():
                tabla.delete(i)
            # Volver a cargar los datos originales de la base de datos
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
                        # Obtener el id_enfermedad y id_sintoma
                        cursor.execute("SELECT id_enfermedad FROM enfermedades WHERE nombre_objeto = %s", (enfermedad,))
                        id_enfermedad = cursor.fetchone()
                        
                        cursor.execute("SELECT id_sintoma FROM sintomas WHERE sintoma = %s", (sintoma,))
                        id_sintoma = cursor.fetchone()
                        
                        if id_enfermedad and id_sintoma:
                            id_enfermedad = id_enfermedad[0]
                            id_sintoma = id_sintoma[0]
                            # Borrar la relación específica
                            cursor.execute("DELETE FROM cuadro_relacion WHERE id_enfermedad = %s AND id_sintoma = %s", (id_enfermedad, id_sintoma))
                            conexion.commit()
                            messagebox.showinfo("Éxito", f"Se ha borrado la relación para el síntoma '{sintoma}'.", parent=ventana_cuadro_relacion)
                            # Eliminar el item de la tabla
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

                # Eliminar relaciones existentes para esta enfermedad
                cursor.execute("DELETE FROM cuadro_relacion WHERE id_enfermedad = %s", (id_enfermedad,))

                for item in tabla.get_children():
                    sintoma, peso = tabla.item(item)['values']
                    peso = peso.rstrip('%')  # Eliminar el símbolo '%' del peso

                    cursor.execute("SELECT id_sintoma FROM sintomas WHERE sintoma = %s", (sintoma,))
                    id_sintoma = cursor.fetchone()
                    if id_sintoma is None:
                        continue
                    id_sintoma = id_sintoma[0]

                    # Insertar nueva relación
                    cursor.execute("""
                        INSERT INTO cuadro_relacion (id_enfermedad, id_sintoma, peso)
                        VALUES (%s, %s, %s)
                    """, (id_enfermedad, id_sintoma, peso))
                
                conexion.commit()
                messagebox.showinfo("Éxito", "Características guardadas correctamente.", parent=ventana_cuadro_relacion)

                    # Limpiar los campos de selección de síntoma y peso
                combo_sintoma.set('')  # Limpiar el Combobox del síntoma
                entry_peso.delete(0, tk.END)  # Limpiar el campo de texto del peso

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

        # Limpiar la tabla
        for i in tabla.get_children():
            tabla.delete(i)
        
        # Obtener síntomas de la enfermedad seleccionada
        conexion = conectar_db()
        if conexion:
            try:
                with conexion.cursor() as cursor:
                    # Primero, obtener el id_enfermedad
                    cursor.execute("SELECT id_enfermedad FROM enfermedades WHERE nombre_objeto = %s", (enfermedad,))
                    id_enfermedad = cursor.fetchone()
                    
                    if id_enfermedad:
                        id_enfermedad = id_enfermedad[0]
                        # Luego, usar el id_enfermedad para obtener los síntomas y pesos
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
      
        

    #Bton Guardar
    boton_guardar = ttk.Button(ventana_cuadro_relacion, text="Guardar",command=guardar_caracteristicas, style='CustomButton.TButton')
    boton_guardar.place(x=450, y=620, width=100, height=30)

    boton_cancelar = ttk.Button(ventana_cuadro_relacion, text="Cancelar", command=cancelar_cambios, style='CustomButton.TButton')
    boton_cancelar.place(x=560, y=620, width=100, height=30)

    boton_borrar = ttk.Button(ventana_cuadro_relacion, text="Borrar", command=borrar_relaciones, style='CustomButton.TButton')
    boton_borrar.place(x=670, y=620, width=100, height=30)

    #combo_enfermedad.bind("<<ComboboxSelected>>", lambda event: mostrar_imagen(combo_enfermedad.get(), imagen_label))

    combo_enfermedad.bind("<<ComboboxSelected>>", lambda event: ejecutar_metodos(combo_enfermedad.get(), imagen_label))
    def ejecutar_metodos(enfermedad, label):
        mostrar_imagen(enfermedad, label)  # Llama al método para mostrar la imagen
        buscar_sintomas()  # Llama al método para buscar los síntomas
        
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
        label.image = imagen_tk  # Mantener una referencia
    except Exception as e:
        messagebox.showerror("Error al cargar imagen", str(e))

def volver_a_menu_experto(ventana_cuadro_relacion, ventana_menu_expe):
    ventana_cuadro_relacion.destroy()
    ventana_menu_expe.deiconify()
