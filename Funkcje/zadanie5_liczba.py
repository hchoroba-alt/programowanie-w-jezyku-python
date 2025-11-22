def sprawdz_liczbe(liczba):
    if liczba > 0:
        print("Liczba jest dodatnia.")
    elif liczba < 0:
        print("Liczba jest ujemna.")
    else:
        print("Liczba jest równa zero.")


if __name__ == "__main__":
    sprawdz_liczbe(5)
    sprawdz_liczbe(-3)
    sprawdz_liczbe(0)
