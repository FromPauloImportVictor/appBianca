import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify


#Função para fazer uma requisição
def getPageContent(url: str) -> bytes:
    """

    :param url: URL da página bianca.com
    :return: Conteúdo HTML
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site!:{e}")


#Função para manipular o HTML e retornar um JSON
def getDict(htmlcontent) -> dict or None:
    """

    :param htmlcontent: Conteúdo HTML
    :return: Conteúdo da HOME em formato de Dicionário ou None se não for encontrado
    """
    try:
        soup = BeautifulSoup(htmlcontent, "html.parser")
        element = soup.find("h1")
        if element:
            dataDict = {"content":element.text}
            return dataDict
        else:
            print("Elemento não encontrado")
            return None
    except Exception as e:
        print(f"Erro do bs4:{e}")
        return None
        


#Variaveis de configuração
url = "http://bianca.com/"
host = ""

#Iniciando o Flask para a pagina da API
app = Flask(__name__)


@app.route('/')
def home():
    """
    Função para a home da API
    """
    pageContent = getPageContent(url)
    dict = getDict(pageContent)
    return jsonify(dict)


if __name__ == '__main__':
    app.run(host=host)


