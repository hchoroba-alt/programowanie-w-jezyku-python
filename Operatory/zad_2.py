from typing import Tuple  # (opcjonalny import — dla typu krotki, jeśli chcielibyśmy zwracać 2 wartości)


def mnoz(a: int, b: int) -> int:
    # Funkcja przyjmuje dwa argumenty typu int: 'a' i 'b'.
    # Zwraca wynik mnożenia obu liczb.

    return a * b  # operator * mnoży dwie liczby całkowite


if __name__ == "__main__":
    # Przykładowe dane do testu działania funkcji
    liczba1 = 6
    liczba2 = 7

    wynik = mnoz(liczba1, liczba2)  # wywołanie funkcji
    print(wynik)  # powinno wypisać: 42
