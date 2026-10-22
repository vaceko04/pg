def levensteinova_vzdalenost(dotaz1, dotaz2):
    """
    Levenshteinova vzdálenost měří, jak moc se dva textové řetězce liší.
    Představuje minimální počet úprav (smazání, vložení nebo nahrazení jednoho písmene), 
    které musíme provést, abychom jeden řetězec přeměnili na druhý.

    Příklady:
    - Pokud jsou řetězce naprosto stejné, vzdálenost je 0 (např. "auto" a "auto").
    - Pro řetězce "čas" a "čaj" je vzdálenost 1 (stačí jedno písmeno nahradit).
    - Čím větší číslo, tím jsou slova odlišnější.

    Využívá se např. v opravě překlepů nebo při vyhledávání (tzv. "Mysleli jste...?").

    :param dotaz1: První textový řetězec
    :param dotaz2: Druhý textový řetězec
    :return: Celé číslo udávající míru rozdílu
    """
    levenstein = 0
    lenght = min(len(dotaz1), len(dotaz2))
    for i in range(lenght):
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"
    query4 = "seznam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))

    print(levensteinova_vzdalenost(query1, query4))