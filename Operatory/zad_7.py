from dataclasses import dataclass  # Ułatwia tworzenie klas danych
from typing import Optional, List  # Typowanie: Optional, List
import requests  # Do połączenia z API HTTP


@dataclass
class Brewery:
    # Pola odpowiadające temu, co zwraca API OpenBreweryDB
    # Dokumentacja: https://www.openbrewerydb.org/documentation
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: Optional[str]
    street: Optional[str]

    @classmethod
    def from_json(cls, data: dict) -> "Brewery":
        """Tworzy obiekt Brewery z jednego elementu JSON zwróconego przez API."""

        def to_float(value) -> Optional[float]:
            # API czasem zwraca None albo string – tu bezpiecznie konwertujemy do float
            if value is None:
                return None
            try:
                return float(value)
            except (TypeError, ValueError):
                return None

        return cls(
            id=data.get("id", ""),
            name=data.get("name", ""),
            brewery_type=data.get("brewery_type", ""),
            address_1=data.get("address_1"),
            address_2=data.get("address_2"),
            address_3=data.get("address_3"),
            city=data.get("city", ""),
            state_province=data.get("state_province", ""),
            postal_code=data.get("postal_code", ""),
            country=data.get("country", ""),
            longitude=to_float(data.get("longitude")),
            latitude=to_float(data.get("latitude")),
            phone=data.get("phone"),
            website_url=data.get("website_url"),
            state=data.get("state"),
            street=data.get("street"),
        )

    def __str__(self) -> str:
        """Ładny opis obiektu przy print()."""
        location_parts = [self.city]

        if self.state_province:
            location_parts.append(self.state_province)
        if self.country:
            location_parts.append(self.country)

        location = ", ".join(location_parts)

        return (
            f"Brewery(id={self.id}, "
            f"name={self.name!r}, "
            f"type={self.brewery_type}, "
            f"location={location}, "
            f"website={self.website_url or 'brak'})"
        )


def fetch_breweries(limit: int = 20) -> List[Brewery]:
    """
    Pobiera pierwsze `limit` browarów z API
    i zwraca listę obiektów Brewery.
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": limit}

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # Rzuci wyjątek, jeśli status != 200

    data = response.json()  # lista słowników
    breweries = [Brewery.from_json(item) for item in data]
    return breweries


if __name__ == "__main__":
    # Pobranie 20 pierwszych browarów
    breweries = fetch_breweries(20)

    # Iteracja po liście i wyświetlenie każdego obiektu
    for brewery in breweries:
        print(brewery)
