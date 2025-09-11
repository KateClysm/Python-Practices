from functions.functions import hola_mundo
from fastapi import FastAPI
#Importa la clase FastAPI del framework FastAPI, que se usa para crear aplicaciones web o APIs en Python.
# FastAPI permite definir rutas (@app.get, @app.post, etc.) y manejar peticiones HTTP.
from models.tablas import insert_datos, select, create_table


create_table()

app = FastAPI()
# Crea una instancia de la aplicación FastAPI llamada app.
# Esta instancia será usada para definir todas las rutas y manejar peticiones.

#@app.get("/"): define una ruta HTTP GET en la raíz de la API (http://localhost:8000/).
@app.get("/")
async def inicio():
    resultado = hola_mundo("Aye", 21)
    return resultado


#{nombre} y {edad} son parámetros dinámicos de la URL.
@app.get("/insert/{nombre}/{edad}")
async def insertar(nombre:str, edad:int):   #FastAPI automáticamente convierte edad a int y nombre a str.
    try:
        insert_datos(nombre,edad)
        return "Datos insertados correctamente"
    except Exception as e:
        print("Ups:", e)
    

# Llama a la función select() que obtiene todos los registros de la tabla usuarios.
# Devuelve la lista de resultados al cliente en formato JSON.
@app.get("/seleccionar")
async def seleccionar():
    resultado = select()
    return resultado