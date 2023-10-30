import requests
url="https://img.freepik.com/vector-gratis/ilustracion-icono-vector-dibujos-animados-lindo-gato-sentado-concepto-icono-naturaleza-animal-aislado-premium-vector-estilo-dibujos-animados-plana_138676-4148.jpg?size=626&ext=jpg"
response=requests.get(url,stream=True)

with open("http2/gato.jpg","wb") as file:
    for i in response.iter_content():
        file.write(i)