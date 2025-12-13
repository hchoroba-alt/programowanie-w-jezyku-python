def czy_parzysta(liczba: int) -> bool:
    # Funkcja przyjmuje argument typu int.
    # Zwraca True, jeśli liczba jest parzysta.
    # Zwraca False, jeśli liczba jest nieparzysta.
    return liczba % 2 == 0  # liczba parzysta ma resztę z dzielenia przez 2 równą 0


if __name__ == "__main__":
    testowa_liczba = 7  # tutaj można wpisać dowolną liczbę

    wynik = czy_parzysta(
        testowa_liczba
    )  # zapisujemy wynik działania funkcji do zmiennej

    # Sprawdzenie warunku logicznego i wypisanie odpowiedniego komunikatu
    if wynik:
        print("Liczba parzysta")
    else:
        print("Liczba nieparzysta")
