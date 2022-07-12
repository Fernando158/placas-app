from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from typing import Union
import string

app = FastAPI()

#Invalida los mensajes predeterminados de Fastapi cuando ocurre un error
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    msg_error = 'La patente ingresada es incorrecta, verifique e intente nuevamente'
    return PlainTextResponse("{Error : %s}" % msg_error, status_code=400)

@app.get("/")
def read_root():
    return {"Bienvenido a la api para consultar patentes"}

def get_placas():
    """Función que busca todas las placas vehiculares y asigna un id a cada una.
    Parámetros:
        Ninguno.
    Devuelve:
        Un diccionario con todas las placas con su id unico.
    """
    letras = string.ascii_uppercase
    placas = {}
    patente_id = 0

    for letra in letras:
       for i in range(1000):
            patente_id += 1
            placas[letra * 4 + str(i).zfill(3)] = patente_id

    return placas

def get_id(patente_id):
    """Función que busca una patente por su id.
    Parámetros:
        patente_id : Es un número entero.
    Devuelve:
        patente : La patente del id solicitado.
    """

    # obtener todas las placas
    placas = get_placas()
    for patente, value in placas.items():
        if patente_id == value:
            return patente

@app.get("/patente/{patente}")
def get_patente(patente: str):
    """Función que busca una placa y devuelve el id.
    Parámetros:
        patente : Es una cadena de caracteres con un mismo patrón cuatro letras y tres números, ejemplo:AAAA000.
    Devuelve:
        - placa_id : Es el id de la patente solicitada.
        En caso de error:
            detail : mensaje de error.
    """

    # obtener todas las placas
    placas = get_placas()

    if patente not in placas:
        msg_error = "La patente ingresada es incorrecta, verifique e intente nuevamente"
        raise HTTPException(status_code=404, detail=msg_error)
    
    return {"patente_id": placas[patente]}


@app.get("/patente_id/{patente_id}")
def get_patente_id(patente_id: int):
    """Función que busca una placa y devuelve el id.
    
    Parámetros:
        patente_id : Es un número entero debe ser en el rango del 1 hasta el 26000.
    Devuelve:
        - patente : Es el patente de la placa solicitada.
        En caso de error:
            detail : mensaje de error.
    """
    
    if patente_id not in range(1,26001):
        msg_error = "La patente ingresada no existe, las patentes registradas estan en el rango del 1 al 26000"
        raise HTTPException(status_code=404, detail=msg_error)

    patente = get_id(patente_id)

    return {"patente": patente}