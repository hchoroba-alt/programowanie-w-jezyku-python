# ==============================
# ZADANIE 1 — Product.py
# ==============================
# W tym pliku:
# - definiujemy klasę Product
# - importujemy moduł utils
# - używamy IMPORTU NIEZALEŻNEGO (absolutnego)

import magazine.utils


class Product:
    """
    Klasa Product.
    Celem jest pokazanie poprawnego importu utils.
    """

    def __str__(self):
        # Wywołujemy funkcję z utils
        return magazine.utils.helper()
