# ==============================
# ZADANIE 1 — main.py
# ==============================
# Plik uruchomieniowy.
# Zgodnie z treścią zadania:
# - importujemy TYLKO Product
# - NIE importujemy utils ani Order

from magazine.Product import Product


def main():
    product = Product()
    print(product)


if __name__ == "__main__":
    main()
