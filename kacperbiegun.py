def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Niepoprawna wartość. Podaj liczbę.")

a = get_number("Podaj pierwszą liczbę: ")
b = get_number("Podaj drugą liczbę: ")
print("Suma:", a + b)