import tkinter as tk
from PIL import ImageTk, Image
import pyodbc
import subprocess

class Pelicula:
    def __init__(self, titulo, caratula, ubicacion):
        self.titulo = titulo
        self.caratula = caratula
        self.ubicacion = ubicacion

class ReproductorPeliculas:
    def __init__(self):
        self.peliculas = []
        self.ventana = tk.Tk()
        self.ventana.title("Reproductor de Películas")
        self.canvas = tk.Canvas(self.ventana, width=500, height=500)
        self.canvas.pack()

        # Establecer la conexión con la base de datos
        conexion_str = 'Driver={SQL Server};Server=DESKTOP-49JK190;Database=PeliculasDB;Trusted_Connection=yes;'
        self.conexion = pyodbc.connect(conexion_str)

        # Cargar las películas de la base de datos
        self.cargar_peliculas()

    def cargar_peliculas(self):
        cursor = self.conexion.cursor()

        # Obtener las películas de la tabla Peliculas
        cursor.execute("SELECT Titulo, Caratula, Ubicacion FROM Peliculas")
        rows = cursor.fetchall()

        for row in rows:
            titulo = row.Titulo
            caratula = row.Caratula
            ubicacion = row.Ubicacion

            pelicula = Pelicula(titulo, caratula, ubicacion)
            self.peliculas.append(pelicula)
            self.mostrar_pelicula(pelicula)

    def mostrar_pelicula(self, pelicula):
        # Cargar la imagen de la carátula
        imagen = Image.open(pelicula.caratula)
        imagen = imagen.resize((300, 400), Image.ANTIALIAS)
        imagen_tk = ImageTk.PhotoImage(imagen)

        # Mostrar la imagen en el lienzo
        self.canvas.create_image(250, 250, image=imagen_tk)
        self.canvas.image = imagen_tk

        # Agregar un evento de clic a la imagen
        self.canvas.bind("<Button-1>", lambda event: self.reproducir_pelicula(pelicula))

    def reproducir_pelicula(self, pelicula):
        # Reproducir la película utilizando el reproductor predeterminado del sistema
        subprocess.call([pelicula.ubicacion])

    def iniciar_reproductor(self):
        self.ventana.mainloop()

# Crear una instancia del reproductor de películas
reproductor = ReproductorPeliculas()

# Iniciar el reproductor
reproductor.iniciar_reproductor()
