# pytest to biblioteka do testów
# Dzięki niej możemy pisać testy jako zwykłe funkcje i robić "assert"
import pytest

# Importujemy funkcje, które chcemy testować
# (czyli te, które napisałaś w utils.py)
from utils import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime,
)


# =========================
# TESTY: is_palindrome
# =========================
class TestIsPalindrome:
    # Test 1: zwykły palindrom
    def test_kajak_true(self):
        # assert sprawdza warunek
        # jeśli to nie będzie True -> test się wysypie
        assert is_palindrome("kajak") is True

    # Test 2: zdanie z dużymi literami i spacjami
    def test_sentence_true(self):
        assert is_palindrome("Kobyła ma mały bok") is True

    # Test 3: coś co NIE jest palindromem
    def test_python_false(self):
        assert is_palindrome("python") is False

    # Test 4: pusty string - w zadaniu ma być True
    def test_empty_true(self):
        assert is_palindrome("") is True

    # Test 5: pojedynczy znak - też True
    def test_single_char_true(self):
        assert is_palindrome("A") is True


# =========================
# TESTY: fibonacci
# =========================
class TestFibonacci:
    def test_fib_0(self):
        assert fibonacci(0) == 0

    def test_fib_1(self):
        assert fibonacci(1) == 1

    def test_fib_5(self):
        assert fibonacci(5) == 5

    def test_fib_10(self):
        assert fibonacci(10) == 55

    # test wyjątku:
    # jeśli fibonacci(-1) ma rzucić ValueError, to test musi to sprawdzić
    def test_negative_raises(self):
        with pytest.raises(ValueError):
            fibonacci(-1)


# =========================
# TESTY: count_vowels
# =========================
class TestCountVowels:
    def test_python(self):
        # "Python" ma tylko 'o, y' jako samogłoski -> 2
        assert count_vowels("Python") == 2

    def test_all_vowels(self):
        assert count_vowels("AEIOUY") == 6

    def test_no_vowels(self):
        assert count_vowels("bcd") == 0

    def test_empty(self):
        assert count_vowels("") == 0

    def test_polish_text(self):
        # WAŻNE:
        # Nasza implementacja liczy tylko: a,e,i,o,u,y
        # NIE zamieniamy 'ó' na 'o'
        # "Próba żółwia" -> samogłoski wg naszego zestawu:
        # a, i, a -> razem 3
        assert count_vowels("Próba żółwia") == 3


# =========================
# TESTY: calculate_discount
# =========================
class TestCalculateDiscount:
    def test_100_20_percent(self):
        assert calculate_discount(100, 0.2) == 80.0

    def test_discount_zero(self):
        assert calculate_discount(50, 0) == 50.0

    def test_discount_one(self):
        assert calculate_discount(200, 1) == 0.0

    # discount < 0 -> ValueError
    def test_discount_below_range_raises(self):
        with pytest.raises(ValueError):
            calculate_discount(100, -0.1)

    # discount > 1 -> ValueError
    def test_discount_above_range_raises(self):
        with pytest.raises(ValueError):
            calculate_discount(100, 1.5)


# =========================
# TESTY: flatten_list
# =========================
class TestFlattenList:
    def test_flat(self):
        assert flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_nested(self):
        assert flatten_list([1, [2, 3], [4, [5]]]) == [1, 2, 3, 4, 5]

    def test_empty(self):
        assert flatten_list([]) == []

    def test_deep_single(self):
        assert flatten_list([[[1]]]) == [1]

    def test_deep(self):
        assert flatten_list([1, [2, [3, [4]]]]) == [1, 2, 3, 4]


# =========================
# TESTY: word_frequencies
# =========================
class TestWordFrequencies:
    def test_to_be_or_not(self):
        assert word_frequencies("To be or not to be") == {
            "to": 2,
            "be": 2,
            "or": 1,
            "not": 1,
        }

    def test_hello_hello(self):
        assert word_frequencies("Hello, hello!") == {"hello": 2}

    def test_empty(self):
        assert word_frequencies("") == {}

    def test_python_repeats(self):
        assert word_frequencies("Python Python python") == {"python": 3}

    def test_ala_sentence(self):
        # Test sprawdza, czy ignorujemy interpunkcję (kropki, przecinki)
        assert word_frequencies("Ala ma kota, a kot ma Ale.") == {
            "ala": 1,
            "ma": 2,
            "kota": 1,
            "a": 1,
            "kot": 1,
            "ale": 1,
        }


# =========================
# TESTY: is_prime
# =========================
class TestIsPrime:
    # parametrize = jeden test, wiele przypadków
    # zamiast pisać 7 osobnych testów
    @pytest.mark.parametrize(
        "n, expected",
        [
            (2, True),
            (3, True),
            (4, False),
            (0, False),
            (1, False),
            (5, True),
            (97, True),
        ],
    )
    def test_primes(self, n, expected):
        assert is_prime(n) is expected
