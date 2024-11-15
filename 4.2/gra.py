import pygame
from postac import Postac
from mapa import Mapa


OKNO_SZEROKOSC = 1000
OKNO_WYSOKOSC = 600
ROZMIAR_KRATKI = 40


BIALY = (255, 255, 255)
CZARNY = (0, 0, 0)
NIEBIESKI = (0, 0, 255)

def gra():
    pygame.init()


    ekran = pygame.display.set_mode((OKNO_SZEROKOSC, OKNO_WYSOKOSC))
    pygame.display.set_caption("Gra w Pygame")


    postac = Postac(1, 1)  
    mapa = Mapa()  
    zegar = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    postac.ruch('w', mapa)
                elif event.key == pygame.K_a:
                    postac.ruch('a', mapa)
                elif event.key == pygame.K_s:
                    postac.ruch('s', mapa)
                elif event.key == pygame.K_d:
                    postac.ruch('d', mapa)

        ekran.fill(BIALY)

        for y, wiersz in enumerate(mapa.dane):
            for x, pole in enumerate(wiersz):
                kolor = CZARNY if pole == 1 else BIALY
                pygame.draw.rect(
                    ekran,
                    kolor,
                    (x * ROZMIAR_KRATKI, y * ROZMIAR_KRATKI, ROZMIAR_KRATKI, ROZMIAR_KRATKI)
                )

        pygame.draw.rect(
            ekran,
            NIEBIESKI,
            (
                postac.x * ROZMIAR_KRATKI,
                postac.y * ROZMIAR_KRATKI,
                ROZMIAR_KRATKI,
                ROZMIAR_KRATKI
            )
        )

        pygame.display.flip()

        zegar.tick(30)

    pygame.quit()

if __name__ == "__main__":
    gra()