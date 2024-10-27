import requests, json, sys
import urllib.request as url_request

key = "f09cfbdf"
def buscarFilme(nome_filme):
    request = requests.get(f"http://www.omdbapi.com/?apikey={key}&t={nome_filme}")

    data = json.loads(request.content)

    try:
        url_request.urlretrieve(data['Poster'], "Poster_Filme.jpg")
        print("Imagem Salva")
    except:
        erro = sys.exc_info()
        print(erro)
    print(data)
    
buscarFilme("Deadpool")