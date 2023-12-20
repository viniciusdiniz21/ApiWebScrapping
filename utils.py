from dotenv import load_dotenv
import os
import urllib.request, json
import requests 
from bs4 import BeautifulSoup

def getAPIResponse(url, request):
    load_dotenv()

    api_url = os.getenv(url)
    econv_api = os.getenv('API')
    payload = request.get_json()

    #tratar o payload para buscar os dados e enviar o valor

    res = []

    for item in payload:
            if 'url' in item:
                req = requests.get(item["url"])
                scrap = BeautifulSoup(req.text, 'html.parser')
                valor = scrap.find_all('strong')

                extracted_value = valor[5].text


                api_payload = {
                "faturaId": item.get("faturaId", ""),
                "valor": extracted_value
                }
                res.append(api_payload)

            api_response = requests.post(api_url, json=api_payload)

            if api_response.status_code == 200:
                return res
            else:
                return {"error": "Erro na solicitação POST à API externa"}

    return res