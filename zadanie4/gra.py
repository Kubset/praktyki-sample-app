from postac import Postac
from mapa import Mapa

def gra():
    postac = Postac(10, 9)
    mapa = Mapa()

    while True:
        mapa.wyswietl(postac)
        kierunek = input("Wprowadź kierunek (w/a/s/d): ")
        if kierunek in ['w', 'a', 's', 'd']:
            postac.ruch(kierunek, mapa)

if __name__ == "__main__":
    gra()
