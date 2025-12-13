# ==============================
# ZADANIE 8 — main.py
# ==============================
# Plik uruchomieniowy.
# Cel:
# 1) wczytać argument --city z linii poleceń (argparse)
# 2) połączyć się z Open Brewery DB (requests)
# 3) pobrać 20 browarów (z filtrem po mieście, jeśli podano)
# 4) utworzyć listę obiektów Brewery
# 5) wypisać każdy obiekt (wywoła __str__)

import argparse
import requests

from oop_models.brewery import Brewery


# ------------------------------
# KROK 1: Argumenty z linii poleceń
# ------------------------------
def parse_arguments():
    """
    Czytamy argumenty uruchomienia programu.
    Przykład:
      python3 main.py --city=Berlin
    """
    parser = argparse.ArgumentParser(
        description="Fetch breweries from Open Brewery DB"
    )

    parser.add_argument(
        "--city",
        type=str,
        help="Filter breweries by city name",
        required=False,
    )

    return parser.parse_args()


# ------------------------------
# KROK 2: Główna logika programu
# ------------------------------
def main():
    # Wczytanie argumentów z linii poleceń
    args = parse_arguments()
    city = args.city

    # Endpoint API
    url = "https://api.openbrewerydb.org/v1/breweries"

    # Parametry zapytania:
    # - per_page=20: chcemy 20 pierwszych wyników
    # - page=1: pierwsza strona wyników
    params = {
        "page": 1,
        "per_page": 20,
    }

    # Jeśli podano miasto, dokładamy filtr.
    # Open Brewery DB używa parametru by_city.
    if city is not None:
        params["by_city"] = city

    # Wysyłamy zapytanie GET do API
    response = requests.get(url, params=params)

    # Status 200 oznacza sukces
    print("STATUS:", response.status_code)

    # Zamieniamy odpowiedź JSON na strukturę Pythona:
    # tutaj będzie to lista słowników (list[dict])
    data = response.json()

    # Lista na obiekty Brewery
    breweries = []

    # Zamieniamy każdy słownik (item) w obiekt Brewery
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

    # ------------------------------
    # KROK 3: Wyświetlanie wyników
    # ------------------------------
    for brewery in breweries:
        print(brewery)
        print("-" * 40)


# Punkt startowy programu
if __name__ == "__main__":
    main()
