def wypisz_parzyste(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:  # sprawdzamy parzystość
            print(liczba)


if __name__ == "__main__":
    liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    wypisz_parzyste(liczby)
