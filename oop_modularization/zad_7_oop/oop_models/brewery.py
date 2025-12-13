# ==============================
# ZADANIE 7 — brewery.py
# ==============================
# Ten plik zawiera tylko klasę Brewery.
# Klasa przechowuje dane JEDNEGO browaru zwróconego z API
# i potrafi ładnie wypisać się dzięki __str__.

class Brewery:
    """
    Ten obiekt ma przechowywać dane JEDNEGO browaru.
    Każdy obiekt tej klasy będzie odpowiadał JEDNEMU słownikowi (dict) z API.
    """

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
        # W konstruktorze zapisujemy dane do atrybutów obiektu (self.xxx).
        # self oznacza: "ten konkretny obiekt", który właśnie tworzymy.
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
        """
        Metoda magiczna __str__ mówi Pythonowi:
        "Jak mam wyświetlić ten obiekt, gdy ktoś zrobi print(obiekt)?"
        Musi ZWRÓCIĆ string (napis).
        """
        return (
            f"Brewery:\n"
            f"  id: {self.id}\n"
            f"  name: {self.name}\n"
            f"  type: {self.brewery_type}\n"
            f"  address_1: {self.address_1}\n"
            f"  address_2: {self.address_2}\n"
            f"  address_3: {self.address_3}\n"
            f"  city/state_province: {self.city}, {self.state_province}\n"
            f"  postal_code: {self.postal_code}\n"
            f"  country: {self.country}\n"
            f"  longitude: {self.longitude}\n"
            f"  latitude: {self.latitude}\n"
            f"  phone: {self.phone}\n"
            f"  website_url: {self.website_url}\n"
            f"  state: {self.state}\n"
            f"  street: {self.street}"
        )
