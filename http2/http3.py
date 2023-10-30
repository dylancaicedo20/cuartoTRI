import requests
import json

url="https://httpbin.org/post"
argumentos={
    "nombre":"Juan",
    "documento":"12345" 
}
response=requests.post(url,json=argumentos)
#print(response.content.decode())
decodetest=response.content.decode()
print(type(decodetest))
print(response.json())
print('*'*20)
decodetestjson=json.loads(response.content)
print(decodetestjson)
print('*'*20)
print(decodetest)

# print(response.content.decode())
# print(type(response.content.decode()))
# jsonresponse=json.loads(response.content)
# print(type(jsonresponse))