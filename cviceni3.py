#def my_range_while(start, stop, step=1):
    # pomoci cyklu while vytvorte vlastni implementaci funkce range()
    #vysledek = []
    #x = start
    
    #while (x > stop if step < 0 else x < stop):
     #   vysledek.append(x)
      #  x += step
    #return vysledek

def my_enumerate_for(iterable, start=0):
    # implementujte funkci enumerate pomoci cyklu for
    vysledek = []
    for x in range (start, len(iterable)):
        vysledek.append((x+start, iterable[x]))
    return vysledek
def my_enumerate_while(iterable, start=0):
    vysledek = []
    i = 0
    while i < len(iterable):
        vysledek.append((i+start, iterable))
        i += 1
    return vysledek

def my_zip(*iterables):
    vysledek = []
    lenght = min(len(iterable) for iterable in iterables)
    i = 0
    while i < lenght:
        value = []
        for iterable in iterables:
            value.append(iterable[i])
        vysledek.append(value)
        i += 1
    return vysledek

if __name__ == "__main__":

    #print(list(range(1, 10, -1)))
    #print(my_range_while(1, 10, -1))

   # print(list(enumerate(["aaa", "bbb", "ccc", 100])))
   # print(my_enumerance_for(["aaa", "bbb", "ccc", 100])))
   # print(my_enemerance_while(["aaa", "bbb", "ccc", 100])))

    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek = [30, 20, 24, 18, 27]
    vaha = [50, 80, 90, 55, 67]

    vysledek = list(zip(jmena, vek, vaha))
    print(vysledek)
    # for jmeno, vek, vaha in vysledek
    #     print(f"{jmeno} je {vek} let a vazi {vaha} kg")

    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)
