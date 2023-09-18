import json
import requests
from banco_livros import Livros

def buscarDados(livros:list, capitulos:list):
    request = requests.get("https://www.abibliadigital.com.br/api/books")
    j = json.loads(request.content)

    for i in range(66):
        livros.append(j[i]['name'])
        capitulos.append(j[i]['chapters'])

    return livros, capitulos


       



