# ==============================
# ZADANIE 3 — main.py
# ==============================
# Plik uruchomieniowy.
# Importujemy klasy dziedziczące po Property
# i tworzymy przykładowe obiekty.

from oop_models.house import House
from oop_models.flat import Flat


def main():
    # Tworzymy obiekt klasy House
    house = House(
        120,
        5,
        850000,
        "Warszawa, ul. Leśna 3",
        600,
    )

    # Tworzymy obiekt klasy Flat
    flat = Flat(
        55,
        2,
        420000,
        "Kraków, ul. Długa 12",
        3,
    )

    # Wyświetlamy obiekty
    print(house)
    print()
    print(flat)


if __name__ == "__main__":
    main()
