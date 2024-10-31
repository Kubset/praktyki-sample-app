import random

def get_number(prompt):
    while True:
        try:
            zakres = int(input(prompt))
            if 1 <= zakres <= 49:
                return zakres
            else: 
                print("Liczba musi być w zakresie od 1 do 49.")
        except ValueError:
            print("Niepoprawna wartość.")

liczba1 = get_number("Podaj liczbę 1: ")
liczba2 = get_number("Podaj liczbę 2: ")
liczba3 = get_number("Podaj liczbę 3: ")
liczba4 = get_number("Podaj liczbę 4: ")
liczba5 = get_number("Podaj liczbę 5: ")
liczba6 = get_number("Podaj liczbę 6: ")

zbior_liczb = {liczba1, liczba2, liczba3, liczba4, liczba5, liczba6}

while True:
    try:
        trafienia = int(input("Podaj ile ma być trafień, aby zakończyć program: "))
        if trafienia < 1:
            print("Liczba trafień musi być większa niż 0.")
        else:
            break
    except ValueError:
        print("Niepoprawna wartość.")

hits = 0
losowania = 0  

while hits < trafienia:
    wylosowane_liczby = random.sample(range(1, 50), 6)
    print("Wylosowane liczby to:", wylosowane_liczby)

 
    hits = len(zbior_liczb.intersection(wylosowane_liczby))
    print("Ilość trafionych liczb:", hits)

    losowania += 1  

print("Dziękujemy za grę! ")
print(f"liczba losowań: {losowania}")
