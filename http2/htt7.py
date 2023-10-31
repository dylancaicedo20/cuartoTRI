import requests
url="https://api.github.com/users"
sesion=requests.session()
sesion.auth=("dylan.caicedo2007@hotmail.com","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")
response=sesion.get(url)

if response.status_code==200:
    response1=sesion.get("https://github.com/dylancaicedo20")
    print(response1.cookies)