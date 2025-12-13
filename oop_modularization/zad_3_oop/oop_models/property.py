# ==============================
# ZADANIE 3 — property.py
# ==============================
# Klasa bazowa Property.
# Zawiera cechy wspólne dla wszystkich nieruchomości.

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms

        # Wymaganie z zadania:
        # price MUSI być typu int
        self.price = int(price)

        self.address = address
