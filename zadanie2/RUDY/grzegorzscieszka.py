def get_number(prompt):
    while True:
        try:
            liczba = input(prompt)
            return float(liczba)  
        except ValueError:
            print("Podaj inną liczbę")  

def main():
    liczba1 = get_number("Podaj liczbę 1: ")
    liczba2 = get_number("Podaj liczbę 2: ")
    
    suma = liczba1 + liczba2
    print("Suma: {suma}")