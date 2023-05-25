import requests
from bs4 import BeautifulSoup
import tkinter as tk

def buscar_informacion_pelicula():
    titulo = entry_titulo.get()
    
    # Formatear el título para incluir en la URL de búsqueda
    titulo_formateado = titulo.replace(" ", "+")

    # URL de búsqueda en IMDb
    url_busqueda = f"https://www.imdb.com/find?q={titulo_formateado}&s=tt"

    # Realizar la solicitud HTTP GET a la página de búsqueda
    response = requests.get(url_busqueda)

    # Crear el objeto BeautifulSoup a partir del contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrar el primer resultado de búsqueda
    resultado = soup.find("td", class_="result_text")

    if resultado:
        # Obtener el enlace de la página de la película
        enlace = resultado.find("a")["href"]
        url_pelicula = f"https://www.imdb.com{enlace}"

        # Realizar la solicitud HTTP GET a la página de la película
        response_pelicula = requests.get(url_pelicula)

        # Crear otro objeto BeautifulSoup para la página de la película
        soup_pelicula = BeautifulSoup(response_pelicula.text, 'html.parser')

        # Encontrar los elementos de información de la película
        titulo = soup_pelicula.find("h1").text.strip()
        director = soup_pelicula.find("div", class_="credit_summary_item").find("a").text.strip()
        genero = soup_pelicula.find("div", class_="subtext").find("a").text.strip()
        duracion = soup_pelicula.find("div", class_="subtext").find("time").text.strip()

        # Actualizar la etiqueta de resultado con la información de la película
        label_resultado.config(text=f"Título: {titulo}\nDirector: {director}\nGénero: {genero}\nDuración: {duracion}")
    else:
        # Actualizar la etiqueta de resultado con un mensaje de error
        label_resultado.config(text="No se encontró información para esa película.")

# Crear la ventana principal
window = tk.Tk()
window.title("Búsqueda de Películas")

# Crear los elementos de la interfaz
label_titulo = tk.Label(window, text="Título de la película:")
label_titulo.pack()

entry_titulo = tk.Entry(window)
entry_titulo.pack()

button_buscar = tk.Button(window, text="Buscar", command=buscar_informacion_pelicula)
button_buscar.pack()

label_resultado = tk.Label(window, text="")
label_resultado.pack()

# Ejecutar el bucle principal de la ventana
window.mainloop()
