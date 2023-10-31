import requests
import json
url="https://httpbin.org/delete"#?nombre=juan&documento=12345"
argumentos={
    'nombre':'Perico',
    'documento':'12345'
}
theheaders={
    'Content-Type':'Text',
    'access-token':'12345'
}
response=requests.delete(url,data=json.dumps(argumentos),headers=theheaders)
decodetest=response.content.decode()
print('*'*20)
print(decodetest)
print('-'*20)
headersprint=response.headers
print(headersprint)