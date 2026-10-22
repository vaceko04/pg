def jaccardova_vzdalenost_mnozin(mnozina1, mnozina2):
    """
    Jaccardova vzdálenost měří, jak moc se dvě množiny liší. 
    Výsledek je vždy číslo v rozmezí od 0 do 1:
    - 0 znamená, že množiny jsou naprosto identické (obsahují úplně stejné prvky).
    - 1 znamená, že jsou zcela rozdílné (nemají vůbec žádný společný prvek).
    - Čím blíže je číslo 1, tím jsou množiny odlišnější; čím blíže 0, tím jsou podobnější.

    Příklady:
    - Množina A = {"fotbal", "hokej"} a Množina B = {"hokej", "fotbal"} -> vzdálenost je 0 (jsou stejné).
    - Množina A = {"fotbal", "hokej"} a Množina B = {"tenis", "basketbal"} -> vzdálenost je 1 (nemají nic společného).
    - Množina A = {"fotbal", "hokej"} a Množina B = {"tenis", "fotbal"} -> sdílí 1 prvek z 3 celkových 
      (sjednocení je {"fotbal", "hokej", "tenis"}), vzdálenost je přibližně 0.33.

    Využívá se např. v doporučujících systémech (porovnání toho, jaké filmy nebo zboží mají dva uživatelé společné) 
    nebo při porovnávání textů.

    :param mnozina1: První množina prvků
    :param mnozina2: Druhá množina prvků
    :return: Desetinné číslo (float) od 0.0 do 1.0 udávající míru rozdílu
    """
    mnozina1 = set(mnozina1)
    mnozina2 = set(mnozina2)
    prunik = mnozina1.intersection(mnozina2)
    sjednoceni = mnozina1.union(mnozina2)
    jaccard_index = len(prunik)/len(sjednoceni)
    jaccardova_vzdalenost_mnozin = 1 - jaccard_index
    return jaccardova_vzdalenost_mnozin


if __name__ == "__main__":
    serp1 = ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    serp2 = ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    serp3 = ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]

    print(jaccardova_vzdalenost_mnozin(serp1, serp2))
    print(jaccardova_vzdalenost_mnozin(serp2, serp3))
    print(jaccardova_vzdalenost_mnozin(serp1, serp3))