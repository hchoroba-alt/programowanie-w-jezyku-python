"""
ZADANIE 7 — main.py

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

from oop_models.brewery import Brewery  # importujemy klasę z osobnego pliku


# =========================
# KROK 1: Pobranie danych z API
# =========================

def main():
    # Adres endpointu API, który zwraca listę browarów (JSON)
    url = "https://api.openbrewerydb.org/v1/breweries"

    # Parametry zapytania:
    # - page=1: pierwsza strona wyników
    # - per_page=20: chcemy dokładnie 20 obiektów
    params = {"page": 1, "per_page": 20}

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
    print("TYP danych:", type(data))
    print("LICZBA elementów:", len(data))

    # (Opcjonalnie) sprawdzenie kluczy pierwszego obiektu.
    print("KLUCZE pierwszego obiektu:", data[0].keys())

    # =========================
    # KROK 2: Zamiana słowników na obiekty Brewery
    # =========================

    breweries = []

    for item in data:
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
            street=item["street"],
        )
        breweries.append(brewery)

    # Po pętli mamy listę obiektów klasy Brewery.
    print("LICZBA obiektów Brewery:", len(breweries))
    print("TYP pierwszego obiektu:", type(breweries[0]))

    # =========================
    # KROK 3: Wyświetlenie każdego browaru
    # =========================

    for brewery in breweries:
        print(brewery)
        print("-" * 40)


if __name__ == "__main__":
    main()
