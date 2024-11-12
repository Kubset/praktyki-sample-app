class Mapa:
    def __init__(self):
        self.mapa = [
            "#########################",
            "#.......................#",
            "#.......................#",
            "#.......................#",
            "#.......................#",
            "#.......................#",
            "#.......................#",
            "#.......................#",
            "#.......................#",
            "#.......................#",
            "#.......................#",
            "#########################",
        ]
        self.szerokosc = len(self.mapa[0])
        self.wysokosc = len(self.mapa)

    def czy_dostepne(self, x, y):
        return self.mapa[y][x] != '#'

    def wyswietl(self, postac):
        for y, linia in enumerate(self.mapa):
            if y == postac.y:
                linia = linia[:postac.x] + postac.symbol + linia[postac.x + 1:]
            print(linia)
