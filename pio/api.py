import requests
url="https://gutendex.com/books/"
response=requests.get(url)
dicc=response.json()
resultados=dicc["results"]
#print(resultados[0])
titulos = [libro["title"] for libro in resultados]
titulos_ord=sorted(titulos)
      #print(libro["title"], end="\n")
    
for titulo in titulos_ord:
    print(titulo)
