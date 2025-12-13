"""
Skrypt: Open Brewery DB → lista obiektów Brewery → print każdego obiektu

CEL:
1) Połączyć się z API Open Brewery DB
2) Pobrać 20 pierwszych browarów
3) Zrobić klasę Brewery z atrybutami (zgodnymi z kluczami z API)
4) Utworzyć 20 instancji klasy Brewery (z danych JSON)
5) Przeiterować listę i wyświetlić każdy obiekt osobno

UWAGA:
- To jest wersja "edukacyjna": dużo komentarzy, krok po kroku.
- Używamy biblioteki requests.
"""

# =========================
# KROK 0: Importy
# =========================

import requests  # requests potrafi wysyłać zapytania HTTP (np. GET) do API


# =========================
# KROK 1: Definicja klasy Brewery (czyli "szablonu" na jeden browar)
# =========================

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
        street: str
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


# =========================
# KROK 2: Pobranie danych z API
# =========================

# Adres endpointu API, który zwraca listę browarów (JSON)
url = "https://api.openbrewerydb.org/v1/breweries"

# Parametry zapytania:
# - page=1: pierwsza strona wyników
# - per_page=20: chcemy dokładnie 20 obiektów
params = {
    "page": 1,
    "per_page": 20
}

# Wysyłamy zapytanie GET:
# API odpowie obiektem response, w którym jest status i treść odpowiedzi.
response = requests.get(url, params=params)

# Drukujemy status, żeby wiedzieć, czy serwer zwrócił poprawną odpowiedź:
# 200 = OK
print("STATUS:", response.status_code)

# Zamieniamy odpowiedź JSON → struktury Pythona:
# Jeśli API zwraca listę, to tutaj dostaniemy listę.
data = response.json()

# (Opcjonalnie) szybkie sprawdzenie: typ danych i liczba elementów.
# To pomaga upewnić się, że API zwraca to, czego się spodziewamy.
print("TYP danych:", type(data))
print("LICZBA elementów:", len(data))

# (Opcjonalnie) sprawdźmy, jakie pola (klucze) ma pierwszy element.
# Dzięki temu wiemy, jakie atrybuty ma mieć klasa Brewery.
print("KLUCZE pierwszego obiektu:", data[0].keys())


# =========================
# KROK 3: Zamiana słowników (dict) z API na obiekty klasy Brewery
# =========================

# Tworzymy pustą listę, do której będziemy dodawać obiekty Brewery.
breweries = []

# data to lista 20 słowników.
# item to JEDEN słownik opisujący JEDEN browar.
for item in data:
    # Tworzymy obiekt Brewery.
    # Każdy parametr bierzemy ze słownika item po kluczu, np. item["name"].
    brewery = Brewery(
        id=item["id"],
        name=item["name"],
        brewery_type=item["brewery_type"],
        address_1=item["address_1"],
        address_2=item["address_2"],
        address_3=item["address_3"],
        city=item["city"],
        state_province=item["state_province"],
        postal_code=item["postal_code"],
        country=item["country"],
        longitude=item["longitude"],
        latitude=item["latitude"],
        phone=item["phone"],
        website_url=item["website_url"],
        state=item["state"],
        street=item["street"]
    )

    # Dodajemy nowo utworzony obiekt do listy.
    breweries.append(brewery)

# Po pętli mamy listę 20 obiektów klasy Brewery.
print("LICZBA obiektów Brewery:", len(breweries))
print("TYP pierwszego obiektu:", type(breweries[0]))


# =========================
# KROK 4: Iteracja po liście obiektów i wyświetlenie każdego z osobna
# =========================

# Przechodzimy po każdym obiekcie w breweries.
for brewery in breweries:
    # print(brewery) automatycznie wywoła brewery.__str__()
    # dlatego zobaczysz ładny opis, a nie coś typu <object at 0x...>
    print(brewery)
    print("-" * 40)  # separator, żeby wyniki były czytelniejsze
