## Roguelike game 


### Etap 2

Celetem tego etapu będzie wzbogacenie gry o dodatkowe funkcjonalności:

1. możliwość zaczytania mapy bezpośrednio z pliku
2. nadanie grze wyglądu - zastąpienie znaków ASCII przez obrazki i jednocześnie migracja z konsoli na formę okienkową gry. W tym celu będzie potrzebne zainstalowanie biblioteki pygame. (patrz instalacja przez pip)
3. dodanie przeciwników - przeciwnik musi posiadać punkty życia oraz musi mieć możliwość odbierania życia bohaterowi. Powinien też chodzić. Na tym etapie warto zastanowić się jak będzie odbywała się walka (zadawanie obrażeń itp) - do przemyślenia
4. Dodanie przedmiotów oraz ekwipunku - bohater może zbierać przedmioty które wpływają na jego statystyki (obrona atak)

Każdy obiekt (potwór czy przedmiot) będzie pewnym znakiem (litera, cyfra cokolwiek) natomiast implementacja punktu 2 pozwoli na nadanie im wyglądu. W pewnym miejscu w kodzie będzie trzeba zrobić mapping np:
# -> obrazek1
$ -> obrazek2
. -> obrazek3
[...]
