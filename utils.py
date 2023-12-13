from dotenv import load_dotenv
import os
import urllib.request, json

def getAPIResponse(url, request):
    load_dotenv()

    api_url = os.getenv(url)
    print(api_url)
    payload = request.get_json()
    print(payload)

    #tratar o payload para buscar os dados e enviar o valor

    headers = {'Content-Type': 'application/json'}
    req     = urllib.request.Request(api_url, data=json.dumps(payload).encode('utf-8'), headers=headers)

    response = urllib.request.urlopen(req)
    result   = response.read().decode('utf-8')

    return result