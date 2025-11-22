def suma_dwoch_wieksza_lub_rowna(a: int, b: int, c: int) -> bool:
    # Funkcja przyjmuje trzy liczby całkowite: a, b, c.
    # Sprawdza, czy suma dwóch pierwszych (a + b)
    # jest większa lub równa trzeciej liczbie (c).
    # Jeśli tak — zwraca True, w przeciwnym razie — False.

    return (a + b) >= c  # porównanie wartości zwraca wynik typu bool


if __name__ == "__main__":
    # Dane testowe — możesz je zmienić
    liczba1 = 3
    liczba2 = 5
    liczba3 = 7

    wynik = suma_dwoch_wieksza_lub_rowna(liczba1, liczba2, liczba3)  # wynik logiki

    print(wynik)  # wypisze True lub False w zależności od danych
