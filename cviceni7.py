class vektor:

    def __init__(self, tmp_x, tmp_y):
        self.x = tmp_x
        self.y = tmp_y

    def __str__(self):

        return f"vektor({self.x}, {self.y})"

    def secti(self, jiny_vektor):

        return vektor(self.x + jiny_vektor.x, self.y + jiny_vektor.y)

    def vynasob(self, skalar):

        return vektor(self.x * skalar, self.y * skalar)


if __name__ == "__main__":

    v1 = vektor(10, 6)
    print(v1)

    v2 = vektor(3, 8)
    print(v1.secti(v2))
    print(v2.vynasob(2))