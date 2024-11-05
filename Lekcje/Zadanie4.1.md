## Roguelike game 

Celem tego zadania będzie stworzenie gry w poziomie commandline.

Co należy przeczytać i zrozumieć przed rozpoczęciem zadania.

- Zagrać w grę którą zamierza się stworzyć przykład wystawiony webowo: https://tung.github.io/ruggrogue/play/
- programowanie obiektowe - o co chodzi na czym polega (Klasa, Obiekt, atrybuty [...])
- sposób tworzenia projektu w pythonie - dzielenie na wiele plików, import plików
- *instalowanie zewnętrznych bibliotek w pythonie - pip3 (przyda się na późniejszym etapie)


### Etap 1
Celem etapu pierwszego jest stworzenie bardzo prostej gry w której będziemy wyrózniać 3 zasadnicze obiekty:

- Bohater gry
- pole na którym bohater może stanąć
- pole na którym bohater nie może stanąć

Mechanika gry:
- Bohater może poruszać się za pomocą strzałek lub wsad
- Mapa musi się odświeżać (może po każdym naciśnięciu klawisza, może co okeśloną ilośc czasu?)
- Bohater może chodzić po jednych kratkach a po innych nie.

Oczekiwany rezultat pierwszego etapu:

#########################
#.......................#
#.......................#
#.......................#
#.......................#
#.......................#
#.......................#
#.......................#
#.......................#
#..........@............#
#.......................#
#########################

@ to bohater który będzie mógł poruszać się po . ale nie będzie mógł po #