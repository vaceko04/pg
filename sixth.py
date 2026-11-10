import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    r = requests.get(url)
    if r.status_code != 200:
            print(f"Stahovani skoncilo chybou")
            return []
    data = r.text.split('<a href="')
    data.pop(0)

    for x in data:
         hrefs.append(x.split('"')[0])


    return hrefs
    

    


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        print(download_url_and_get_all_hrefs(url))
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")

    
    



