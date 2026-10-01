def add(a,b):
    c = a + b
    return c 







def div(a, b):
    if b == 0:
        # prvni cast, kdy b je 0
        vysledek = 0
    else:
        # druha cast, kdy b je nenulove
        vysledek = a / b
    return vysledek
def je_delitelne_beze_zbytku(a, b):
    x = a % b
    if x == 0:
        return je_delitelne_beze_zbytku
    else:
        return "neni delitelne beze zbytku"

def je_delitelne_3(a):
    return je_delitelne_beze_zbytku(a,  3)

if __name__ == "__main__":
    # x = add(1,2)
    # x = mul(1,2,3)
    # x = div(10, 1)
    # vysledek = je_delitelne_beze_zbytku(10, 3)
    vysledek = je_delitelne_3(10)
    print(vysledek)