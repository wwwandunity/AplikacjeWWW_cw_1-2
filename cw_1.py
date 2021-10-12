from datetime import datetime


# Zadanie 1
lorem_ipsum = "Lorem Ipsum jest tekstem stosowanym jako przykladowy wypelniacz w przemysle poligraficznym." \
              " Zostal po raz pierwszy uzyty w XV w. przez nieznanego drukarza do wypelnienia tekstem próbnej" \
              " ksiazki. Piec wieków pózniej zaczal byc uzywany przemysle elektronicznym," \
              " pozostajac praktycznie niezmienionym. Spopularyzowal sie w latach 60. XX w. wraz z publikacja" \
              " arkuszy Letrasetu, zawierajacych fragmenty Lorem Ipsum, a ostatnio z zawierajacym rózne wersje" \
              " Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych," \
              " jak Aldus PageMaker"


# Zadanie 2
imie = "Ryszard"
nazwisko = "Staruch"

litera_1 = imie[2]
litera_2 = nazwisko[3]

liczba_liter1 = 0
liczba_liter2 = 0

for litera in lorem_ipsum:
    if litera.lower() == litera_1:
        liczba_liter1 += 1
    if litera.lower() == litera_2:
        liczba_liter2 += 1

print(f"W tekscie jest {liczba_liter1} liter {litera_1} oraz {liczba_liter2} liter {litera_2}")


# Zadanie 3
print('{:>10}'.format('test'))
print('{:_<10}'.format('test'))
print('{:^10}'.format('test'))

data = {'first': 'Hodor', 'last': 'Hodor!'}
print('{first} {last}'.format(**data))
print('{:%Y-%m-%d %H:%M}'.format(datetime(2001, 2, 3, 4, 5)))


# Zadanie 4
print(dir("eo"))
help("eo".ljust)


# Zadanie 5
print(imie[::-1].capitalize(), nazwisko[::-1].capitalize())


# Zadanie 6
lista_1_10 = [x for x in range(1, 11)]
lista_1_10, lista_6_10 = lista_1_10[:5], lista_1_10[5:]
print(lista_1_10)
print(lista_6_10)


# Zadanie 7
polaczone_listy = [0] + lista_1_10 + lista_6_10
polaczone_listy.sort(reverse=True)
print(polaczone_listy)


# Zadanie 8
lista_studentow = (
    ("123456", "Adam Malysz"),
    ("654321", "Robert Kubica"),
    ("111111", "Robert Mateja")
)


# Zadanie 9
slownik_studentow = {x[0]: x[1] for x in lista_studentow}
print(slownik_studentow)

slownik_studentow["222222"] = ["Marcin Bachleda", "30", "marcin@gmail.com", "ul. Dluga 5, Olsztyn"]
slownik_studentow["333333"] = ["Maciej Kot", "25", "maciej@gmail.com", "ul. Krotka 6, Olsztyn"]
print(slownik_studentow)


# Zadanie 10
numery_telefonow = ["123456789", "111111111", "123456789"]
print(numery_telefonow)
print(set(numery_telefonow))


# Zadanie 11
for x in range(1, 11):
    print(x)


# Zadanie 12
for x in range(0, 81, 5):
    print(100 - x)


# Zadanie 13
lista_slownikow = [
    {
        "1": "Robert Lewandowski",
        "2": "Mariusz Pudzianowski",
        "3": "Adam Roman"
    },
    {
        "4": "Antoni Ziemowit",
        "5": "Arnold Boczek",
        "6": "Mikolaj Bialach"
    }
]

napis = ""
for slownik in lista_slownikow:
    for key, value in slownik.items():
        napis += key + " "
        napis += value + "\n"

print(napis)