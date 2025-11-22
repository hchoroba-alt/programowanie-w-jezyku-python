# WERSJA 1 — klasyczna pętla
def mnoz_przez_dwa_loop(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik


# WERSJA 2 — list comprehension (krótsza, „pythonic”)
def mnoz_przez_dwa_comprehension(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]


if __name__ == "__main__":
    liczby = [1, 2, 3, 4, 5]

    print("Wersja 1:", mnoz_przez_dwa_loop(liczby))
    print("Wersja 2:", mnoz_przez_dwa_comprehension(liczby))
