import sys
import requests
import json


url = 'https://www.jcu.cz/cz/'
url1 = 'https://data.carnewschina.com/suggest?q='
url2 = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'


def get_model_names(prefix):
    return []

def download_rates():
    r = requests.get(url2)
    if r.status_code != 200:
        return {}
    data = r.text
    lines = data.splitlines()[2:]
    vysledek = {}
    for line in lines:
        hodnoty = line.split("|")
        vysledek[hodnoty[3]] = float(hodnoty[4].replace(",", ".")) / int(hodnoty[2])
    return vysledek


if __name__ == "__main__":
    rates = download_rates()
    print(rates)