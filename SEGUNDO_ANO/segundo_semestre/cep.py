import requests, json

def buscarCep(cep):
    request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    todo = json.loads(request.content)
    return todo
    
print(buscarCep(14403729))