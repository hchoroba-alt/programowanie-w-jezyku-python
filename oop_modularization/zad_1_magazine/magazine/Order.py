# ==============================
# ZADANIE 1 — Order.py
# ==============================
# Ten moduł również importuje utils
# przy użyciu importu niezależnego.

import magazine.utils


class Order:
    """
    Klasa Order.
    Również korzysta z modułu utils.
    """

    def __str__(self):
        return magazine.utils.helper()
