import tkinter as tk
from tkinter import messagebox
import pyodbc

class ModificarCaratulaGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Modificar Carátula")

        # Etiqueta y entrada para el título de la película
        self.lbl_titulo = tk.Label(self.ventana, text="Título:")
        self.lbl_titulo.pack()
        self.entry_titulo = tk.Entry(self.ventana)
        self.entry_titulo.pack()

        # Etiqueta y entrada para la nueva ruta de la carátula
        self.lbl_ruta_caratula = tk.Label(self.ventana, text="Nueva Ruta de Carátula:")
        self.lbl_ruta_caratula.pack()
        self.entry_ruta_caratula = tk.Entry(self.ventana)
        self.entry_ruta_caratula.pack()

        # Botón para modificar la ruta de la carátula
        self.btn_modificar = tk.Button(self.ventana, text="Modificar", command=self.modificar_caratula)
        self.btn_modificar.pack()

        # Establecer la conexión con la base de datos
        conexion_str = 'Driver={SQL Server};Server=DESKTOP-49JK190;Database=PeliculasDB;Trusted_Connection=yes;'
        self.conexion = pyodbc.connect(conexion_str)

    def modificar_caratula(self):
        # Obtener el título de la película y la nueva ruta de la carátula
        titulo_pelicula = self.entry_titulo.get()
        nueva_ruta_caratula = self.entry_ruta_caratula.get()

        if titulo_pelicula and nueva_ruta_caratula:
            try:
                # Crear un cursor para ejecutar la consulta SQL
                cursor = self.conexion.cursor()

                # Modificar la ruta de la carátula en la base de datos mediante una consulta SQL
                consulta = f"UPDATE Peliculas SET Caratula = '{nueva_ruta_caratula}' WHERE Titulo = '{titulo_pelicula}'"
                cursor.execute(consulta)

                # Confirmar los cambios en la base de datos
                self.conexion.commit()

                # Mostrar un mensaje de éxito
                mensaje = f"La carátula de la película '{titulo_pelicula}' ha sido modificada exitosamente."
                messagebox.showinfo("Modificación Exitosa", mensaje)
            except pyodbc.Error as error:
                # Mostrar un mensaje de error en caso de ocurrir un error en la base de datos
                messagebox.showerror("Error en la Base de Datos", str(error))
        else:
            # Mostrar un mensaje de error si no se proporcionaron los datos necesarios
            messagebox.showerror("Datos Faltantes", "Por favor, ingrese el título de la película y la nueva ruta de la carátula.")

    def iniciar_interfaz(self):
        self.ventana.mainloop()

# Crear una instancia de la interfaz de modificación de carátula
interfaz = ModificarCaratulaGUI()

# Iniciar la interfaz
interfaz.iniciar_interfaz()
