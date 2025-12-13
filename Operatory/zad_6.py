from typing import List  # adnotacja dla listy


def polacz_i_przetworz(lista1: List[int], lista2: List[int]) -> List[int]:
    """
    Funkcja:
    - łączy dwie listy w jedną,
    - usuwa duplikaty,
    - każdą liczbę podnosi do trzeciej potęgi (x^3),
    - zwraca nową listę.
    """

    # Połączenie dwóch list w jedną
    polaczona = lista1 + lista2

    # Usunięcie duplikatów poprzez konwersję do typu set (zbiór)
    bez_duplikatow = set(polaczona)

    # Podniesienie każdego elementu zbioru do potęgi 3
    wynik = [element**3 for element in bez_duplikatow]

    # Zwracamy przetworzoną listę
    return wynik


if __name__ == "__main__":
    lista_a = [1, 2, 3, 3, 4]
    lista_b = [3, 4, 5, 6]

    wynik = polacz_i_przetworz(lista_a, lista_b)
    print(wynik)  # przykładowy wynik np. [1, 8, 27, 64, 125, 216]
