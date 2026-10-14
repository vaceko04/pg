def vynasob_xty_prvek(seznam, x, nasobek):
    """
    Funkce vezme x-ty prvek ze seznamu (zadano jako 1 pro prvni prvek),
    vynasobi ho pomoci * nasobek a ulozi zpet do seznamu na puvodni pozici.
    Pozor, seznam muze mit mene prvku nez x
    """
    
    if len(seznam) <= x:
        print("V seznamu neni dostatek prvku")
        return seznam
    x -= 1
    if x < 0:
        print("Index mensi nez 0")
        return seznam

    seznam[x] *= nasobek
    return seznam

def spocitej_prumer(seznam):
    """
    Funcke spocita prumer z hodnot v seznamu
    """
    pocet = len(seznam)
    if pocet <= 0:
        print("Prazdy seznam")
        return None
    suma = sum(seznam)
    
    return suma / pocet

def formatuj_text(student):
    znamky = student["znamky"]
    prumer = spocitej_prumer(znamky)
    prumer = round(prumer, 1)
    return f"Student {student["jmeno"]}{student["prijmeni"]}, Vek: {student["vek"]}, Prumer {prumer}"


if __name__ == "__main__":

    student = {
        "jmeno": "Jan",
        "prijmeni": "Novak",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    print(formatuj_text(student)) # "Student Jan Novak, Vek: 21, Prumer: 1.7"

    #seznam = vynasob_xty_prvek([1, 2, 3, 4, 5], 3, 10)
    #print(seznam) # [1, 2, 30, 4, 5]

    #prumer = spocitej_prumer(seznam)
    #print(prumer)
    #vysledek = sum(seznam)
    #print(vysledek)
