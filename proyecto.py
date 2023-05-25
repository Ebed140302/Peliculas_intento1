import tkinter as tk
import pyodbc

def cargar_pelicula():
    # Obtener los valores ingresados por el usuario
    titulo = entry_titulo.get()
    director = entry_director.get()
    genero = entry_genero.get()
    duracion = entry_duracion.get()
    caratula = entry_caratula.get()
    ubicacion = entry_ubicacion.get()

    # Establecer la conexión con el servidor SQL Server
    server = 'DESKTOP-49JK190'
    database = 'PeliculasDB'
    conexion_str = f'Driver={{SQL Server}};Server={server};Database={database};Trusted_Connection=yes;'
    conexion = pyodbc.connect(conexion_str)

    # Crear un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Insertar la película en la tabla Peliculas
    cursor.execute("INSERT INTO Peliculas (Titulo, Director, Genero, Duracion, Caratula, Ubicacion) VALUES (?, ?, ?, ?, ?, ?)",
                   titulo, director, genero, duracion, caratula, ubicacion)

    # Confirmar los cambios en la base de datos
    conexion.commit()

    print("Película cargada exitosamente.")

# Crear la ventana principal
window = tk.Tk()
window.title("Cargar Película")

# Crear los campos de entrada de texto
label_titulo = tk.Label(window, text="Título:")
entry_titulo = tk.Entry(window)
label_director = tk.Label(window, text="Director:")
entry_director = tk.Entry(window)
label_genero = tk.Label(window, text="Género:")
entry_genero = tk.Entry(window)
label_duracion = tk.Label(window, text="Duración:")
entry_duracion = tk.Entry(window)
label_caratula = tk.Label(window, text="Carátula:")
entry_caratula = tk.Entry(window)
label_ubicacion = tk.Label(window, text="Ubicación del video:")
entry_ubicacion = tk.Entry(window)

# Crear el botón de carga
button_cargar = tk.Button(window, text="Cargar Película", command=cargar_pelicula)

# Ubicar los elementos en la ventana
label_titulo.pack()
entry_titulo.pack()
label_director.pack()
entry_director.pack()
label_genero.pack()
entry_genero.pack()
label_duracion.pack()
entry_duracion.pack()
label_caratula.pack()
entry_caratula.pack()
label_ubicacion.pack()
entry_ubicacion.pack()
button_cargar.pack()

# Iniciar el bucle de eventos de la ventana
window.mainloop()
