def potega(liczba, wykladnik):
    wynik = liczba**wykladnik
    print(f"{liczba} do potęgi {wykladnik} to: {wynik}")


if __name__ == "__main__":
    potega(2, 3)  # 2^3 = 8
    potega(5, 2)  # 5^2 = 25
    potega(10, 0)  # 10^0 = 1
