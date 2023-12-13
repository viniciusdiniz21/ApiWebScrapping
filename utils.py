from dotenv import load_dotenv
import os
import urllib.request, json
import requests 
from bs4 import BeautifulSoup

def getAPIResponse(url, request):
    load_dotenv()

    api_url = os.getenv(url)
    payload = request.get_json()

    #tratar o payload para buscar os dados e enviar o valor

    for item in payload:
            if 'url' in item:
                req = requests.get(item["url"])
                scrap = BeautifulSoup(req.text, 'html.parser')
                valor = scrap.find_all('strong')
                print(valor[5].text)

    return payload