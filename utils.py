# Importujemy moduł re (regular expressions)
# Użyjemy go później do wyciągania słów z tekstu
import re


def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy tekst jest palindromem.
    Palindrom = czytany od przodu i od tyłu wygląda tak samo.
    Ignorujemy:
    - wielkość liter
    - spacje
    """

    # Tworzymy nowy napis:
    # - bierzemy każdy znak z tekstu
    # - zamieniamy go na małą literę (lower)
    # - pomijamy spacje (isspace)
    normalized = "".join(
        ch.lower() for ch in text if not ch.isspace()
    )

    # Sprawdzamy:
    # - normalized[::-1] to odwrócony napis
    # - jeśli są równe → True, w przeciwnym razie False
    return normalized == normalized[::-1]


def fibonacci(n: int) -> int:
    """
    Zwraca n-ty element ciągu Fibonacciego.
    fibonacci(0) = 0
    fibonacci(1) = 1
    """

    # Jeśli ktoś poda liczbę ujemną → błąd
    if n < 0:
        raise ValueError("n must be >= 0")

    # a i b to dwie kolejne liczby ciągu
    a = 0
    b = 1

    # Pętla wykona się n razy
    for _ in range(n):
        # Przesuwamy się w ciągu:
        # nowa wartość a = stare b
        # nowa wartość b = a + b
        a, b = b, a + b

    # Po zakończeniu pętli a jest n-tym elementem
    return a


def count_vowels(text: str) -> int:
    """
    Zlicza samogłoski w tekście.
    Samogłoski: a, e, i, o, u, y
    Wielkość liter nie ma znaczenia.
    """

    # Zbiór samogłosek (set działa szybciej niż lista)
    vowels = {"a", "e", "i", "o", "u", "y"}

    # Licznik samogłosek
    count = 0

    # Przechodzimy po każdym znaku w tekście
    for ch in text.lower():
        # Jeśli znak jest samogłoską → zwiększamy licznik
        if ch in vowels:
            count += 1

    return count


def calculate_discount(price: float, discount: float) -> float:
    """
    Oblicza cenę po zniżce.
    discount musi być w zakresie od 0 do 1.
    """

    # Sprawdzamy poprawność zniżki
    if discount < 0 or discount > 1:
        raise ValueError("discount must be between 0 and 1")

    # Obliczamy nową cenę:
    # np. 100 * (1 - 0.2) = 80
    final_price = price * (1 - discount)

    return final_price


def flatten_list(nested_list: list) -> list:
    """
    Spłaszcza listę zagnieżdżoną (rekurencja).
    """

    # Lista wynikowa
    result = []

    # Iterujemy po elementach listy
    for item in nested_list:

        # Jeśli element JEST listą → wołamy funkcję ponownie
        if isinstance(item, list):
            # extend dodaje wiele elementów naraz
            result.extend(flatten_list(item))

        # Jeśli element NIE jest listą → dodajemy go
        else:
            result.append(item)

    return result


def word_frequencies(text: str) -> dict:
    """
    Liczy, ile razy każde słowo występuje w tekście.
    Ignoruje:
    - wielkość liter
    - interpunkcję
    """

    # Zamieniamy tekst na małe litery
    lower_text = text.lower()

    # Wyciągamy słowa (bez przecinków, kropek itd.)
    words = re.findall(r"\w+", lower_text)

    # Słownik wynikowy
    frequencies = {}

    # Iterujemy po słowach
    for word in words:

        # Jeśli słowo już jest w słowniku → zwiększamy licznik
        if word in frequencies:
            frequencies[word] += 1

        # Jeśli nie ma → dodajemy z wartością 1
        else:
            frequencies[word] = 1

    return frequencies


def is_prime(n: int) -> bool:
    """
    Sprawdza, czy liczba jest pierwsza.
    """

    # Liczby < 2 NIE są pierwsze
    if n < 2:
        return False

    # 2 jest pierwsza
    if n == 2:
        return True

    # Parzyste > 2 NIE są pierwsze
    if n % 2 == 0:
        return False

    # Sprawdzamy dzielniki od 3 do sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True
