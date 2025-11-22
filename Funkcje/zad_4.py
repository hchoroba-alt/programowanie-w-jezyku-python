def wyswietl_co_drugi(lista_liczb):
    # start: 0, stop: koniec listy, krok: 2
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])


if __name__ == "__main__":
    liczby = list(range(1, 11))  # 1–10
    wyswietl_co_drugi(liczby)
