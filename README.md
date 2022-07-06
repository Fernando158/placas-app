# placas-app
 Api para consultas de patentes
Welcome to the placas-app wiki!

# Instalación:

`git clone https://github.com/Fernando158/placas-app.git`

Ejemplo para Windows:

* Luego de descargar la app se deben situar en la carpeta placas-app desde la consola.

* Crear entorno virtual

`python -m virtualenv placas-app-env`

* Activar entorno virtual:

`./placas-app-env/Scripts/activate`

Una vez iniciado tu entorno vitual, descarga las librerias ejecutando el archivo requirements.txt

`pip install -r requirements.txt`

* Luego de instalar las librerias necesarias podemos encender el servidor:

`uvicorn main:app --reload`

 Una vez ejecutado el comando nos vamos al navegador y podemos empezar a probar.

# Ejemplos:

1. Endpoint donde se ingrese una patente y este retorne el ID asociado a la patente.

* http://127.0.0.1:8000/patente/{patente}

Consulta de ejemplo:
* http://127.0.0.1:8000/patente/AAAA000

2. Endpoint donde se ingrese el ID y este retorne la patente.

* http://127.0.0.1:8000/patente/{patente_id}

Consulta de ejemplo:
* http://127.0.0.1:8000/patente_id/1

