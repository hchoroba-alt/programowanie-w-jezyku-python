from typing import List  # adnotacja typu listy


def zawiera_wartosc(lista: List[int], wartosc: int) -> bool:
    # Funkcja przyjmuje:
    # - lista: list[int] → lista liczb całkowitych
    # - wartosc: int     → liczba, której szukamy w liście
    #
    # Funkcja zwraca wartość bool:
    # - True, jeśli wartosc znajduje się w liście
    # - False, jeśli nie

    return wartosc in lista  # operator "in" sprawdza obecność elementu


if __name__ == "__main__":
    przyklad_lista = [10, 20, 30, 40, 50]  # przykładowa lista
    przyklad_wartosc = 30                 # szukana wartość

    wynik = zawiera_wartosc(przyklad_lista, przyklad_wartosc)
    print(wynik)  # True, bo 30 jest w liście
