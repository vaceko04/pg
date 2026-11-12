class MojeVyjimka(Exception):
    pass

class BankovniUcet:
    def __init__(self, jmeno, urok):
        self.jmeno = jmeno
        self.urok = urok
        self.__zustatek = 0

    def __str__(self):
        return f"Na ucte {self.jmeno} je {self.__zustatek} Kc"

    def vloz(self, castka):
        # vlozit jde pouzde kladna castka, jinak vyhodit vyjimku (pomoci raise)
        self.castka = castka
        if castka > 0:
            self.__zustatek += castka
        else:
            raise(MojeVyjimka)

    def vyber(self,castka):
        # vybrat jde pouze kladna castka nizsi ne je __zustatek, jinka vyhodit vyjimku (pomoci raise)
        self.castka = castka
        if self.__zustatek > castka:
            self.__zustatek -= castka
        else:
            raise(MojeVyjimka)


    def pricti_uroky(self):
        # navys zustatek uctu o nasobek uroku, tzn. pokud je urok 0,05 -> zustatek += zustatek * 0,05
        self.__zustatek += self.__zustatek * 0.05

if __name__ == "__main__":
    ucet = BankovniUcet("sporici", 0.05)
    ucet.vloz(200)
    ucet.vyber(100)
    ucet.pricti_uroky()
    print(ucet)