def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")

a = get_number("Podaj pierwszą liczbę: ")
b = get_number("Podaj drugą liczbę: ")
print("Suma:", a + b)

input("Naciśnij Enter, aby zakończyć...")
