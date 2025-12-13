from typing import List  # Import typu listy dla czytelności


def zawiera_wartosc(lista: List[int], wartosc: int) -> bool:
    # Funkcja zwraca wartość logiczną (True/False).
    # Sprawdza, czy 'wartosc' znajduje się w liście 'lista'.

    return wartosc in lista  # operator 'in' sprawdza obecność elementu


if __name__ == "__main__":
    przyklad_lista = [1, 2, 3, 4, 5]  # Przykładowa lista liczb
    przyklad_wartosc = 3  # Szukana wartość

    wynik = zawiera_wartosc(przyklad_lista, przyklad_wartosc)
    print(wynik)  # Powinno wypisać True
