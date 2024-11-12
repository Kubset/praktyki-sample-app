class Postac:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = "@"

    def ruch(self, kierunek, mapa):
        nowy_x, nowy_y = self.x, self.y

        if kierunek == 'w':
            nowy_y -= 1
        elif kierunek == 'a':
            nowy_x -= 1
        elif kierunek == 's':
            nowy_y += 1
        elif kierunek == 'd':
            nowy_x += 1

        if mapa.czy_dostepne(nowy_x, nowy_y):
            self.x, self.y = nowy_x, nowy_y
