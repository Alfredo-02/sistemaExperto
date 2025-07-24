# 🧠 Sistema Experto para el Diagnóstico de Enfermedades

Aplicación de escritorio desarrollada en Python con interfaz gráfica basada en Tkinter. Este sistema permite registrar, modificar, consultar y eliminar enfermedades y síntomas, junto con imágenes asociadas, facilitando el diagnóstico médico a través de una interfaz intuitiva para usuarios y expertos.

## 🎯 Características principales

### 👤 Modo Usuario
- Búsqueda de enfermedades por síntomas desde un combobox.
- Visualización de síntomas seleccionados en tabla.
- Visualización automática de imágenes asociadas a síntomas.
- Modo de inferencia (estructura preparada).

### 👨‍⚕️ Modo Experto (protegido por contraseña)
- Gestión de enfermedades: altas, bajas, consultas, cambios.
- Gestión de síntomas: agregar, modificar, eliminar.
- Carga y redimensionamiento de imágenes desde archivos locales.
- Navegación entre registros (inicio, final, adelante, atrás).
- Cuadro de relación entre enfermedades y síntomas.
- Consultas generales e individuales con visualización completa de datos e imágenes.

## 🛠️ Tecnologías utilizadas

- **Python 3.10+**
- **Tkinter** (interfaz gráfica)
- **MySQL** (persistencia de datos)
- **Pillow / ImageTk** (visualización de imágenes)
- **ttk / Treeview** (gestión visual de datos)
- **FullScreen UI** (para experiencia de usuario envolvente)

## 📁 Estructura del Proyecto

```
sistema_experto/
├── sistemaExperto.py             # Lógica principal del sistema
├── interfazUsuario.py            # Interfaz gráfica para el usuario
├── cuadroRelacion.py             # Relaciones enfermedad-síntoma
├── busquedaSintoma.py            # Búsqueda y selección por síntomas
├── imagenes/                     # Carpeta de imágenes del sistema
├── base_de_datos.sql             # Script opcional de creación de tablas
└── README.md
```

## 🗃️ Base de Datos

Tablas principales:
- `enfermedades`: id, nombre_objeto, descripción, imagen_path
- `sintomas`: id, sintoma, imagen_path
- `relacion_enfermedad_sintoma`: enfermedad_id, sintoma_id

La conexión se configura en el método `conectar_db()` del archivo `cuadroRelacion.py`.

## ▶️ Ejecución del sistema

1. Instalar dependencias necesarias:
```bash
pip install pillow mysql-connector-python
```

2. Ejecutar el sistema:
```bash
python sistemaExperto.py
```

3. Asegúrate de tener el servidor MySQL corriendo y la base de datos creada.

## 🧪 Módulos incluidos

- `interfaces()` – Entrada al sistema con opción experto/usuario.
- `abrir_busqueda_sintomas()` – Búsqueda visual por síntomas.
- `mostrar_menu_experto()` – Menú de administración completa.
- `guardar_objeto()` – Inserción de nuevas enfermedades o síntomas.
- `consulta_general()` y `consulta_individual()` – Vistas con tabla o ventana emergente.

## 📸 Interfaz Gráfica

La aplicación presenta una interfaz a pantalla completa con botones grandes y colores diferenciados por acción:

- Azul: Agregar
- Rojo: Eliminar
- Verde: Consultas
- Amarillo: Modificar
- Gris: Navegación
- Íconos visuales en el menú principal

## 🚧 Funcionalidades futuras

- Integración de un motor de inferencia real (reglas, pesos).
- Generación de reportes automáticos en PDF.
- Exportación de datos.
- Optimización y validación avanzada de entradas.

Desarrollado por: **Alfredo Valparaiso Pascual**  
Correo: alfredo.valparaiso09@gmail.com  
