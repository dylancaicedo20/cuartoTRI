import requests
import json

url = "https://httpbin.org/get"
response = requests.get(url)

def imprimir_claves(diccionario, prefijo=""):
    for key, value in diccionario.items():
        if isinstance(value, dict):
            imprimir_claves(value, f"{prefijo}.{key}" if prefijo else key)
        else:
            print(f"{prefijo}.{key}" if prefijo else key)

try:
    jsonresponse = response.json()
    print(type(jsonresponse))
    
    imprimir_claves(jsonresponse)
except ValueError:
    print("La respuesta no es un objeto JSON válido.")
