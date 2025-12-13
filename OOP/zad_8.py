import requests
import argparse

# =========================
# KROK 1: Klasa Brewery
# =========================


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


# =========================
# KROK 2: Argumenty z linii poleceń
# =========================


def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch breweries from Open Brewery DB")

    parser.add_argument(
        "--city", type=str, help="Filter breweries by city name", required=False
    )

    return parser.parse_args()


# =========================
# KROK 3: Główna logika programu
# =========================


def main():
    args = parse_arguments()
    city = args.city

    url = "https://api.openbrewerydb.org/v1/breweries"

    params = {"page": 1, "per_page": 20}

    # Jeśli użytkownik podał --city, dodajemy filtr
    if city is not None:
        params["by_city"] = city

    response = requests.get(url, params=params)
    print("STATUS:", response.status_code)

    data = response.json()

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

    # =========================
    # KROK 4: Wyświetlanie wyników
    # =========================

    for brewery in breweries:
        print(brewery)
        print("-" * 40)


# =========================
# KROK 5: Punkt startowy skryptu
# =========================

if __name__ == "__main__":
    main()
