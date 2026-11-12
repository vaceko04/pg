class Osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
    
    def __str__(self):
        return f'Osoba {self.jmeno} ma {self.vek} let'

    def pridat_rok(self):
        self.vek += 1

class Student(Osoba):
    def __init__(self, jmeno, vek, rocnik):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return f"Student {self.jmeno} ma {self.vek} let a studuje {self.rocnik} rocnik"

    def pridat_rok(self):
        # metoda bude zvysovat vek a zaroven rocnik, ale pouzde do 5 (neexistuje vyssi rocnik nez 5)
        self.vek += 1
        if self.rocnik < 5:
            self.rocnik +=1

class Ucitel(Osoba):
    def __init__(self, jmeno, vek, roky_praxe):
        super().__init__(jmeno, vek)
        self.roky_praxe = roky_praxe

    def __str__(self):
        return f"Ucitel {self.jmeno} ma {self.vek} let a ma {self.roky_praxe} let praxe"

    def pridat_rok(self):
        # metoda zvysuje vek + roky_praxe
        self.vek += 1
        self.roky_praxe += 1

class Udrzbar(Osoba):
    def __init__(self, jmeno, vek):
        super().__init__(jmeno, vek)


if __name__ == "__main__":
    osoby = [Student("Tomas", 20, 2),
             Ucitel("Vlada", 44, 3),
             Student("Jana", 19, 1),
             Udrzbar("Martin", 50)]

    for osoba in osoby:
        print(osoba)