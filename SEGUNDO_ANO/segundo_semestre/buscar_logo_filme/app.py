import requests, json, sys
import urllib.request as url_request
from gerar_tela import Tela

key = "f09cfbdf"
def buscarFilme(nome_filme):
    request = requests.get(f"http://www.omdbapi.com/?apikey={key}&t={nome_filme}")

    data = json.loads(request.content)

    try:
        url_request.urlretrieve(data['Poster'], "Poster_Filme.jpg")
        print("Imagem Salva")
        
        # tela = Tela()
        # tela.adicionar_img()
        # tela.rodar()
    except:
        erro = sys.exc_info()
        print(erro)
    print(data)
    
# name = input("Nome do filme?")
# buscarFilme(name)