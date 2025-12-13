# ==============================
# ZADANIE 2 — main.py
# ==============================
# Ten plik jest PLIKIEM URUCHOMIENIOWYM.
#
# Jego rola:
# - zebrać wszystkie klasy z pakietu oop_models
# - utworzyć obiekty
# - pokazać, że importy niezależne działają poprawnie
#
# Zgodnie z ideą modularizacji:
# - klasy są w osobnych plikach
# - logika "sklejania" jest tutaj

# IMPORTY NIEZALEŻNE (absolutne) — zgodnie z PEP8
from oop_models.book import Book
from oop_models.employee import Employee
from oop_models.library import Library
from oop_models.order import Order
from oop_models.student import Student


def main():
    """
    Funkcja główna programu (entry point).
    Tutaj:
    - tworzymy obiekty
    - korzystamy z klas zaimportowanych z innych modułów
    """

    # ------------------------------
    # Tworzenie bibliotek
    # ------------------------------
    library1 = Library(
        "Warszawa",
        "Marszałkowska 10",
        "00-001",
        "8:00-18:00",
        "111-222-333",
    )
    library2 = Library(
        "Kraków",
        "Długa 5",
        "30-001",
        "9:00-17:00",
        "444-555-666",
    )

    # ------------------------------
    # Tworzenie książek
    # (Book zawiera obiekt Library)
    # ------------------------------
    book1 = Book(library1, "2010", "Adam", "Mickiewicz", 300)
    book2 = Book(library1, "2015", "Henryk", "Sienkiewicz", 450)
    book3 = Book(library2, "2020", "Olga", "Tokarczuk", 380)
    book4 = Book(library2, "2005", "Bolesław", "Prus", 520)
    book5 = Book(library1, "2018", "Andrzej", "Sapkowski", 600)

    # ------------------------------
    # Tworzenie pracowników
    # ------------------------------
    employee1 = Employee(
        "Jan",
        "Kowalski",
        "2020-01-01",
        "1990-05-05",
        "Warszawa",
        "Polna 3",
        "00-100",
        "123-123-123",
    )
    employee2 = Employee(
        "Anna",
        "Nowak",
        "2018-06-15",
        "1988-03-12",
        "Kraków",
        "Leśna 7",
        "30-200",
        "234-234-234",
    )

    # ------------------------------
    # Tworzenie studentów
    # ------------------------------
    student1 = Student("Kasia", [60, 70, 80])
    student2 = Student("Ola", [90, 85, 95])

    # ------------------------------
    # Tworzenie zamówień
    # (Order zawiera Student, Employee i listę Book)
    # ------------------------------
    order1 = Order(employee1, student1, [book1, book2], "2025-12-13")
    order2 = Order(employee2, student2, [book3, book4, book5], "2025-12-14")

    # ------------------------------
    # Wyświetlenie wyników
    # ------------------------------
    print(order1)
    print("\n" + "=" * 40 + "\n")
    print(order2)


# Standardowy punkt wejścia programu w Pythonie
if __name__ == "__main__":
    main()
