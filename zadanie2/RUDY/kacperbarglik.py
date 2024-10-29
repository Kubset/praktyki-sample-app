# zadanie2.py

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę. ")

a = get_number("podaj pierwszą liczbę: ")
b = get_number("podaj drugą liczbę")
print("suma:", a+ b)