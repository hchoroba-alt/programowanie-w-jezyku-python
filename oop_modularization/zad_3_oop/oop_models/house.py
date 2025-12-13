# ==============================
# ZADANIE 3 — house.py
# ==============================
# Klasa House:
# - DZIEDZICZY po klasie Property
# - dodaje nowe pole: plot (rozmiar działki)

from .property import Property


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        # Wywołujemy konstruktor klasy bazowej
        super().__init__(area, rooms, price, address)

        # Pole charakterystyczne tylko dla domu
        self.plot = plot

    def __str__(self):
        return (
            f"House:\n"
            f"  Area: {self.area} m2\n"
            f"  Rooms: {self.rooms}\n"
            f"  Price: {self.price}\n"
            f"  Address: {self.address}\n"
            f"  Plot size: {self.plot} m2"
        )
