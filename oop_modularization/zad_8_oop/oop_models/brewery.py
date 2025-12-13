# ==============================
# ZADANIE 8 — brewery.py
# ==============================
# Ten plik zawiera tylko klasę Brewery.
# Klasa odpowiada za przechowywanie danych JEDNEGO browaru
# oraz za czytelne wypisanie obiektu metodą __str__.

class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        address_1: str,
        address_2: str,
        address_3: str,
        city: str,
        state_province: str,
        postal_code: str,
        country: str,
        longitude: str,
        latitude: str,
        phone: str,
        website_url: str,
        state: str,
        street: str,
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self) -> str:
        return (
            f"Brewery:\n"
            f"  id: {self.id}\n"
            f"  name: {self.name}\n"
            f"  type: {self.brewery_type}\n"
            f"  city: {self.city}\n"
            f"  address: {self.street}\n"
            f"  phone: {self.phone}\n"
            f"  website: {self.website_url}"
        )
