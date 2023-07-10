import urllib.request
import json

url = 'http://api.exchangeratesapi.io/v1/latest?access_key=6d58cfeda7b35c0b4061278821ad77f7&symbols=USD,AUD,' \
      'CAD,PLN,MXN,ARS,BRL&format=1'


# Realiza um request na exchange rates API que retorna um json contendo a cotação atual das moedas especificadas
# USD,AUD,CAD,PLN,MXN,ARS,BRL. Todas com o valor em relação ao Euro
def api_request() -> dict[str | str, int, dict[str | int]]:
    request = urllib.request.urlopen(url)
    return json.loads(request.read())
