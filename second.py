def cislo_text(cislo):
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100

    cislo = int(cislo)

    jednotky = ["nula", "jedna", "dva", "tři", "čtyři",
                "pět", "šest", "sedm", "osm", "devět"]

    teen = ["deset", "jedenáct", "dvanáct",
                          "třináct", "čtrnáct", "patnáct",
                          "šestnáct", "sedmnáct", "osmnáct",
                          "devatenáct"]

    desitky = ["", "", "dvacet", "třicet", "čtyřicet",
               "padesát", "šedesát", "sedmdesát",
               "osmdesát", "devadesát"]

    if cislo < 0 or cislo > 100:
            return "Číslo musí být od 0 do 100"

    if cislo < 10:
        return jednotky[cislo]

    elif cislo < 20:
        return teen[cislo - 10]

    elif cislo == 100:
        return "sto"
    

    desitka = cislo // 10
    jednotka = cislo % 10
    

    if jednotka == 0:
        return desitky[desitka]

    return desitky[desitka] + " " + jednotky[jednotka]


if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)