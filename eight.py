def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    
    binarni_cislo = str(binarni_cislo)
    mocnina = len(binarni_cislo) - 1
    seznam = []

    for i in binarni_cislo:
        if i == "1":
            seznam.append(2 ** mocnina)
        mocnina -= 1

    return sum(seznam)       
    
def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

if __name__ == "__main__":

    cislo = input("Zadej binarni cislo: ")
    test_bin_to_dec()
    print(bin_to_dec(cislo))
    