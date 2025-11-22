def wyswietl_parzyste(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 == 0:   # liczba parzysta
            print(liczba)


if __name__ == "__main__":
    # lista liczb od 1 do 10 (10 elementów)
    liczby = list(range(1, 11))
    wyswietl_parzyste(liczby)
