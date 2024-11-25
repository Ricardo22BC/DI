# import tkinter as tk
#
# import requests
# from PIL import Image, ImageTk
# from io import BytesIO
#
# from requests import RequestException
#
#
# #descripción y parametros
# def descargar_imagen(url,size):
#     try:
#         #Validación del tamaño
#         if not isinstance(size, tuple):
#             raise ValueError
#
#         #Solicitud GET a la URL
#         respuesta = requests.get(url)
#         respuesta.raise_for_status() #excepción si la solicitud no fue exitosa
#         # Verifica si la respuesta contiene una imagen válida
#         if 'image' not in respuesta.headers['Content-Type']:
#             raise ValueError(f"La URL no contiene una imagen válida: {url}")
#     #Abrir imagen desde el flujo de bytes
#         imagen = Image.open(BytesIO(respuesta.content))
#
#         if imagen.mode == "RGBA":
#             imagen = imagen.convert("RGB")
#     #Ajusta al tamaño especificado usando el filtro LANCZOS para una redimensionada de alta calidad
#         imagen=imagen.resize(size,Image.LANCZOS)
#     #La imagen se convierte en un formato compatible con Tkinter
#         imagen_tk = ImageTk.PhotoImage(imagen)
#         print(f"Imagen descargada correctamente de {url}")
#     #Devolvemos la imagen
#         return imagen_tk
#     #Manejo de excepciones , si hay algun error en la descarga, se captura la excepción
#     #se muestran con un mensaje de error indicando la URL y se devuelve NONE,
#     #Indicando que la imgen no se pudo ser descargada.
#     except RequestException as e:
#         print(f"Error al descargar la immagen: {url}: {e}")
#     except ValueError as e:
#         print(f"Error en el procesamiento de la imagen: {e}")
#     except Exception as e:
#         print(f"Ha ocurrido un error inesperado: {e}")
#     return None
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Lista de URLs de imágenes
image_urls = [
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/0.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/1.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/2.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/3.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/4.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/5.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/6.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/7.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/8.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/9.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/10.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/11.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/12.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/13.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/14.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/15.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/16.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/17.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/18.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/19.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/20.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/21.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/22.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/23.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/24.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/25.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/26.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/27.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/28.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/29.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/30.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/31.png",
    "https://raw.githubusercontent.com/Ricardo22BC/DI/refs/heads/main/Sprint4Tkinter/images/32.png"
]


def descargar_imagenes(urls, size):
    imagenes = {}
    for index, url in enumerate(urls):
        try:
            print(f"Descargando imagen {index} desde: {url}")

            # Validación del tamaño
            if not isinstance(size, tuple):
                raise ValueError("El tamaño debe ser una tupla.")

            # Solicitud GET a la URL
            respuesta = requests.get(url)
            respuesta.raise_for_status()  # excepción si la solicitud no fue exitosa

            # Verifica si la respuesta contiene una imagen válida
            if 'image' not in respuesta.headers['Content-Type']:
                raise ValueError(f"La URL no contiene una imagen válida: {url}")

            # Abrir imagen desde el flujo de bytes
            imagen = Image.open(BytesIO(respuesta.content))

            if imagen.mode == "RGBA":
                imagen = imagen.convert("RGB")

            # Ajusta al tamaño especificado usando el filtro LANCZOS para una redimensionada de alta calidad
            imagen = imagen.resize(size, Image.LANCZOS)

            # La imagen se convierte en un formato compatible con Tkinter
            imagen_tk = ImageTk.PhotoImage(imagen)
            print(f"Imagen descargada correctamente de {url}")

            # Almacena la imagen descargada en el diccionario
            imagenes[index] = imagen_tk

        except Exception as e:
            print(f"Error al descargar la imagen {index} desde la URL: {url}. Error: {e}")

    return imagenes

# Ejemplo de prueba
tamaño = (100, 100)
imagenes = descargar_imagenes(image_urls, tamaño)
if imagenes:
    print("Todas las imágenes se descargaron y procesaron correctamente.")
else:
    print("Hubo un problema al descargar las imágenes.")



