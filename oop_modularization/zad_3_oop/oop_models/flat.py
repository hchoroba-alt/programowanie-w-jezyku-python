# ==============================
# ZADANIE 3 — flat.py
# ==============================
# Klasa Flat:
# - DZIEDZICZY po klasie Property
# - dodaje nowe pole: floor (piętro)

from .property import Property


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        # Wywołujemy konstruktor klasy bazowej
        super().__init__(area, rooms, price, address)

        # Pole charakterystyczne tylko dla mieszkania
        self.floor = floor

    def __str__(self):
        return (
            f"Flat:\n"
            f"  Area: {self.area} m2\n"
            f"  Rooms: {self.rooms}\n"
            f"  Price: {self.price}\n"
            f"  Address: {self.address}\n"
            f"  Floor: {self.floor}"
        )
