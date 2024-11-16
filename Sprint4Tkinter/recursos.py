import tkinter as tk

import requests
from PIL import Image, ImageTk
from io import BytesIO

from requests import RequestException


#descripción y parametros
def descargar_imagen(url,size):
    try:
        #Solicitud GET a la URL
        respuesta = requests.get(url)
        respuesta.raise_for_status() #excepción si la solicitud no fue exitosa
    #Abrir imagen desde el flujo de bytes
        imagen = Image.open(BytesIO(respuesta.content))
    #Ajusta al tamaño especificado usando el filtro LANCZOS para una redimensionada de alta calidad
        imagen=imagen.resize(size,Image.LANCZOS)
    #La imagen se convierte en un formato compatible con Tkinter
        imagen_tk = ImageTk.PhotoImage(imagen)
    #Devolvemos la imagen
        return imagen_tk
    #Manejo de excepciones , si hay algun error en la descarga, se captura la excepción
    #se muestran con un mensaje de error indicando la URL y se devuelve NONE,
    #Indicando que la imgen no se pudo ser descargada.
    except RequestException as e:
        print(f"Error al descargar la immagen: {url}: {e}")
        return None



